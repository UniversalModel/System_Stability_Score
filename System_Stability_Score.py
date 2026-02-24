#!/usr/bin/env python3
"""
System_Stability_Score.py
=========================
Evaluates ANY system (cup, country, company, person, marriage, institution…)
using the U-Model triadic framework: Form / Position / Action.

  FORM     — What the system IS.   Stability costs TIME   (endurance against decay).
  POSITION — Where the system IS.  Stability costs SPACE  (resistance to displacement).
  ACTION   — What the system DOES. Stability costs ENERGY (expenditure leaves entropy).

Uses ai_subagent.py's existing compare_models() for parallel OpenRouter calls —
no reinvention of infrastructure.

Usage:
  python System_Stability_Score.py "United Nations" --models 50 --save
  python System_Stability_Score.py "A Glass of Water" --models 20 --save
  python System_Stability_Score.py "LA Galaxy" --domain sport/MLS --models 30 --save

Output: structured Markdown report (Page 1 Overview + Page 2 Form + Page 3 Position + Page 4 Action)
Format: mirrors "SDGs vs U-Model — Comparative Overview.md"

Author: U-Theory v24 / U-Model.org
"""
import os, sys, json, re, math, time, threading, urllib.request, statistics, argparse
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Locate & import ai_subagent.py ───────────────────────────────────────────
_HERE     = Path(__file__).parent.resolve()
_BOT_DIR  = _HERE.parent.parent / ".github" / "bot"   # v.25 -> u-score -> .github/bot
if _BOT_DIR.exists() and str(_BOT_DIR) not in sys.path:
    sys.path.insert(0, str(_BOT_DIR))

try:
    from ai_subagent import compare_models, api_generate, OPENROUTER_API_KEY
    _SUBAGENT_AVAILABLE = True
except ImportError:
    _SUBAGENT_AVAILABLE = False
    OPENROUTER_API_KEY  = ""

# ── Paths ─────────────────────────────────────────────────────────────────────
PRINCIPLES_DIR = _HERE / "principles"
REPORTS_DIR    = _HERE / "reports"
CONTEXT_DIR    = _HERE / "context"
ENV_FILE       = _BOT_DIR.parent / ".env"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# Domain context loader
# ─────────────────────────────────────────────────────────────────────────────
def load_context(domain: str, override_file: str | None = None) -> str:
    """
    Returns domain context text for injection into prompts.

    Priority order:
      1. override_file  (CLI --context FILE)
      2. context/{domain}/general.md   (auto-discovered)
      3. ""  (empty — no context available)

    NOTE: In --subject (specific) mode, callers must NOT pass context_text
    to build_prompt() — only the subject document is the source of truth.
    """
    if override_file:
        p = Path(override_file)
        if p.exists():
            return p.read_text(encoding="utf-8", errors="ignore")
        print(f"  WARNING: --context file not found: {override_file}", file=sys.stderr)
        return ""
    auto = CONTEXT_DIR / domain / "general.md"
    if auto.exists():
        return auto.read_text(encoding="utf-8", errors="ignore")
    return ""


# ── Load API key from .env if ai_subagent didn't provide it ──────────────────
def _load_env():
    env = {}
    for candidate in [ENV_FILE, _HERE.parent.parent / ".github" / ".env"]:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
            break
    return env

_ENV = _load_env()
OR_KEY = (OPENROUTER_API_KEY if _SUBAGENT_AVAILABLE and OPENROUTER_API_KEY
          else _ENV.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API_KEY", ""))

if not OR_KEY:
    print("ERROR: OPENROUTER_API_KEY not found. Set it in .github/.env", file=sys.stderr)
    sys.exit(1)

STABILITY_THRESHOLD = 0.618   # Golden Ratio
OR_BASE = "https://openrouter.ai/api/v1"
FIVE_GOALS = [
    "Minimize Public Costs",
    "Maximize Productivity & Efficiency",
    "Maximize Service to Citizens",
    "Minimize Mortality",
    "Maximize Happiness",
]


# ─────────────────────────────────────────────────────────────────────────────
# 1. Fetch models dynamically from OpenRouter API  (no YAML, no CLI)
# ─────────────────────────────────────────────────────────────────────────────
def fetch_models(n: int = 50) -> list[str]:
    """
    Returns up to n OpenRouter model IDs, auto-fetched from /api/v1/models.
    Sorts paid models cheapest-first (maximizes diversity per budget).
    Falls back to a hardcoded list if the API is unreachable.
    """
    try:
        req = urllib.request.Request(
            f"{OR_BASE}/models",
            headers={"Authorization": f"Bearer {OR_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        models = data.get("data", [])

        # Filter: skip routing meta-models and negative-price entries
        paid, free = [], []
        for m in models:
            mid = m.get("id", "")
            if mid.startswith("openrouter/"):
                continue
            price = float(m.get("pricing", {}).get("completion") or 0)
            if price < 0:
                continue
            # Skip models that don't support JSON mode well (vision/audio only)
            mod = m.get("architecture", {}).get("modality", "text")
            if mod and "text" not in mod:
                continue
            bucket = free if (price == 0 or mid.endswith(":free")) else paid
            bucket.append({"id": mid, "price": price})

        paid.sort(key=lambda x: x["price"])
        combined = [m["id"] for m in paid] + [m["id"] for m in free]
        return combined[:n]

    except Exception as e:
        print(f"  WARNING: Could not fetch models ({e}). Using fallback list.", file=sys.stderr)
        return [
            "openai/gpt-4o",
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3.7-sonnet",
            "x-ai/grok-3-beta",
            "google/gemini-2.0-flash-001",
            "anthropic/claude-3.5-haiku",
            "openai/gpt-4o-mini",
            "meta-llama/llama-3.3-70b-instruct",
            "deepseek/deepseek-chat",
            "qwen/qwen-2.5-72b-instruct",
        ][:n]


# ─────────────────────────────────────────────────────────────────────────────
# 2. Load principles
# ─────────────────────────────────────────────────────────────────────────────
def load_principles(domain: str = "universal") -> dict[str, list[str]]:
    base = PRINCIPLES_DIR / domain
    result = {}
    for cat in ["Form", "Position", "Action"]:
        for ext in [".md", ".txt"]:
            files = list(base.glob(f"{cat}{ext}")) + list(base.glob(f"{cat.lower()}{ext}"))
            if files:
                text = files[0].read_text(encoding="utf-8", errors="ignore")
                principles = re.findall(r'^\d+\.\s+\*\*(.+?)\*\*\s*[-—]\s*(.+?)$', text, re.MULTILINE)
                if principles:
                    result[cat] = [f"{n} — {d.strip()}" for n, d in principles[:15]]
                else:
                    raw = re.findall(r'^\d+\.\s+(.+)$', text, re.MULTILINE)
                    result[cat] = [p.strip() for p in raw[:15]]
                break
        if cat not in result:
            raise FileNotFoundError(f"No {cat} principles in {base}. Run 3_pillars_constructor.py to generate them.")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 3. Build evaluation prompt
# ─────────────────────────────────────────────────────────────────────────────
def build_prompt(
    entity: str,
    principles: dict[str, list[str]],
    subject_text: str | None = None,
    subject_label: str = "",
    context_text: str = "",
) -> str:
    """
    Builds the evaluation prompt.

    Two modes:
      ABSTRACT mode (no subject_text):
        Models use their general knowledge PLUS optional domain context
        (context_text) to score the system type.

      SPECIFIC mode (subject_text provided):
        Models score a SPECIFIC REAL INSTANCE based solely on the provided
        document. context_text is intentionally NOT injected here — only the
        subject document is the source of truth. No internet, no general knowledge.
    """
    def fmt(lst): return "\n".join(f"  {i+1}. {p}" for i, p in enumerate(lst))
    goals = "\n".join(f"  - {g}" for g in FIVE_GOALS)

    if subject_text:
        # ── SPECIFIC MODE: evaluate a real documented instance ──────────────
        label = subject_label or entity
        # Truncate subject if too long (keep within token budget)
        max_chars = 6000
        subject_snippet = subject_text[:max_chars]
        if len(subject_text) > max_chars:
            subject_snippet += f"\n\n[... document truncated at {max_chars} chars for token budget ...]\n"

        return f"""You are a rigorous systems analyst applying the U-Model stability framework.

You are evaluating a SPECIFIC REAL INSTANCE of **{entity}**: **{label}**

A document with measurements, observations, or research data about this specific
instance has been provided below. You MUST base your scores EXCLUSIVELY on the
data in this document. Do NOT use general knowledge about {entity} — only the
specific evidence in the document matters.

If the document does not contain enough data to assess a particular principle,
set score = 50 and state "Insufficient data in the document" in brief_assessment.

The U-Model has three pillars of stability — each with its own "price of existence":
  FORM     = what the system IS       — stability costs TIME   (endurance, resisting decay)
  POSITION = where the system IS      — stability costs SPACE  (resistance to displacement)
  ACTION   = what the system DOES     — stability costs ENERGY (expenditure leaves entropy)

For each principle score 0–100 and provide:
- score: integer 0-100  (base it ONLY on the document data)
- brief_assessment: 1-2 sentences citing SPECIFIC VALUES/FINDINGS from the document + trend (⬆️ ➡️ ⬇️)
- root_causes: 1 sentence — the main documented reason for any gap

Also score this specific subject's contribution to the Five Main Goals (0–100 each):
{goals}

Additionally provide:
- headwinds: list of 3-5 specific risks or challenges found IN THE DOCUMENT
- synergy_score: integer 0-100 (how coherent are Form+Position+Action for THIS instance)
- economic_snapshot: 2-3 sentences on sustainability / cost-of-maintenance for THIS instance
- executive_summary: 3-4 sentences characterising THIS specific instance based on the document

Respond ONLY with valid JSON — no markdown, no commentary outside the JSON:
{{
  "Form": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "Position": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "Action": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "five_goals": {{
    "Minimize Public Costs":             {{"score": 0, "assessment": "..."}},
    "Maximize Productivity & Efficiency": {{"score": 0, "assessment": "..."}},
    "Maximize Service to Citizens":      {{"score": 0, "assessment": "..."}},
    "Minimize Mortality":                {{"score": 0, "assessment": "..."}},
    "Maximize Happiness":                {{"score": 0, "assessment": "..."}}
  }},
  "headwinds": ["..."],
  "synergy_score": 0,
  "economic_snapshot": "...",
  "executive_summary": "..."
}}

--- FORM PRINCIPLES — stability costs TIME ({len(principles["Form"])} total) ---
{fmt(principles["Form"])}

--- POSITION PRINCIPLES — stability costs SPACE ({len(principles["Position"])} total) ---
{fmt(principles["Position"])}

--- ACTION PRINCIPLES — stability costs ENERGY ({len(principles["Action"])} total) ---
{fmt(principles["Action"])}

{'='*70}
SUBJECT DOCUMENT — {label}
{'='*70}
{subject_snippet}
{'='*70}"""

    else:
        # ── ABSTRACT MODE: evaluate the system type from general knowledge ───
        return f"""You are a rigorous systems analyst applying the U-Model stability framework.

System to evaluate: **{entity}**

The U-Model has three pillars of stability — each with its own "price of existence":
  FORM     = what the system IS       — stability costs TIME   (endurance, resisting decay)
  POSITION = where the system IS      — stability costs SPACE  (resistance to displacement)
  ACTION   = what the system DOES     — stability costs ENERGY (expenditure leaves entropy)

Score each principle on a 0–100 integer scale. For each principle provide:
- score: integer 0-100
- brief_assessment: 1-2 sentences with specific evidence and a trend signal (⬆️ ➡️ ⬇️)
- root_causes: 1 sentence on the main reason for any gap

Also score the system's contribution to the Five Main Goals (0–100 each):
{goals}

Additionally provide:
- headwinds: list of 3-5 current key challenges or risks (strings)
- synergy_score: integer 0-100 (internal coherence of Form+Position+Action)
- economic_snapshot: 2-3 sentences on sustainability / resource balance of this system
- executive_summary: 3-4 sentences overall characterisation

Respond ONLY with valid JSON — no markdown, no commentary outside the JSON:
{{
  "Form": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "Position": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "Action": [
    {{"principle": "...", "score": 0, "brief_assessment": "...", "root_causes": "..."}}
  ],
  "five_goals": {{
    "Minimize Public Costs":             {{"score": 0, "assessment": "..."}},
    "Maximize Productivity & Efficiency": {{"score": 0, "assessment": "..."}},
    "Maximize Service to Citizens":      {{"score": 0, "assessment": "..."}},
    "Minimize Mortality":                {{"score": 0, "assessment": "..."}},
    "Maximize Happiness":                {{"score": 0, "assessment": "..."}}
  }},
  "headwinds": ["..."],
  "synergy_score": 0,
  "economic_snapshot": "...",
  "executive_summary": "..."
}}

--- FORM PRINCIPLES — stability costs TIME ({len(principles["Form"])} total) ---
{fmt(principles["Form"])}

--- POSITION PRINCIPLES — stability costs SPACE ({len(principles["Position"])} total) ---
{fmt(principles["Position"])}

--- ACTION PRINCIPLES — stability costs ENERGY ({len(principles["Action"])} total) ---
{fmt(principles["Action"])}""" + (f"""

{'='*70}
DOMAIN CONTEXT — background knowledge (use to inform your scoring)
{'='*70}
{context_text.strip()}
{'='*70}""" if context_text.strip() else "")


# ─────────────────────────────────────────────────────────────────────────────
# 4. Call models — uses ai_subagent.compare_models() OR direct urllib fallback
# ─────────────────────────────────────────────────────────────────────────────
def call_all_models(model_ids: list[str], prompt: str, timeout: int = 90) -> list[dict]:
    """
    Calls compare_models() from ai_subagent.py (parallel, OpenRouter).
    Falls back to direct urllib if ai_subagent is not importable.
    Returns list of dicts: {model, text, success, elapsed}
    """
    total = len(model_ids)
    done  = [0]
    lock  = threading.Lock()

    def _progress(model_id, ok, u_approx=""):
        with lock:
            done[0] += 1
            sym = "✓" if ok else "✗"
            extra = f"  u≈{u_approx}" if u_approx else ""
            print(f"  [{done[0]:2d}/{total}] {model_id:<52} {sym}{extra}")

    if _SUBAGENT_AVAILABLE:
        # ── Use ai_subagent.compare_models() ─────────────────────────────────
        raw = compare_models(prompt, model_ids, provider="openrouter", timeout=timeout)
        results = []
        for mid, r in raw.items():
            ok = getattr(r, "success", False)
            txt = getattr(r, "text", "") or ""
            elapsed = getattr(r, "elapsed", 0.0)
            u_approx = _quick_u(txt)
            _progress(mid, ok, u_approx)
            results.append({"model": mid, "text": txt, "success": ok, "elapsed": elapsed})
        return results

    else:
        # ── Direct urllib fallback (same logic as before) ─────────────────────
        results = []
        results_lock = threading.Lock()
        sem = threading.Semaphore(10)

        def _call(mid):
            with sem:
                start = time.time()
                payload = json.dumps({
                    "model": mid,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1, "max_tokens": 4096,
                    "response_format": {"type": "json_object"},
                }).encode("utf-8")
                req = urllib.request.Request(
                    f"{OR_BASE}/chat/completions", data=payload,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {OR_KEY}",
                        "HTTP-Referer": "https://u-model.org",
                        "X-Title": "System-Stability-Score",
                    }, method="POST"
                )
                try:
                    with urllib.request.urlopen(req, timeout=timeout) as r:
                        raw = json.loads(r.read())
                    txt = raw["choices"][0]["message"]["content"]
                    txt = re.sub(r"^```(?:json)?\s*", "", txt.strip())
                    txt = re.sub(r"\s*```$", "", txt.strip())
                    u_approx = _quick_u(txt)
                    _progress(mid, True, u_approx)
                    with results_lock:
                        results.append({"model": mid, "text": txt, "success": True,
                                        "elapsed": round(time.time() - start, 2)})
                except Exception as e:
                    _progress(mid, False)
                    with results_lock:
                        results.append({"model": mid, "text": "", "success": False,
                                        "elapsed": round(time.time() - start, 2),
                                        "error": str(e)[:100]})

        threads = [threading.Thread(target=_call, args=(mid,), daemon=True) for mid in model_ids]
        for t in threads: t.start()
        for t in threads: t.join()
        return results


def _quick_u(text: str) -> str:
    """Fast approximate U-score from raw JSON text for progress display."""
    try:
        data = json.loads(text)
        form_scores     = [float(p["score"]) for p in data.get("Form", []) if "score" in p]
        position_scores = [float(p["score"]) for p in data.get("Position", []) if "score" in p]
        action_scores   = [float(p["score"]) for p in data.get("Action", []) if "score" in p]
        if form_scores and position_scores and action_scores:
            f = sum(form_scores)/len(form_scores)/100
            po = sum(position_scores)/len(position_scores)/100
            a = sum(action_scores)/len(action_scores)/100
            u = (f * po * a) ** (1/3)
            return f"{u:.3f}"
    except Exception:
        pass
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# 5. Parse & aggregate
# ─────────────────────────────────────────────────────────────────────────────
def _iqr(values: list) -> list:
    if len(values) < 4:
        return values
    s = sorted(values)
    q1, q3 = s[len(s)//4], s[(3*len(s))//4]
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return [v for v in values if lo <= v <= hi]

def _parse(text: str) -> dict | None:
    try:
        text = re.sub(r"^```(?:json)?\s*", "", text.strip())
        text = re.sub(r"\s*```$", "", text.strip())
        return json.loads(text)
    except Exception:
        return None

def aggregate(raw_results: list[dict], principles: dict) -> dict:
    parsed = [(r, _parse(r["text"])) for r in raw_results if r.get("success") and r.get("text")]
    parsed = [(r, d) for r, d in parsed if d is not None]
    n_ok  = len(parsed)
    n_fail= len(raw_results) - n_ok

    if not parsed:
        return {"error": "No valid JSON responses from any model."}

    # Per-principle weighted aggregation
    def _dim(dim):
        n_p = len(principles[dim])
        out = []
        for i in range(n_p):
            scores, assessments, roots = [], [], []
            for r, d in parsed:
                try:
                    item = d[dim][i]
                    scores.append((float(item["score"]), 1.0))   # weight = 1.0 (uniform for now)
                    assessments.append(item.get("brief_assessment", ""))
                    roots.append(item.get("root_causes", ""))
                except (IndexError, KeyError, TypeError):
                    pass
            if not scores:
                out.append({"principle": principles[dim][i], "score": 50, "assessment": "N/A", "root_causes": "N/A", "n": 0, "stdev": 0})
                continue
            raw_scores = [s for s, _ in scores]
            filtered   = _iqr(raw_scores)
            wmean      = sum(filtered) / len(filtered)
            stdev      = round(statistics.stdev(filtered), 1) if len(filtered) > 1 else 0.0
            # Best assessment = pick the one from the model whose score is closest to wmean
            closest_idx = min(range(len(raw_scores)), key=lambda x: abs(raw_scores[x] - wmean))
            out.append({
                "principle":   principles[dim][i],
                "score":       round(wmean),
                "assessment":  assessments[closest_idx] if assessments else "",
                "root_causes": roots[closest_idx] if roots else "",
                "n":           len(filtered),
                "stdev":       stdev,
            })
        avg = sum(p["score"] for p in out) / len(out) if out else 0
        return {"principles": out, "avg": round(avg, 1)}

    form_r     = _dim("Form")
    position_r = _dim("Position")
    action_r   = _dim("Action")

    f  = form_r["avg"] / 100
    po = position_r["avg"] / 100
    a  = action_r["avg"] / 100
    u = (f * po * a) ** (1/3) if (f > 0 and po > 0 and a > 0) else 0.0

    # Per-model U-scores (for table + stats)
    model_rows = []
    for res, d in parsed:
        try:
            fv  = sum(p["score"] for p in d["Form"])     / len(d["Form"])     / 100
            pov = sum(p["score"] for p in d["Position"]) / len(d["Position"]) / 100
            av  = sum(p["score"] for p in d["Action"])   / len(d["Action"])   / 100
            u_m = (fv * pov * av) ** (1/3)
            model_rows.append({
                "model": res["model"], "u": round(u_m, 4),
                "form": round(fv*100, 1), "position": round(pov*100, 1),
                "action": round(av*100, 1), "elapsed": round(res.get("elapsed", 0), 1),
            })
        except Exception:
            pass
    model_rows.sort(key=lambda x: x["u"], reverse=True)

    u_vals = _iqr([m["u"] for m in model_rows])
    stdev  = round(statistics.stdev(u_vals), 4) if len(u_vals) > 1 else 0.0
    n      = len(u_vals)
    se     = stdev / math.sqrt(n) if n > 0 else 0
    ci_lo  = max(0.0, round(u - 1.96*se, 4))
    ci_hi  = min(1.0, round(u + 1.96*se, 4))

    stab = "STABLE" if u >= STABILITY_THRESHOLD else ("FRAGILE" if u >= 0.4 else "CRITICAL")
    stab_sym = {"STABLE": "✓", "FRAGILE": "⚠", "CRITICAL": "✗"}[stab]
    agree = round(sum(1 for m in model_rows
                      if (m["u"] >= STABILITY_THRESHOLD) == (u >= STABILITY_THRESHOLD))
                  / len(model_rows) * 100, 1) if model_rows else 0.0

    # Five Goals
    five_goals = {}
    for goal in FIVE_GOALS:
        sc, asmt = [], []
        for _, d in parsed:
            try:
                g = d["five_goals"][goal]
                sc.append(float(g["score"]))
                asmt.append(g.get("assessment", ""))
            except (KeyError, TypeError):
                pass
        if sc:
            f = _iqr(sc)
            best_idx = min(range(len(sc)), key=lambda x: abs(sc[x] - sum(f)/len(f)))
            five_goals[goal] = {"score": round(sum(f)/len(f)), "assessment": asmt[best_idx]}
        else:
            five_goals[goal] = {"score": 50, "assessment": "insufficient data"}

    # Headwinds, synergy, economic, executive — from best model (highest u_score)
    best_data = max(parsed, key=lambda x: _quick_u(x[1] if isinstance(x[1], str) else json.dumps(x[1])) if False else 0,
                    default=(None, {}))[1] if parsed else {}
    # simpler: just take first successful parsed
    headwinds = []
    synergy_score = 70
    economic_snapshot = ""
    executive_summary = ""
    for _, d in sorted(parsed, key=lambda x: _quick_u(x[0]["text"]), reverse=True):
        headwinds         = headwinds or d.get("headwinds", [])
        synergy_score     = d.get("synergy_score", synergy_score) or synergy_score
        economic_snapshot = economic_snapshot or d.get("economic_snapshot", "")
        executive_summary = executive_summary or d.get("executive_summary", "")
        if all([headwinds, economic_snapshot, executive_summary]):
            break

    return {
        "u_score": round(u, 4), "stability": stab, "stability_sym": stab_sym,
        "form": form_r, "position": position_r, "action": action_r,
        "five_goals": five_goals, "headwinds": headwinds[:6],
        "synergy_score": synergy_score,
        "economic_snapshot": economic_snapshot,
        "executive_summary": executive_summary,
        "model_scores": model_rows,
        "n_success": n_ok, "n_failed": n_fail, "n_total": len(raw_results),
        "ci_lo": ci_lo, "ci_hi": ci_hi, "stdev": stdev, "agreement": agree,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 6. Report helpers
# ─────────────────────────────────────────────────────────────────────────────
def _bar(score: int, w: int = 20) -> str:
    f = max(0, min(w, round(score / 100 * w)))
    return "█" * f + "░" * (w - f)

def _emoji(score: int) -> str:
    if score >= 85: return "😄"
    if score >= 75: return "😃"
    if score >= 65: return "🙂"
    if score >= 55: return "😌"
    if score >= 45: return "😐"
    if score >= 35: return "😕"
    return "😟"


# ─────────────────────────────────────────────────────────────────────────────
# 7. Generate Markdown report  (style: SDGs vs U-Model — Comparative Overview)
# ─────────────────────────────────────────────────────────────────────────────
def generate_report(
    entity: str,
    domain: str,
    agg: dict,
    subject_label: str = "",
    subject_file: str = "",
) -> str:
    now   = datetime.now().strftime("%B %d, %Y")
    u     = agg["u_score"]
    fa    = agg["form"]["avg"]
    poa   = agg["position"]["avg"]
    aa    = agg["action"]["avg"]
    stab  = agg["stability"]
    sym   = agg["stability_sym"]
    n_ok  = agg["n_success"]
    n_tot = agg["n_total"]
    # Subject info for report header
    subject_mode = bool(subject_label)
    display_name = subject_label if subject_mode else entity
    mode_tag     = "SPECIFIC SUBJECT" if subject_mode else "ABSTRACT TYPE"

    L = []
    def p(*args): L.append(" ".join(str(a) for a in args))
    def br(): L.append("")

    # ── PAGE 1 ───────────────────────────────────────────────────────────────
    p(f"# {display_name} — U-Model System Stability Report (Page 1)")
    br()
    p("## Introduction")
    br()
    if subject_mode:
        p(
            f"This report evaluates a **specific real instance**: **{display_name}** "
            f"(system type: *{entity}*), using the **U-Model** triadic stability framework. "
            f"Principles were generated by `3_pillars_constructor.py` for the **{entity}** system type "
            f"and represent ideal stability conditions. "
            f"The AI jury scored **this specific subject** against those principles "
            f"using ONLY the provided subject document (`{subject_file}`) — not general knowledge."
        )
        br()
        p(
            f"> **Evaluation mode: SPECIFIC SUBJECT** — scores reflect the documented state of "
            f"**{display_name}**, not the abstract average of {entity}."
        )
    else:
        p(
            f"This report evaluates the systemic stability of **{entity}** using the "
            f"**U-Model** — a universal triadic framework that measures stability across three dimensions: "
            f"**Form** (what the system IS — stability costs *Time*, endurance against decay), "
            f"**Position** (where the system IS — stability costs *Space*, resistance to displacement), and "
            f"**Action** (what the system DOES — stability costs *Energy*, expenditure leaves entropy). "
            f"Together these assess the system's contribution to five Main Goals: "
            f"Minimizing Public Costs, Maximizing Productivity and Efficiency, Maximizing Service to Citizens, "
            f"Minimizing Mortality, and Maximizing Happiness."
        )
    br()
    p(
        f"The evaluation is a **consensus derived from {n_ok} AI models** (of {n_tot} called) "
        f"operating in parallel via OpenRouter, each applying the U-Model evaluation framework "
        f"independently. Outliers removed via IQR. Date: {now}. Domain: `{domain}`."
    )
    br()

    p("## What it is (at a glance)")
    br()
    if agg.get("executive_summary"):
        p(f"**{entity}:** {agg['executive_summary']}")
        br()
    p(f"**U-Model Status: {stab} {sym}** (U-Score: **{u:.4f}**)")
    br()

    p("```")
    p(f"  FORM     (costs Time)    [{_bar(int(fa),  24)}]  {fa:.1f}/100")
    p(f"  POSITION (costs Space)   [{_bar(int(poa), 24)}]  {poa:.1f}/100")
    p(f"  ACTION   (costs Energy)  [{_bar(int(aa),  24)}]  {aa:.1f}/100")
    p(f"  ────────────────────────────────────────────────────")
    p(f"  U-Score  =  {u:.4f}   [{_bar(int(u*100), 30)}]")
    p(f"  STATUS:  {stab} {sym}   (threshold ≥ {STABILITY_THRESHOLD} — Golden Ratio)")
    p(f"  95% CI:  [{agg['ci_lo']:.4f} – {agg['ci_hi']:.4f}]   σ = {agg['stdev']:.4f}")
    p(f"  Models:  {n_ok}/{n_tot} successful   |   {agg['agreement']:.0f}% consensus agreement")
    p("```")
    br()

    p("## Alignment with the Five Main Goals (coverage matrix)")
    br()
    p(f"| U-Model Main Goal | {entity} Performance | How U-Model measures it | Score |")
    p("|:---|:---|:---|:---:|")
    goal_pillars = {
        "Minimize Public Costs":              "Form: structural efficiency & anti-fragility; Position: minimal friction costs; Action: low-waste operations.",
        "Maximize Productivity & Efficiency": "Action: efficient energy expenditure; Form: clear & stable structure; Position: optimal placement.",
        "Maximize Service to Citizens":       "Action: reliable delivery; Position: accessible & stable location; Form: trustworthy identity.",
        "Minimize Mortality":                 "Form: refusal to decay/harm; Action: protective behaviors; Position: safe placement.",
        "Maximize Happiness":                 "Position: stable meaningful place; Action: purposeful doing; Form: dignified identity over time.",
    }
    for goal in FIVE_GOALS:
        g = agg["five_goals"].get(goal, {"score": 50, "assessment": "N/A"})
        em = _emoji(g["score"])
        p(f"| **{goal}** | {g['assessment']} | {goal_pillars.get(goal, '')} | {g['score']}% {em} |")
    br()

    p("## Methodological differences (why the score matters)")
    br()
    p("**Scope:** U-Model is a universal stability scorecard — it measures *how well the system maintains its Form, holds its Position, and sustains its Action* at a bearable price.")
    br()
    p("**Three prices of existence:** You pay with **Time** to hold Form (endurance against decay). You pay with **Space** to hold Position (resistance to displacement). You pay with **Energy** to execute Action (expenditure leaves entropy).")
    br()
    p("**Actionability:** U-Model pinpoints *which pillar is most costly* and where the system is losing stability.")
    br()
    p(f"**Formula:** `U = ∛(Form × Position × Action)` — geometric mean: all three pillars must score well. "
      f"A system with Form = 1.0, Position = 1.0, Action = 0 has U = 0. No pillar can compensate for another's collapse.")
    br()

    p("## Status & Headwinds (Current Snapshot)")
    br()
    if agg.get("headwinds"):
        for hw in agg["headwinds"]:
            p(f"- {hw}")
    else:
        p("- No specific headwinds identified.")
    br()
    p("(Trend notation per U-Model guidance.)")
    br()

    p("## Synergy & division of labor")
    br()
    syn = agg.get("synergy_score", 70)
    level = "High" if syn >= 70 else ("Medium" if syn >= 50 else "Low")
    p(f"**{level} internal coherence (score: {syn}%):** The Form, Position and Action pillars "
      f"of this system reinforce each other at {syn}% effectiveness — higher means the system "
      f"spends its Time, Space, and Energy without internal contradiction.")
    br()

    p("## Economic rationale snapshot (directional)")
    br()
    if agg.get("economic_snapshot"):
        p(agg["economic_snapshot"])
    else:
        p("_Economic snapshot not available._")
    br()

    # ── PAGE 1 tail (model jury overview) ───────────────────────────────────
    p("## Model Jury Breakdown (top results)")
    br()
    p("| Model | U-Score | Form (Time) | Position (Space) | Action (Energy) |")
    p("|:---|:---:|:---:|:---:|:---:|")
    for m in agg["model_scores"][:15]:
        p(f"| `{m['model']}` | **{m['u']:.4f}** | {m['form']} | {m['position']} | {m['action']} |")
    if len(agg["model_scores"]) > 15:
        p(f"| _...and {len(agg['model_scores'])-15} more models_ | | | | |")
    br()
    p(f"_Category averages & U-score computed from {n_ok} model responses. "
      f"Formula: U = ∛(Form × Position × Action). Threshold: ≥ {STABILITY_THRESHOLD} = Stable Existence._")
    br()
    p(f"Please, if you appreciate our work or are satisfied with the result, "
      f"please invest in us http://Donate.U-Model.org . "
      f"For more detailed insights or to support our work, please visit our official website: http://U-Model.org .")
    br()

    # ── PAGE 2: Form ─────────────────────────────────────────────────────────
    p("<br>")
    br()
    p(f"# {entity} vs U-Model — System Stability Overview (Page 2)")
    br()
    p(f"## Form (Stability of Structure — costs Time)")
    br()
    p("Evaluates the system's ability to *persist as itself* over time — "
      "maintaining identity, structure, and integrity against decay, entropy, and dissolution.")
    br()

    for i, pd in enumerate(agg["form"]["principles"], 1):
        sc  = pd["score"]
        em  = _emoji(sc)
        name = pd["principle"].split(" — ")[0] if " — " in pd["principle"] else pd["principle"]
        desc = pd["principle"].split(" — ", 1)[1] if " — " in pd["principle"] else ""
        p(f"### {i}) {name}")
        br()
        if desc:
            p(f"_{desc}_")
            br()
        p(f"**Score: {sc}% {em}**   `{_bar(sc, 20)}`   (n={pd.get('n','?')} models, σ={pd.get('stdev',0)})")
        br()
        if pd.get("assessment"):
            p(f"**Assessment.** {pd['assessment']}")
            br()
        if pd.get("root_causes"):
            p(f"**Root causes of gap.** {pd['root_causes']}")
            br()
    p(f"> **Form Average: {agg['form']['avg']:.1f}% — {_emoji(int(agg['form']['avg']))}**")
    br()
    p(f"Continue to Page 3 (Position)?")
    br()

    # ── PAGE 3: Position ─────────────────────────────────────────────────────
    p("<br>")
    br()
    p(f"# {entity} vs U-Model — System Stability Overview (Page 3)")
    br()
    p(f"## Position (Stability of Place — costs Space)")
    br()
    p("Evaluates the system's ability to *hold its place* — "
      "maintaining its location, relationships, and resistance to displacement or disintegration of context.")
    br()

    for i, pd in enumerate(agg["position"]["principles"], 1):
        sc   = pd["score"]
        em   = _emoji(sc)
        name = pd["principle"].split(" — ")[0] if " — " in pd["principle"] else pd["principle"]
        desc = pd["principle"].split(" — ", 1)[1] if " — " in pd["principle"] else ""
        p(f"### {i}) {name}")
        br()
        if desc:
            p(f"_{desc}_")
            br()
        p(f"**Score: {sc}% {em}**   `{_bar(sc, 20)}`   (n={pd.get('n','?')} models, σ={pd.get('stdev',0)})")
        br()
        if pd.get("assessment"):
            p(f"**Assessment.** {pd['assessment']}")
            br()
        if pd.get("root_causes"):
            p(f"**Root causes of gap.** {pd['root_causes']}")
            br()
    p(f"> **Position Average: {agg['position']['avg']:.1f}% — {_emoji(int(agg['position']['avg']))}**")
    br()
    p(f"Continue to Page 4 (Action)?")
    br()

    # ── PAGE 4: Action ───────────────────────────────────────────────────────
    p("<br>")
    br()
    p(f"# {entity} vs U-Model — System Stability Overview (Page 4)")
    br()
    p(f"## Action (Stability of Doing — costs Energy)")
    br()
    p("Evaluates the system's ability to *act without self-destruction* — "
      "executing its function efficiently, with change that leaves tolerable trace (manageable entropy).")
    br()

    for i, pd in enumerate(agg["action"]["principles"], 1):
        sc   = pd["score"]
        em   = _emoji(sc)
        name = pd["principle"].split(" — ")[0] if " — " in pd["principle"] else pd["principle"]
        desc = pd["principle"].split(" — ", 1)[1] if " — " in pd["principle"] else ""
        p(f"### {i}) {name}")
        br()
        if desc:
            p(f"_{desc}_")
            br()
        p(f"**Score: {sc}% {em}**   `{_bar(sc, 20)}`   (n={pd.get('n','?')} models, σ={pd.get('stdev',0)})")
        br()
        if pd.get("assessment"):
            p(f"**Assessment.** {pd['assessment']}")
            br()
        if pd.get("root_causes"):
            p(f"**Root causes of gap.** {pd['root_causes']}")
            br()
    p(f"> **Action Average: {agg['action']['avg']:.1f}% — {_emoji(int(agg['action']['avg']))}**")
    br()

    # ── Final summary ────────────────────────────────────────────────────────
    p("---")
    br()
    p(f"## Final U-Score — {entity}")
    br()
    p("```")
    p(f"  ══════════════════════════════════════════════════════")
    p(f"  System:   {entity}")
    p(f"  Domain:   {domain}")
    p(f"  Date:     {now}")
    p(f"  Models:   {n_ok}/{n_tot} successful")
    p(f"  ══════════════════════════════════════════════════════")
    p(f"  FORM     {fa:.1f}%   {_bar(int(fa),  22)}  (costs Time)")
    p(f"  POSITION {poa:.1f}%   {_bar(int(poa), 22)}  (costs Space)")
    p(f"  ACTION   {aa:.1f}%   {_bar(int(aa),  22)}  (costs Energy)")
    p(f"  ──────────────────────────────────────────────────────")
    p(f"  U-SCORE  {u:.4f}    {stab} {sym}")
    p(f"  95% CI   [{agg['ci_lo']:.4f} – {agg['ci_hi']:.4f}]   σ = {agg['stdev']:.4f}")
    p(f"  AGREE    {agg['agreement']:.0f}% of models agree with {stab}")
    p(f"  ══════════════════════════════════════════════════════")
    p("```")
    br()
    p(f"_Generated by System_Stability_Score.py · powered by ai_subagent.compare_models() · "
      f"U-Model v24 · AI jury of {n_ok} models · [U-Model.org](https://u-model.org)_")
    br()
    p(f"_Please support our work: [Donate.U-Model.org](http://Donate.U-Model.org) | "
      f"[U-Model.org](http://U-Model.org)_")

    return "\n".join(L)


# ─────────────────────────────────────────────────────────────────────────────
# 8. Terminal summary
# ─────────────────────────────────────────────────────────────────────────────
def print_summary(entity: str, agg: dict):
    u   = agg["u_score"]
    fa  = agg["form"]["avg"]
    poa = agg["position"]["avg"]
    aa  = agg["action"]["avg"]
    W   = 70
    print("\n" + "═"*W)
    print(f"  SYSTEM STABILITY SCORE — {entity}")
    print(f"  {agg['n_success']}/{agg['n_total']} models succeeded")
    print("═"*W)
    print(f"  FORM     (costs Time)    [{_bar(int(fa),  28)}]  {fa:.1f}")
    print(f"  POSITION (costs Space)   [{_bar(int(poa), 28)}]  {poa:.1f}")
    print(f"  ACTION   (costs Energy)  [{_bar(int(aa),  28)}]  {aa:.1f}")
    print("─"*W)
    print(f"  U-SCORE  =  {u:.4f}   [{_bar(int(u*100), 38)}]")
    print(f"  STATUS:  {agg['stability']} {agg['stability_sym']}")
    print(f"  95% CI:  [{agg['ci_lo']:.4f} – {agg['ci_hi']:.4f}]   σ = {agg['stdev']:.4f}")
    print(f"  Agreement: {agg['agreement']:.0f}%")
    print("═"*W)
    if agg["model_scores"]:
        print(f"\n  {'Model':<50} {'U':>6}  Form  Pos   Action")
        print("  " + "─"*70)
        for m in agg["model_scores"][:12]:
            print(f"  {m['model']:<50} {m['u']:>6.4f}  {m['form']:.0f}    {m['position']:.0f}    {m['action']:.0f}")
    print(f"\n  U = ∛(Form × Position × Action)   Threshold ≥ {STABILITY_THRESHOLD} = Stable Existence")
    print("═"*W + "\n")


# ─────────────────────────────────────────────────────────────────────────────
# 9. CLI
# ─────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description="System_Stability_Score — U-Model AI jury evaluation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Abstract evaluation (general knowledge about the system type):
  python System_Stability_Score.py "Human Heart" --domain biology/heart --models 20 --save

  # Specific subject evaluation (document-grounded — score THIS particular heart):
  python System_Stability_Score.py "Human Heart" --domain biology/heart \\
      --subject patient_john.txt --subject-label "John D., 52yr Male, ECG+echo" \\
      --models 20 --save
"""
    )
    ap.add_argument("entity",    help='System TYPE to evaluate (matches the domain principles), e.g. "Human Heart"')
    ap.add_argument("--domain",  default="universal", help="Principle domain folder (default: universal)")
    ap.add_argument("--models",  type=int, default=10, help="Number of OpenRouter models (default: 10, max: 50)")
    ap.add_argument("--timeout", type=int, default=90,  help="Per-model timeout in seconds")
    ap.add_argument("--save",    action="store_true",   help="Save Markdown report")
    ap.add_argument(
        "--subject",
        metavar="FILE",
        help="Path to a document about a SPECIFIC instance (e.g. medical report, lab results, audit). "
             "When provided, models evaluate THIS document instead of using general knowledge."
    )
    ap.add_argument(
        "--subject-label",
        dest="subject_label",
        default="",
        metavar="LABEL",
        help="Short label for the specific subject, e.g. 'Patient John, 52yr Male, ECG+echo 2026'"
    )
    ap.add_argument(
        "--context",
        metavar="FILE",
        default=None,
        help="Override path to domain context file (default: context/{domain}/general.md). "
             "Ignored automatically when --subject is used (specific mode is document-only)."
    )
    args = ap.parse_args()

    entity = args.entity
    n      = min(args.models, 50)

    # ── Load subject document if provided ─────────────────────────────────────
    subject_text  = None
    subject_label = ""
    subject_file  = ""
    context_text  = ""
    if args.subject:
        sp = Path(args.subject)
        if not sp.exists():
            print(f"ERROR: Subject file not found: {sp}", file=sys.stderr)
            sys.exit(1)
        subject_text  = sp.read_text(encoding="utf-8", errors="ignore")
        subject_label = args.subject_label or sp.stem
        subject_file  = sp.name
        print(f"\n  Subject document: {sp.name}  ({len(subject_text):,} chars)")
        print(f"  Subject label:    {subject_label}")
        print(f"  Mode:             SPECIFIC SUBJECT EVALUATION (context ignored, document is sole source)")
        # context intentionally NOT loaded in specific mode
    else:
        # Abstract mode: load domain context to ground the evaluation
        context_text = load_context(args.domain, override_file=args.context)
        ctx_src = (args.context or str(CONTEXT_DIR / args.domain / "general.md"))
        if context_text:
            print(f"\n  Mode:             ABSTRACT TYPE EVALUATION + domain context")
            print(f"  Context:          {ctx_src}  ({len(context_text):,} chars)")
        else:
            print(f"\n  Mode:             ABSTRACT TYPE EVALUATION (no domain context found)")
            print(f"  Tip: create context/{args.domain}/general.md for grounded evaluation")

    print(f"\n  Loading principles — domain: {args.domain}")
    principles = load_principles(args.domain)
    for dim, lst in principles.items():
        print(f"    {dim}: {len(lst)} principles")

    print(f"\n  Fetching {n} models from OpenRouter...")
    model_ids = fetch_models(n)
    print(f"  Selected: {len(model_ids)} models")

    infra = "ai_subagent.compare_models()" if _SUBAGENT_AVAILABLE else "direct urllib (ai_subagent not found)"
    print(f"  Engine: {infra}")

    target = subject_label if subject_label else entity
    print(f"\n  Building evaluation prompt for: {target}")
    prompt = build_prompt(entity, principles,
                          subject_text=subject_text,
                          subject_label=subject_label,
                          context_text=context_text)
    print(f"  Prompt: {len(prompt):,} chars")

    print(f"\n  Calling {len(model_ids)} models in parallel...")
    print("-"*68)
    raw = call_all_models(model_ids, prompt, timeout=args.timeout)
    print("-"*68)

    print(f"\n  Aggregating...")
    agg = aggregate(raw, principles)

    if "error" in agg:
        print(f"ERROR: {agg['error']}", file=sys.stderr)
        sys.exit(1)

    print_summary(target, agg)

    if args.save:
        report = generate_report(entity, args.domain, agg,
                                  subject_label=subject_label, subject_file=subject_file)
        safe_name = subject_label if subject_label else entity
        safe   = re.sub(r'[^\w\s-]', '', safe_name).strip().replace(' ', '_')[:40]
        ts     = datetime.now().strftime("%Y%m%d_%H%M%S")
        path   = REPORTS_DIR / f"SSS_{safe}_{ts}.md"
        path.write_text(report, encoding="utf-8")
        print(f"  Report saved: {path}\n")

if __name__ == "__main__":
    main()
