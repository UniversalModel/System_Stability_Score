#!/usr/bin/env python3
"""
3_pillars_constructor.py
========================
Generates domain-specific Form / Position / Action principles for ANY system
using a top-tier AI model (Opus / Kimi / Gemini) as the ARCHITECT.

The philosophical foundation (U-Theory, Three Prices of Existence):
  ┌─────────────┬──────────────────────────────────────────────────────────────┐
  │  FORM       │  What the system IS.   Stability costs TIME   (endurance).  │
  │  POSITION   │  Where the system IS.  Stability costs SPACE  (resistance). │
  │  ACTION     │  What the system DOES. Stability costs ENERGY (entropy).    │
  └─────────────┴──────────────────────────────────────────────────────────────┘

Key insight: NOT stability at any price — stability at a TOLERABLE price.
  - Form pays with Time to endure, but excessive rigidity leads to brittle collapse.
  - Position pays with Space to hold place, but total isolation leads to irrelevance.
  - Action pays with Energy to act, but exhaustion without trace leads to dissolution.

Usage (interactive):
  python 3_pillars_constructor.py

Usage (CLI):
  python 3_pillars_constructor.py --system "A Glass of Water" --n 15 --domain glass
  python 3_pillars_constructor.py --system "A Marriage"       --n 12 --domain marriage
  python 3_pillars_constructor.py --system "United Nations"  --n 15 --domain un
  python 3_pillars_constructor.py --system "Human Heart"     --n 10 --domain biology/heart

Outputs (saved to principles/<domain>/):
  Form.md       — principles of stable identity over time
  Position.md   — principles of stable location / relationship context
  Action.md     — principles of stable purposeful doing

After generation, use System_Stability_Score.py to evaluate any system with these principles:
  python System_Stability_Score.py "A Glass of Water" --domain glass --models 20 --save

Author: U-Theory v24 / U-Model.org
"""
import os, sys, json, re, time, urllib.request, argparse, textwrap
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Paths & imports ───────────────────────────────────────────────────────────
_HERE    = Path(__file__).parent.resolve()
_BOT_DIR = _HERE.parent.parent / ".github" / "bot"
if _BOT_DIR.exists() and str(_BOT_DIR) not in sys.path:
    sys.path.insert(0, str(_BOT_DIR))

try:
    from ai_subagent import api_generate, OPENROUTER_API_KEY
    _SUBAGENT_AVAILABLE = True
except ImportError:
    _SUBAGENT_AVAILABLE = False
    OPENROUTER_API_KEY  = ""

PRINCIPLES_DIR = _HERE / "principles"
CONTEXT_DIR    = _HERE / "context"
ENV_FILE       = _BOT_DIR.parent / ".env"


# ─────────────────────────────────────────────────────────────────────────────
# Domain context loader
# ─────────────────────────────────────────────────────────────────────────────
def load_context(domain: str, override_file: str | None = None) -> str:
    """
    Returns domain context text to inject into the construction prompt.

    Priority:
      1. override_file (CLI --context FILE)
      2. context/{domain}/general.md  (auto-discovered)
      3. "" (no context)
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

# ── Load API key ──────────────────────────────────────────────────────────────
def _load_env() -> dict:
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

_ENV   = _load_env()
OR_KEY = (OPENROUTER_API_KEY if _SUBAGENT_AVAILABLE and OPENROUTER_API_KEY
          else _ENV.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API_KEY", ""))

OR_BASE = "https://openrouter.ai/api/v1"

# ── Architect models — tried in order until one succeeds ─────────────────────
ARCHITECT_MODELS = [
    "anthropic/claude-opus-4",          # best reasoning
    "moonshotai/kimi-k2",               # outstanding at structured generation
    "google/gemini-2.5-pro",            # excellent instruction following
    "anthropic/claude-3.7-sonnet",      # proven fallback
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o",
]


# ─────────────────────────────────────────────────────────────────────────────
# 1. Check which architect models are available on OpenRouter
# ─────────────────────────────────────────────────────────────────────────────
def get_available_architects() -> list[str]:
    try:
        req = urllib.request.Request(
            f"{OR_BASE}/models",
            headers={"Authorization": f"Bearer {OR_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read())
        available = {m["id"] for m in data.get("data", [])}
        found = [m for m in ARCHITECT_MODELS if m in available]
        return found if found else ARCHITECT_MODELS[:3]
    except Exception:
        return ARCHITECT_MODELS[:3]


# ─────────────────────────────────────────────────────────────────────────────
# 2. Build the construction prompt
# ─────────────────────────────────────────────────────────────────────────────
def build_construction_prompt(system_name: str, n: int, context_text: str = "") -> str:
    return f"""You are the ARCHITECT of stability principles for the U-Model framework.

Your task: generate the {n} most essential principles for each of three stability pillars
for this specific system: **{system_name}**

─────────────────────────────────────────────────────────────────────────────
FRAMEWORK: THREE PRICES OF EXISTENCE (U-Theory)
─────────────────────────────────────────────────────────────────────────────

Every system that exists pays three inescapable prices:

  FORM     = what the system IS
             Stability costs TIME (endurance — resisting decay, maintaining identity)
             → But: excessive rigidity makes the form brittle and catastrophically fragile.
               The goal is durable, not rigid. Tolerable time-cost, not eternal preservation.

  POSITION = where the system IS
             Stability costs SPACE (resistance — resisting displacement, holding context)
             → But: total resistance to displacement leads to isolation and irrelevance.
               The goal is grounded, not stuck. Tolerable space-cost, not immovability.

  ACTION   = what the system DOES
             Stability costs ENERGY (expenditure — change leaves trace, entropy is real)
             → But: action that exhausts all energy without sustainable trace leads to collapse.
               The goal is effective, not exhausting. Tolerable energy-cost, not zero-action.

─────────────────────────────────────────────────────────────────────────────
YOUR TASK
─────────────────────────────────────────────────────────────────────────────

For the system **{system_name}**, generate {n} principles for EACH pillar.

Each principle must:
1. Be SPECIFIC to this system (not generic platitudes)
2. Define what GUARANTEES stability OF THAT PILLAR at a BEARABLE PRICE
3. Name what makes it FAIL when violated
4. Be FALSIFIABLE — you can observe whether the system follows it or not
5. Reference the implicit "price" dimension (time/space/energy) in its meaning

Format of each principle:
  "name": Short evocative name (2-5 words)
  "description": 1 sentence — what this principle states and why it matters for stability

CRITICAL: Principles are not goals or values. They are STABILITY CONDITIONS.
  ✓ "The glass maintains wall thickness above the yield limit of the material"
  ✗ "The glass should be strong" (too generic)
  ✓ "The glass returns to equilibrium position after perturbation within 1 oscillation"  
  ✗ "The glass should be stable" (tautological)

─────────────────────────────────────────────────────────────────────────────
RESPOND ONLY WITH VALID JSON — no markdown, no commentary:
─────────────────────────────────────────────────────────────────────────────
{{
  "system": "{system_name}",
  "theory": "1-2 sentences: what kind of system is this and what defines its existence?",
  "Form": [
    {{"name": "...", "description": "..."}},
    ...{n} items total
  ],
  "Position": [
    {{"name": "...", "description": "..."}},
    ...{n} items total
  ],
  "Action": [
    {{"name": "...", "description": "..."}},
    ...{n} items total
  ],
  "prices_commentary": {{
    "Form":     "1 sentence: how does this system specifically pay the price of Time to maintain Form?",
    "Position": "1 sentence: how does this system specifically pay the price of Space to maintain Position?",
    "Action":   "1 sentence: how does this system specifically pay the price of Energy to execute Action?"
  }}
}}"""  + (f"""

{'='*70}
DOMAIN CONTEXT—reference knowledge for generating accurate principles
{'='*70}
{context_text.strip()}
{'='*70}""" if context_text.strip() else "")


# ─────────────────────────────────────────────────────────────────────────────
# 3. Call the architect model  (ai_subagent.api_generate OR direct urllib)
# ─────────────────────────────────────────────────────────────────────────────
def call_architect(prompt: str, model_id: str, timeout: int = 120) -> str | None:
    print(f"  → Calling architect: {model_id} ...", end="", flush=True)
    start = time.time()

    if _SUBAGENT_AVAILABLE:
        try:
            result = api_generate(
                "openrouter", prompt,
                model=model_id, timeout=timeout,
                max_tokens=6000, temperature=0.2,
            )
            elapsed = round(time.time() - start, 1)
            if result and getattr(result, "success", False):
                print(f" ✓ {elapsed}s")
                return getattr(result, "text", "")
            else:
                err = getattr(result, "error", "unknown")
                print(f" ✗ {err}")
                return None
        except Exception as e:
            print(f" ✗ {e}")
            return None

    else:
        # direct urllib fallback
        payload = json.dumps({
            "model": model_id,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2, "max_tokens": 6000,
            "response_format": {"type": "json_object"},
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{OR_BASE}/chat/completions", data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OR_KEY}",
                "HTTP-Referer": "https://u-model.org",
                "X-Title": "U-Model-PillarsConstructor",
            }, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = json.loads(r.read())
            elapsed = round(time.time() - start, 1)
            print(f" ✓ {elapsed}s")
            txt = raw["choices"][0]["message"]["content"]
            txt = re.sub(r"^```(?:json)?\s*", "", txt.strip())
            txt = re.sub(r"\s*```$", "", txt.strip())
            return txt
        except Exception as e:
            print(f" ✗ {e}")
            return None


# ─────────────────────────────────────────────────────────────────────────────
# 4. Parse the JSON response
# ─────────────────────────────────────────────────────────────────────────────
def parse_response(text: str) -> dict | None:
    try:
        text = re.sub(r"^```(?:json)?\s*", "", text.strip())
        text = re.sub(r"\s*```$", "", text.strip())
        return json.loads(text)
    except Exception:
        # Try to extract JSON block
        m = re.search(r'\{.*\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
        return None


# ─────────────────────────────────────────────────────────────────────────────
# 5. Format a pillar as Markdown
# ─────────────────────────────────────────────────────────────────────────────
PILLAR_META = {
    "Form":     ("what the system IS",    "costs TIME   (endurance — resisting decay)"),
    "Position": ("where the system IS",   "costs SPACE  (resistance — resisting displacement)"),
    "Action":   ("what the system DOES",  "costs ENERGY (expenditure — change leaves entropy)"),
}

def format_pillar_md(
    pillar: str,
    principles: list[dict],
    system_name: str,
    model_used: str,
    prices_commentary: dict,
    theory: str,
    date: str,
) -> str:
    meta_what, meta_price = PILLAR_META[pillar]
    commentary = prices_commentary.get(pillar, "")
    lines = [
        f"# {pillar} Principles — {system_name}",
        f"*Generated by 3_pillars_constructor.py · {model_used} · {date}*",
        "",
        f"> **{pillar}** = {meta_what} · stability {meta_price}",
        "",
        f"**System theory:** {theory}",
        "",
        f"**Price of {pillar}:** {commentary}",
        "",
        "---",
        "",
    ]
    for i, p in enumerate(principles, 1):
        name = p.get("name", f"Principle {i}")
        desc = p.get("description", "")
        lines.append(f"{i}. **{name}** — {desc}")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# 6. Preview the principles in terminal
# ─────────────────────────────────────────────────────────────────────────────
def preview_principles(data: dict, system_name: str):
    W = 72
    print("\n" + "═"*W)
    print(f"  GENERATED PRINCIPLES — {system_name}")
    print("═"*W)
    if data.get("theory"):
        print(f"\n  Theory: {data['theory']}")
    for pillar in ["Form", "Position", "Action"]:
        meta_what, meta_price = PILLAR_META[pillar]
        print(f"\n  ── {pillar.upper()} ({meta_what} · {meta_price}) ──")
        for i, p in enumerate(data.get(pillar, []), 1):
            name = p.get("name", "?")
            desc = p.get("description", "")
            wrapped = textwrap.fill(desc, width=62, subsequent_indent=" " * 6)
            print(f"    {i:2}. {name}")
            print(f"       {wrapped}")
    pcom = data.get("prices_commentary", {})
    if pcom:
        print(f"\n  ── PRICE COMMENTARY ──")
        for k, v in pcom.items():
            print(f"  {k}: {v}")
    print("\n" + "═"*W)


# ─────────────────────────────────────────────────────────────────────────────
# 7. Save principles to disk
# ─────────────────────────────────────────────────────────────────────────────
def save_principles(
    data: dict,
    domain: str,
    system_name: str,
    model_used: str,
    date: str,
    force: bool = False,
) -> Path:
    domain_dir = PRINCIPLES_DIR / domain
    domain_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    for pillar in ["Form", "Position", "Action"]:
        principles = data.get(pillar, [])
        if not principles:
            print(f"  WARNING: No {pillar} principles in response, skipping.")
            continue
        md = format_pillar_md(
            pillar, principles, system_name,
            model_used, data.get("prices_commentary", {}),
            data.get("theory", ""), date,
        )
        outpath = domain_dir / f"{pillar}.md"
        if outpath.exists() and not force:
            answer = input(f"\n  {outpath.name} already exists. Overwrite? [y/N] ").strip().lower()
            if answer != "y":
                print(f"  Skipped {outpath.name}")
                continue
        outpath.write_text(md, encoding="utf-8")
        print(f"  Saved: {outpath}")
        saved.append(outpath)
    return domain_dir


# ─────────────────────────────────────────────────────────────────────────────
# 8. Interactive wizard
# ─────────────────────────────────────────────────────────────────────────────
def interactive_wizard() -> tuple[str, int, str]:
    print("\n" + "━"*60)
    print("  U-MODEL · 3 PILLARS CONSTRUCTOR")
    print("  Form / Position / Action — at a bearable price")
    print("━"*60)
    print("""
  This tool generates domain-specific stability principles
  for ANY system using top-tier AI (Opus / Kimi / Gemini).

  Examples of systems:
    • A physical object   ("A Glass of Water", "The Eiffel Tower")
    • A biological entity ("Human Heart", "A Forest")
    • A social structure  ("A Marriage", "NATO")
    • An organization     ("United Nations", "Tesla")
    • An abstract system  ("Democracy", "The Internet", "Language")
""")
    system_name = input("  What system are we evaluating? > ").strip()
    if not system_name:
        print("ERROR: System name required.", file=sys.stderr)
        sys.exit(1)

    n_str = input(f"  How many principles per pillar? [15] > ").strip()
    n = int(n_str) if n_str.isdigit() else 15

    default_domain = re.sub(r'[^\w]', '_', system_name.lower()).strip('_')
    dom_str = input(f"  Domain name for saving principles? [{default_domain}] > ").strip()
    domain = dom_str if dom_str else default_domain

    return system_name, n, domain


# ─────────────────────────────────────────────────────────────────────────────
# 9. Main
# ─────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description="3_pillars_constructor — generate Form/Position/Action principles for any system"
    )
    ap.add_argument("--system",  help='System to generate principles for (e.g. "A Glass of Water")')
    ap.add_argument("--n",       type=int, default=15, help="Principles per pillar (default: 15)")
    ap.add_argument("--domain",  help='Domain folder name for saving (default: sanitized system name)')
    ap.add_argument("--model",   help='Override architect model ID')
    ap.add_argument("--timeout", type=int, default=120, help="Timeout per model call (seconds)")
    ap.add_argument("--yes",     action="store_true", help="Skip confirmation prompts")
    ap.add_argument(
        "--context",
        metavar="FILE",
        default=None,
        help="Override path to domain context file (default: context/{domain}/general.md). "
             "Context is injected into the construction prompt to ground principle generation."
    )
    args = ap.parse_args()

    if not OR_KEY:
        print("ERROR: OPENROUTER_API_KEY not found. Set it in .github/.env", file=sys.stderr)
        sys.exit(1)

    # ── Input
    if args.system:
        system_name = args.system
        n           = args.n
        domain      = args.domain or re.sub(r'[^\w]', '_', system_name.lower()).strip('_')
    else:
        system_name, n, domain = interactive_wizard()

    date = datetime.now().strftime("%B %d, %Y")

    print(f"\n  System:  {system_name}")
    print(f"  Pillars: Form / Position / Action")
    print(f"  Count:   {n} principles each  ({n*3} total)")
    print(f"  Domain:  {domain}  →  principles/{domain}/")

    # ── Architect selection
    if args.model:
        architects = [args.model]
    else:
        print(f"\n  Checking architect availability on OpenRouter...")
        architects = get_available_architects()
        print(f"  Available: {', '.join(architects[:3])}{'...' if len(architects) > 3 else ''}")

    # ── Build prompt
    print(f"\n  Building construction prompt...")
    context_text = load_context(domain, override_file=args.context)
    ctx_src = (args.context or str(CONTEXT_DIR / domain / "general.md"))
    if context_text:
        print(f"  Context loaded: {ctx_src}  ({len(context_text):,} chars)")
    else:
        print(f"  Context: none  (tip: create context/{domain}/general.md for grounded principles)")
    prompt = build_construction_prompt(system_name, n, context_text=context_text)
    print(f"  Prompt: {len(prompt):,} chars")

    # ── Try architect models until one works
    raw_text = None
    model_used = None
    print(f"\n  Calling architect(s)...\n")
    for mid in architects:
        raw_text = call_architect(prompt, mid, timeout=args.timeout)
        if raw_text:
            model_used = mid
            break
        time.sleep(2)

    if not raw_text:
        print("ERROR: All architect models failed. Check API key and connectivity.", file=sys.stderr)
        sys.exit(1)

    # ── Parse
    print(f"\n  Parsing response...")
    data = parse_response(raw_text)
    if not data:
        print("ERROR: Could not parse JSON from response.", file=sys.stderr)
        print("Raw response snippet:", raw_text[:500])
        sys.exit(1)

    # Validate
    for pillar in ["Form", "Position", "Action"]:
        count = len(data.get(pillar, []))
        print(f"  {pillar:10}: {count} principles")
        if count == 0:
            print(f"  WARNING: {pillar} returned 0 principles — model may have failed.")

    # ── Preview
    preview_principles(data, system_name)

    # ── Confirm & save
    if not args.yes:
        answer = input(f"\n  Save to principles/{domain}/ ? [Y/n] > ").strip().lower()
        if answer == "n":
            print("  Aborted — nothing saved.")
            sys.exit(0)

    print(f"\n  Saving...")
    domain_dir = save_principles(data, domain, system_name, model_used, date, force=args.yes)

    # ── Done
    print(f"""
  ✓ DONE
  ─────────────────────────────────────────────────────────
  Principles saved to: {domain_dir}

  Now you can evaluate this system with 50 AI models:

    python System_Stability_Score.py "{system_name}" --domain {domain} --models 20 --save

  The AI jury will score each principle (0-100) and compute:
    U = ∛(Form × Position × Action)
    If U ≥ 0.618 → STABLE ✓
  ─────────────────────────────────────────────────────────
""")


if __name__ == "__main__":
    main()
