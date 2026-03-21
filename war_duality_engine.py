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


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dual war model: constructor scaffold + entropy-export analysis")
    parser.add_argument("--propose", action="store_true", help="Generate constructor scaffold JSON")
    parser.add_argument("--a-name", type=str, default="System A")
    parser.add_argument("--b-name", type=str, default="System B")
    parser.add_argument("--json", type=str, default="", help="Input constructor-output JSON")
    parser.add_argument("--out", type=str, default="", help="Output JSON file")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

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
        raise SystemExit("Use --propose or provide --json INPUT_FILE")

    result = analyze_duality(_load_json(args.json))
    _print_summary(result)

    if args.out:
        Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved analysis: {args.out}")


if __name__ == "__main__":
    main()
