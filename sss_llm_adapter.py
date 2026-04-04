#!/usr/bin/env python3
"""Minimal OpenRouter adapter for System_Stability_Score-main.

This module keeps only the LLM functionality needed by this project:
- OPENROUTER_API_KEY export
- api_generate(provider="openrouter", ...)
- compare_models(...)

It intentionally avoids heavy dependencies on external orchestrators.
"""

import json
import os
import time
import threading
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Retry / rate-limit constants ──────────────────────────────────────────────
_MAX_RETRIES        = 3
_BACKOFF_BASE       = 1.0        # seconds: 1, 2, 4
_RETRYABLE_CODES    = {429, 500, 502, 503, 504}
_MAX_CONCURRENT     = 5          # OpenRouter concurrency guard
_CONCURRENT_SEM     = threading.Semaphore(_MAX_CONCURRENT)

_THIS = Path(__file__).resolve()
_ENV_CANDIDATES = [
    _THIS.parent / ".env",
    _THIS.parent.parent / ".github" / ".env",
    _THIS.parent.parent.parent / ".github" / ".env",
]


def _load_env() -> dict:
    env = {}
    for candidate in _ENV_CANDIDATES:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
            break
    return env


_ENV = _load_env()
OPENROUTER_API_KEY = _ENV.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API_KEY", "")
_OR_URL = "https://openrouter.ai/api/v1/chat/completions"


@dataclass
class LLMResult:
    success: bool
    text: str = ""
    elapsed: float = 0.0
    error: str = ""
    model: str = ""


def _do_request(url, payload_bytes, headers, timeout):
    """Low-level HTTP POST; returns (data_dict, http_code) or raises."""
    req = urllib.request.Request(url, data=payload_bytes, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace")), resp.status


def _http_code_from_exc(exc):
    """Extract HTTP status code from urllib exception if possible."""
    code = getattr(exc, "code", None)
    return int(code) if code is not None else 0


def api_generate(provider, prompt, model=None, timeout=120,
                 max_tokens=4096, temperature=0.7, system=None):
    """OpenRouter API generate with retry, backoff, and response_format fallback."""
    start = time.time()

    if provider != "openrouter":
        return LLMResult(
            success=False,
            error=f"Unsupported provider in local adapter: {provider}",
            elapsed=time.time() - start,
            model=model or "",
        )

    if not OPENROUTER_API_KEY:
        return LLMResult(
            success=False,
            error="OPENROUTER_API_KEY not found",
            elapsed=time.time() - start,
            model=model or "",
        )

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://u-model.org",
        "X-Title": "System-Stability-Score",
    }

    body_base = {
        "model": model or "openai/gpt-4o-mini",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    # Try with response_format first; fall back without it on 400
    for use_json_format in (True, False):
        body = {**body_base}
        if use_json_format:
            body["response_format"] = {"type": "json_object"}
        payload = json.dumps(body).encode("utf-8")

        for attempt in range(_MAX_RETRIES):
            try:
                with _CONCURRENT_SEM:
                    data, _ = _do_request(_OR_URL, payload, headers, timeout)
                text = data["choices"][0]["message"]["content"].strip()
                return LLMResult(
                    success=True,
                    text=text,
                    elapsed=time.time() - start,
                    model=model or "",
                )
            except Exception as exc:
                code = _http_code_from_exc(exc)
                # 400 with response_format → retry without it
                if code == 400 and use_json_format:
                    break
                # Retryable server/rate errors
                if code in _RETRYABLE_CODES and attempt < _MAX_RETRIES - 1:
                    wait = _BACKOFF_BASE * (2 ** attempt)
                    time.sleep(wait)
                    continue
                # Non-retryable or last attempt
                if not (code == 400 and use_json_format):
                    return LLMResult(
                        success=False,
                        error=f"HTTP {code}: {str(exc)[:400]}",
                        elapsed=time.time() - start,
                        model=model or "",
                    )

    return LLMResult(
        success=False,
        error="All retries exhausted",
        elapsed=time.time() - start,
        model=model or "",
    )


def compare_models(prompt, models, provider="openrouter", timeout=120):
    """Run multiple model calls in parallel (capped at _MAX_CONCURRENT). Returns dict model -> LLMResult."""
    results = {}

    def _call(model_id):
        return model_id, api_generate(
            provider,
            prompt,
            model=model_id,
            timeout=timeout,
            max_tokens=4096,
            temperature=0.1,
        )

    with ThreadPoolExecutor(max_workers=min(_MAX_CONCURRENT, len(models))) as pool:
        futures = [pool.submit(_call, m) for m in models]
        for fut in as_completed(futures):
            model_id, result = fut.result()
            results[model_id] = result

    return results


# ── Cost estimation (Patch 1.5) ───────────────────────────────────────────────
# Approximate per-1M-token prices for popular models (USD).
# Sources: openrouter.ai/pricing — updated 2026-04.
_MODEL_PRICING: dict[str, dict[str, float]] = {
    "openai/gpt-4o":              {"prompt": 2.50, "completion": 10.00},
    "openai/gpt-4o-mini":         {"prompt": 0.15, "completion": 0.60},
    "anthropic/claude-3.5-sonnet": {"prompt": 3.00, "completion": 15.00},
    "anthropic/claude-3.7-sonnet": {"prompt": 3.00, "completion": 15.00},
    "anthropic/claude-opus-4":    {"prompt": 15.0, "completion": 75.00},
    "anthropic/claude-3.5-haiku": {"prompt": 0.80, "completion": 4.00},
    "google/gemini-2.0-flash-001":{"prompt": 0.10, "completion": 0.40},
    "google/gemini-2.5-pro":      {"prompt": 1.25, "completion": 10.00},
    "meta-llama/llama-3.3-70b-instruct": {"prompt": 0.39, "completion": 0.39},
    "deepseek/deepseek-chat":     {"prompt": 0.14, "completion": 0.28},
    "qwen/qwen-2.5-72b-instruct": {"prompt": 0.40, "completion": 0.40},
    "x-ai/grok-3-beta":           {"prompt": 3.00, "completion": 15.00},
    "moonshotai/kimi-k2":         {"prompt": 1.00, "completion": 3.00},
}


def estimate_cost(model: str, prompt_chars: int, max_tokens: int = 4096) -> float:
    """
    Rough cost estimate in USD for a single call.
    Uses ~4 chars/token heuristic for prompt length.
    Returns 0.0 if model pricing is unknown.
    """
    pricing = _MODEL_PRICING.get(model)
    if not pricing:
        return 0.0
    est_prompt_tokens = prompt_chars / 4
    cost = (est_prompt_tokens / 1e6) * pricing["prompt"] + \
           (max_tokens / 1e6) * pricing["completion"]
    return round(cost, 6)


def estimate_batch_cost(models: list[str], prompt_chars: int,
                        max_tokens: int = 4096) -> float:
    """Estimate total cost for a batch of model calls."""
    return round(sum(estimate_cost(m, prompt_chars, max_tokens) for m in models), 4)
