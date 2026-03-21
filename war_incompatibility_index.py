#!/usr/bin/env python3
"""war_incompatibility_index.py

Practical calculator for conflict risk between two potentially incompatible systems
using U-Theory triadic coordinates (Form, Position, Action).

Input scale:
- Accepts either [0, 1] floats or [0, 100] percentages.

Core outputs:
- U_A, U_B: internal triadic stability of each system
- Incompatibility: triadic mismatch between the two systems
- Joint instability: average internal fragility
- War index: combined conflict potential
"""

import argparse
import json
from pathlib import Path


def _to_unit(value: float) -> float:
    """Normalize value to [0,1], accepting either [0,1] or [0,100]."""
    if value > 1.0:
        value = value / 100.0
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


def _geom3(x: float, y: float, z: float) -> float:
    return (x * y * z) ** (1.0 / 3.0)


def _normalize_system(system: dict, default_name: str) -> dict:
    return {
        "name": system.get("name", default_name),
        "form": _to_unit(float(system["form"])),
        "position": _to_unit(float(system["position"])),
        "action": _to_unit(float(system["action"])),
    }


def _war_band(war_index: float) -> str:
    if war_index >= 0.80:
        return "CRITICAL"
    if war_index >= 0.62:
        return "HIGH"
    if war_index >= 0.45:
        return "ELEVATED"
    if war_index >= 0.30:
        return "MODERATE"
    return "LOW"


def _build_system_result(system: dict, u_score: float) -> dict:
    return {
        "name": system["name"],
        "form": system["form"],
        "position": system["position"],
        "action": system["action"],
        "u_score": u_score,
        "instability": 1.0 - u_score,
    }


def _build_formula_block() -> dict:
    return {
        "u": "U = cbrt(Form * Position * Action)",
        "compatibility": "C = ( (1-|dF|)^wF * (1-|dP|)^wP * (1-|dA|)^wA )",
        "incompatibility": "I = 1 - C",
        "joint_instability": "J = ((1-U_A) + (1-U_B)) / 2",
        "war_index": "W = 0.60*I + 0.30*J + 0.10*(|dA|*(1-min(U_A,U_B)))",
    }


def _build_pairwise_result(a_sys: dict, b_sys: dict, u_a: float, u_b: float,
                           w_form: float, w_position: float, w_action: float) -> dict:
    d_form = abs(a_sys["form"] - b_sys["form"])
    d_position = abs(a_sys["position"] - b_sys["position"])
    d_action = abs(a_sys["action"] - b_sys["action"])

    triadic_compatibility = (
        ((1.0 - d_form) ** w_form)
        * ((1.0 - d_position) ** w_position)
        * ((1.0 - d_action) ** w_action)
    )
    incompatibility = 1.0 - triadic_compatibility
    joint_instability = 0.5 * ((1.0 - u_a) + (1.0 - u_b))
    escalation_pressure = d_action * (1.0 - min(u_a, u_b))

    war_index = (0.60 * incompatibility) + (0.30 * joint_instability) + (0.10 * escalation_pressure)
    war_index = max(0.0, min(1.0, war_index))

    return {
        "d_form": d_form,
        "d_position": d_position,
        "d_action": d_action,
        "triadic_compatibility": triadic_compatibility,
        "incompatibility": incompatibility,
        "joint_instability": joint_instability,
        "escalation_pressure": escalation_pressure,
        "war_index": war_index,
        "band": _war_band(war_index),
    }


def compute_indices(a: dict, b: dict, w_form=1 / 3, w_position=1 / 3, w_action=1 / 3) -> dict:
    """Compute compatibility, instability, and war index between systems A and B."""
    system_a = _normalize_system(a, "System A")
    system_b = _normalize_system(b, "System B")
    u_a = _geom3(system_a["form"], system_a["position"], system_a["action"])
    u_b = _geom3(system_b["form"], system_b["position"], system_b["action"])
    pairwise = _build_pairwise_result(system_a, system_b, u_a, u_b, w_form, w_position, w_action)

    return {
        "system_a": _build_system_result(system_a, u_a),
        "system_b": _build_system_result(system_b, u_b),
        "pairwise": pairwise,
        "formula": _build_formula_block(),
    }


def _print_human(result: dict) -> None:
    a = result["system_a"]
    b = result["system_b"]
    p = result["pairwise"]

    print("\n=== WAR INCOMPATIBILITY INDEX ===")
    print(f"A: {a['name']} | U={a['u_score']:.3f} | FPA=({a['form']:.2f},{a['position']:.2f},{a['action']:.2f})")
    print(f"B: {b['name']} | U={b['u_score']:.3f} | FPA=({b['form']:.2f},{b['position']:.2f},{b['action']:.2f})")

    print("\nPairwise gaps:")
    print(f"- dForm:     {p['d_form']:.3f}")
    print(f"- dPosition: {p['d_position']:.3f}")
    print(f"- dAction:   {p['d_action']:.3f}")

    print("\nIndices:")
    print(f"- Triadic compatibility: {p['triadic_compatibility']:.3f}")
    print(f"- Incompatibility:       {p['incompatibility']:.3f}")
    print(f"- Joint instability:     {p['joint_instability']:.3f}")
    print(f"- Escalation pressure:   {p['escalation_pressure']:.3f}")
    print(f"- WAR INDEX:             {p['war_index']:.3f}  [{p['band']}]")


def _load_from_json(path: str) -> tuple:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["system_a"], data["system_b"]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute war incompatibility and instability index between two systems")
    parser.add_argument("--json", type=str, default="", help="Path to JSON input file with system_a/system_b")

    parser.add_argument("--a-name", type=str, default="System A")
    parser.add_argument("--a-form", type=float, default=None)
    parser.add_argument("--a-position", type=float, default=None)
    parser.add_argument("--a-action", type=float, default=None)

    parser.add_argument("--b-name", type=str, default="System B")
    parser.add_argument("--b-form", type=float, default=None)
    parser.add_argument("--b-position", type=float, default=None)
    parser.add_argument("--b-action", type=float, default=None)

    parser.add_argument("--w-form", type=float, default=1 / 3)
    parser.add_argument("--w-position", type=float, default=1 / 3)
    parser.add_argument("--w-action", type=float, default=1 / 3)

    parser.add_argument("--out", type=str, default="", help="Optional output JSON path")
    return parser.parse_args()


def _systems_from_args(args: argparse.Namespace) -> tuple:
    if args.json:
        return _load_from_json(args.json)

    required = [
        args.a_form,
        args.a_position,
        args.a_action,
        args.b_form,
        args.b_position,
        args.b_action,
    ]
    if any(v is None for v in required):
        raise SystemExit("Provide either --json FILE or all --a-* and --b-* FPA values")

    system_a = {
        "name": args.a_name,
        "form": args.a_form,
        "position": args.a_position,
        "action": args.a_action,
    }
    system_b = {
        "name": args.b_name,
        "form": args.b_form,
        "position": args.b_position,
        "action": args.b_action,
    }
    return system_a, system_b


def main() -> None:
    args = _parse_args()
    system_a, system_b = _systems_from_args(args)

    result = compute_indices(
        system_a,
        system_b,
        w_form=args.w_form,
        w_position=args.w_position,
        w_action=args.w_action,
    )

    _print_human(result)

    if args.out:
        Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nSaved JSON report: {args.out}")


if __name__ == "__main__":
    main()
