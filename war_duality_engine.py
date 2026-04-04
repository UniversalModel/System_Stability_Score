#!/usr/bin/env python3
"""war_duality_engine.py

Dual-system war model for U-Theory/LGP:
1) Constructor scaffold proposes key Form/Position/Action parameters per side.
2) Analyzer computes duality: each parameter stabilizes its own system while exporting
   entropy to the opponent triad.
"""

import argparse
import json
from pathlib import Path

PILLARS = ("form", "position", "action")


def _to_unit(value: float) -> float:
    if value > 1.0:
        value = value / 100.0
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


def _geom3(a: float, b: float, c: float) -> float:
    return (a * b * c) ** (1.0 / 3.0)


def _combine_entropy(values) -> float:
    """Combine multiple entropy exports as probabilistic union: 1-prod(1-e_i)."""
    product = 1.0
    for v in values:
        product *= (1.0 - _to_unit(float(v)))
    return 1.0 - product


def _default_params(side: str):
    """Constructor scaffold inspired by APPENDIX_WAR + LGP (crack/shelf/bump)."""
    return [
        {
            "id": f"{side}_F1",
            "pillar": "form",
            "name": "Identity Cohesion",
            "stability": 0.72,
            "export_entropy": {"form": 0.35, "position": 0.12, "action": 0.10},
        },
        {
            "id": f"{side}_F2",
            "pillar": "form",
            "name": "Logistics Integrity",
            "stability": 0.68,
            "export_entropy": {"form": 0.20, "position": 0.16, "action": 0.25},
        },
        {
            "id": f"{side}_P1",
            "pillar": "position",
            "name": "Terrain and Corridor Control",
            "stability": 0.66,
            "export_entropy": {"form": 0.08, "position": 0.38, "action": 0.18},
        },
        {
            "id": f"{side}_P2",
            "pillar": "position",
            "name": "Alliance and Resource Shelf",
            "stability": 0.64,
            "export_entropy": {"form": 0.10, "position": 0.34, "action": 0.14},
        },
        {
            "id": f"{side}_A1",
            "pillar": "action",
            "name": "Mobilization Tempo",
            "stability": 0.70,
            "export_entropy": {"form": 0.14, "position": 0.15, "action": 0.42},
        },
        {
            "id": f"{side}_A2",
            "pillar": "action",
            "name": "Command-Loop Precision",
            "stability": 0.67,
            "export_entropy": {"form": 0.12, "position": 0.17, "action": 0.36},
        },
    ]


def propose_constructor_output(name_a: str, name_b: str) -> dict:
    return {
        "system_a": {"name": name_a, "parameters": _default_params("A")},
        "system_b": {"name": name_b, "parameters": _default_params("B")},
        "notes": "Edit stability/export_entropy per parameter with your conflict data.",
    }


def _pillar_base(params) -> dict:
    result = {}
    for pillar in PILLARS:
        values = [_to_unit(p["stability"]) for p in params if p.get("pillar") == pillar]
        if not values:
            result[pillar] = 0.5
        elif len(values) == 1:
            result[pillar] = values[0]
        else:
            product = 1.0
            for v in values:
                product *= v
            result[pillar] = product ** (1.0 / len(values))
    return result


def _incoming_entropy(from_params) -> dict:
    result = {}
    for pillar in PILLARS:
        exports = [_to_unit(p.get("export_entropy", {}).get(pillar, 0.0)) for p in from_params]
        result[pillar] = _combine_entropy(exports)
    return result


def _effective(base: dict, incoming: dict) -> dict:
    return {p: max(0.0, min(1.0, base[p] * (1.0 - incoming[p]))) for p in PILLARS}


def _duality_rows(system_name: str, params) -> list:
    rows = []
    for p in params:
        own = _to_unit(p.get("stability", 0.0))
        exp = p.get("export_entropy", {})
        export_total = (exp.get("form", 0.0) + exp.get("position", 0.0) + exp.get("action", 0.0)) / 3.0
        rows.append(
            {
                "system": system_name,
                "id": p.get("id", ""),
                "name": p.get("name", ""),
                "pillar": p.get("pillar", ""),
                "own_stability": _to_unit(own),
                "export_total": _to_unit(export_total),
                "duality_strength": _to_unit(own) * _to_unit(export_total),
            }
        )
    return rows


def analyze_duality(payload: dict) -> dict:
    a = payload["system_a"]
    b = payload["system_b"]
    pa = a["parameters"]
    pb = b["parameters"]

    base_a = _pillar_base(pa)
    base_b = _pillar_base(pb)

    incoming_a = _incoming_entropy(pb)
    incoming_b = _incoming_entropy(pa)

    eff_a = _effective(base_a, incoming_a)
    eff_b = _effective(base_b, incoming_b)

    u_a = _geom3(eff_a["form"], eff_a["position"], eff_a["action"])
    u_b = _geom3(eff_b["form"], eff_b["position"], eff_b["action"])

    incompatibility = (abs(base_a["form"] - base_b["form"]) + abs(base_a["position"] - base_b["position"]) + abs(base_a["action"] - base_b["action"])) / 3.0
    entropy_exchange = (_combine_entropy(incoming_a.values()) + _combine_entropy(incoming_b.values())) / 2.0
    joint_fragility = ((1.0 - u_a) + (1.0 - u_b)) / 2.0

    war_index = 0.45 * incompatibility + 0.35 * entropy_exchange + 0.20 * joint_fragility
    war_index = max(0.0, min(1.0, war_index))

    if war_index >= 0.80:
        band = "CRITICAL"
    elif war_index >= 0.62:
        band = "HIGH"
    elif war_index >= 0.45:
        band = "ELEVATED"
    elif war_index >= 0.30:
        band = "MODERATE"
    else:
        band = "LOW"

    return {
        "system_a": {
            "name": a.get("name", "System A"),
            "base": base_a,
            "incoming_entropy": incoming_a,
            "effective": eff_a,
            "u_score_under_conflict": u_a,
        },
        "system_b": {
            "name": b.get("name", "System B"),
            "base": base_b,
            "incoming_entropy": incoming_b,
            "effective": eff_b,
            "u_score_under_conflict": u_b,
        },
        "pair": {
            "incompatibility": incompatibility,
            "entropy_exchange": entropy_exchange,
            "joint_fragility": joint_fragility,
            "war_index": war_index,
            "band": band,
        },
        "duality_rows": _duality_rows(a.get("name", "System A"), pa) + _duality_rows(b.get("name", "System B"), pb),
        "formula": {
            "effective_pillar": "U_Xk_eff = U_Xk_base * (1 - incoming_entropy_k)",
            "incoming_entropy": "E_k = 1 - product(1 - e_i_to_k)",
            "u_under_conflict": "U_X = cbrt(U_XF_eff * U_XP_eff * U_XA_eff)",
            "war_index": "W = 0.45*Incompatibility + 0.35*EntropyExchange + 0.20*JointFragility",
        },
    }


def _print_summary(result: dict) -> None:
    sa = result["system_a"]
    sb = result["system_b"]
    p = result["pair"]

    print("\n=== WAR DUALITY ENGINE ===")
    print(f"A: {sa['name']} | U_conflict={sa['u_score_under_conflict']:.3f}")
    print(f"B: {sb['name']} | U_conflict={sb['u_score_under_conflict']:.3f}")
    print(f"Incompatibility: {p['incompatibility']:.3f}")
    print(f"Entropy exchange: {p['entropy_exchange']:.3f}")
    print(f"Joint fragility:  {p['joint_fragility']:.3f}")
    print(f"WAR INDEX:        {p['war_index']:.3f} [{p['band']}]")


def _load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


# ── Patch 6.1: Time-series simulation ────────────────────────────────────────
def simulate_rounds(payload: dict, n_rounds: int = 10,
                    damage_rate: float = 0.05, repair_rate: float = 0.03,
                    seed: int | None = None) -> list[dict]:
    """
    Simulate N rounds of conflict with damage/repair dynamics.
    Each round: each side exports entropy to the other (damage),
    then repairs its own pillars slightly (repair).
    Returns list of per-round snapshots.
    """
    import random as _rng
    if seed is not None:
        _rng.seed(seed)

    a = payload["system_a"]
    b = payload["system_b"]
    pa = list(a["parameters"])  # deep copy via list()
    pb = list(b["parameters"])

    trajectory = []
    for rnd in range(1, n_rounds + 1):
        # Compute effective scores
        base_a = _pillar_base(pa)
        base_b = _pillar_base(pb)
        incoming_a = _incoming_entropy(pb)
        incoming_b = _incoming_entropy(pa)
        eff_a = _effective(base_a, incoming_a)
        eff_b = _effective(base_b, incoming_b)
        u_a = _geom3(eff_a["form"], eff_a["position"], eff_a["action"])
        u_b = _geom3(eff_b["form"], eff_b["position"], eff_b["action"])

        trajectory.append({
            "round": rnd,
            "u_a": round(u_a, 4),
            "u_b": round(u_b, 4),
            "eff_a": {k: round(v, 4) for k, v in eff_a.items()},
            "eff_b": {k: round(v, 4) for k, v in eff_b.items()},
        })

        # Apply damage: reduce stability by damage_rate + noise
        for p in pa + pb:
            p["stability"] = max(0.01, p["stability"] * (1 - damage_rate + _rng.uniform(-0.02, 0.02)))
            # Increase export entropy slightly (escalation)
            for pillar in PILLARS:
                if pillar in p.get("export_entropy", {}):
                    p["export_entropy"][pillar] = min(0.95, p["export_entropy"][pillar] * (1 + 0.02))

        # Apply repair: boost stability by repair_rate
        for p in pa + pb:
            p["stability"] = min(1.0, p["stability"] * (1 + repair_rate + _rng.uniform(-0.01, 0.01)))

    return trajectory


# ── Patch 6.2: LLM-powered parameter estimation ──────────────────────────────
def estimate_params(conflict_description: str, side_a: str = "Side A",
                    side_b: str = "Side B") -> dict:
    """
    Use LLM to estimate realistic stability/entropy parameters from a
    text description of a conflict. Falls back to defaults if no API key.
    """
    try:
        from sss_llm_adapter import api_generate, OPENROUTER_API_KEY
        if not OPENROUTER_API_KEY:
            return propose_constructor_output(side_a, side_b)
    except ImportError:
        return propose_constructor_output(side_a, side_b)

    prompt = f"""Given this conflict description:
"{conflict_description}"

Estimate stability (0-1) and export_entropy (0-1 per pillar) for each side.
Side A: {side_a}
Side B: {side_b}

For each side, provide 6 parameters (2 per pillar: Form, Position, Action):
- stability: how stable is this aspect (0=collapsed, 1=perfect)
- export_entropy: how much entropy this exports to opponent per pillar

Respond ONLY with valid JSON matching this structure:
{{
  "system_a": {{
    "name": "{side_a}",
    "parameters": [
      {{"id": "A_F1", "pillar": "form", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}},
      {{"id": "A_F2", "pillar": "form", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}},
      {{"id": "A_P1", "pillar": "position", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}},
      {{"id": "A_P2", "pillar": "position", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}},
      {{"id": "A_A1", "pillar": "action", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}},
      {{"id": "A_A2", "pillar": "action", "name": "...", "stability": 0.0, "export_entropy": {{"form": 0.0, "position": 0.0, "action": 0.0}}}}
    ]
  }},
  "system_b": {{
    "name": "{side_b}",
    "parameters": [same structure as system_a with B_ prefix]
  }}
}}"""

    result = api_generate("openrouter", prompt, model="openai/gpt-4o-mini",
                          max_tokens=2000, temperature=0.3)
    if result.success and result.text:
        try:
            text = result.text.strip()
            text = text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except json.JSONDecodeError:
            pass
    return propose_constructor_output(side_a, side_b)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dual war model: constructor scaffold + entropy-export analysis")
    parser.add_argument("--propose", action="store_true", help="Generate constructor scaffold JSON")
    parser.add_argument("--a-name", type=str, default="System A")
    parser.add_argument("--b-name", type=str, default="System B")
    parser.add_argument("--json", type=str, default="", help="Input constructor-output JSON")
    parser.add_argument("--out", type=str, default="", help="Output JSON file")
    parser.add_argument("--simulate", type=int, default=0, help="Run N rounds of time-series simulation (Patch 6.1)")
    parser.add_argument("--estimate", type=str, default="", help="LLM parameter estimation from conflict description (Patch 6.2)")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    # Patch 6.2: LLM parameter estimation
    if args.estimate:
        print(f"Estimating parameters from conflict description...")
        payload = estimate_params(args.estimate, args.a_name, args.b_name)
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8")
            print(f"Saved estimated scaffold: {args.out}")
        else:
            print(text)
        return

    if args.propose:
        payload = propose_constructor_output(args.a_name, args.b_name)
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8")
            print(f"Saved scaffold: {args.out}")
        else:
            print(text)
        return

    if not args.json:
        raise SystemExit("Use --propose, --estimate, or provide --json INPUT_FILE")

    payload = _load_json(args.json)

    # Patch 6.1: time-series simulation
    if args.simulate > 0:
        print(f"Simulating {args.simulate} rounds of conflict...")
        trajectory = simulate_rounds(payload, n_rounds=args.simulate)
        for snap in trajectory:
            print(f"  Round {snap['round']:2d}: U_A={snap['u_a']:.3f}  U_B={snap['u_b']:.3f}")
        if args.out:
            Path(args.out).write_text(
                json.dumps(trajectory, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Saved trajectory: {args.out}")
        return

    result = analyze_duality(payload)
    _print_summary(result)

    if args.out:
        Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved analysis: {args.out}")


if __name__ == "__main__":
    main()
