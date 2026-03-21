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
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

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


def api_generate(provider, prompt, model=None, timeout=120,
                 max_tokens=4096, temperature=0.7, system=None):
    """OpenRouter-only API generate compatible with caller expectations."""
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

    payload = json.dumps({
        "model": model or "openai/gpt-4o-mini",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }).encode("utf-8")

    req = urllib.request.Request(
        _OR_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://u-model.org",
            "X-Title": "System-Stability-Score",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        text = data["choices"][0]["message"]["content"].strip()
        return LLMResult(
            success=True,
            text=text,
            elapsed=time.time() - start,
            model=model or "",
        )
    except Exception as exc:
        return LLMResult(
            success=False,
            error=str(exc)[:500],
            elapsed=time.time() - start,
            model=model or "",
        )


def compare_models(prompt, models, provider="openrouter", timeout=120):
    """Run multiple model calls in parallel. Returns dict model -> LLMResult."""
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

    with ThreadPoolExecutor(max_workers=max(1, len(models))) as pool:
        futures = [pool.submit(_call, m) for m in models]
        for fut in as_completed(futures):
            model_id, result = fut.result()
            results[model_id] = result

    return results
