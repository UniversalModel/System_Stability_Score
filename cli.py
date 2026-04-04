#!/usr/bin/env python3
"""
cli.py — Unified CLI entry point for System_Stability_Score ecosystem.

Usage:
  python cli.py sss "United Nations" --models 20 --save
  python cli.py gsi --generations 10 --use-llm
  python cli.py construct --system "A Glass of Water" --n 15
  python cli.py war --a-name USA --b-name RUS --simulate 10
  python cli.py incompat --a-form 0.8 --a-position 0.7 --a-action 0.6 --b-form 0.5 --b-position 0.4 --b-action 0.3

Author: U-Theory v26 / U-Model.org
"""
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="System_Stability_Score — Unified CLI (U-Model v26)",
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # ── sss: System Stability Score ──────────────────────────────────────────
    p_sss = sub.add_parser("sss", help="Run System Stability Score evaluation")
    p_sss.add_argument("entity", help="System to evaluate")
    p_sss.add_argument("--domain", default="universal")
    p_sss.add_argument("--models", type=int, default=10)
    p_sss.add_argument("--timeout", type=int, default=90)
    p_sss.add_argument("--save", action="store_true")
    p_sss.add_argument("--subject", default=None)
    p_sss.add_argument("--subject-label", default=None)
    p_sss.add_argument("--context", default=None)

    # ── gsi: GSI-RTD Runtime ─────────────────────────────────────────────────
    p_gsi = sub.add_parser("gsi", help="Run GSI-RTD multi-domain runtime")
    p_gsi.add_argument("--generations", type=int, default=10)
    p_gsi.add_argument("--top-k", type=int, default=20)
    p_gsi.add_argument("--jury-k", type=int, default=5)
    p_gsi.add_argument("--use-llm", action="store_true")
    p_gsi.add_argument("--verbose", action="store_true")
    p_gsi.add_argument("--model", default="openai/gpt-4o-mini")

    # ── construct: 3 Pillars Constructor ─────────────────────────────────────
    p_con = sub.add_parser("construct", help="Generate Form/Position/Action principles")
    p_con.add_argument("--system", required=True)
    p_con.add_argument("--n", type=int, default=15)
    p_con.add_argument("--domain", default=None)
    p_con.add_argument("--model", default=None)
    p_con.add_argument("--timeout", type=int, default=120)
    p_con.add_argument("--yes", action="store_true")
    p_con.add_argument("--context", default=None)
    p_con.add_argument("--lang", default="en")

    # ── war: War Duality Engine ──────────────────────────────────────────────
    p_war = sub.add_parser("war", help="War duality analysis")
    p_war.add_argument("--propose", action="store_true")
    p_war.add_argument("--a-name", default="System A")
    p_war.add_argument("--b-name", default="System B")
    p_war.add_argument("--json", default="")
    p_war.add_argument("--out", default="")
    p_war.add_argument("--simulate", type=int, default=0)
    p_war.add_argument("--estimate", default="")

    # ── incompat: War Incompatibility Index ──────────────────────────────────
    p_inc = sub.add_parser("incompat", help="War incompatibility index")
    p_inc.add_argument("--json", default="")
    p_inc.add_argument("--a-name", default="System A")
    p_inc.add_argument("--a-form", type=float, default=None)
    p_inc.add_argument("--a-position", type=float, default=None)
    p_inc.add_argument("--a-action", type=float, default=None)
    p_inc.add_argument("--b-name", default="System B")
    p_inc.add_argument("--b-form", type=float, default=None)
    p_inc.add_argument("--b-position", type=float, default=None)
    p_inc.add_argument("--b-action", type=float, default=None)
    p_inc.add_argument("--out", default="")
    p_inc.add_argument("--multi", default="")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "sss":
        from System_Stability_Score import main as sss_main
        sys.argv = ["System_Stability_Score.py", args.entity,
                     "--domain", args.domain,
                     "--models", str(args.models),
                     "--timeout", str(args.timeout)]
        if args.save:
            sys.argv.append("--save")
        if args.subject:
            sys.argv.extend(["--subject", args.subject])
        if args.subject_label:
            sys.argv.extend(["--subject-label", args.subject_label])
        if args.context:
            sys.argv.extend(["--context", args.context])
        sss_main()

    elif args.command == "gsi":
        from gsi_runtime import main as gsi_main
        sys.argv = ["gsi_runtime.py",
                     "--generations", str(args.generations),
                     "--top-k", str(args.top_k),
                     "--jury-k", str(args.jury_k),
                     "--model", args.model]
        if args.use_llm:
            sys.argv.append("--use-llm")
        if args.verbose:
            sys.argv.append("--verbose")
        gsi_main()

    elif args.command == "construct":
        from three_pillars_constructor import main as con_main
        sys.argv = ["3_pillars_constructor.py",
                     "--system", args.system,
                     "--n", str(args.n),
                     "--timeout", str(args.timeout),
                     "--lang", args.lang]
        if args.domain:
            sys.argv.extend(["--domain", args.domain])
        if args.model:
            sys.argv.extend(["--model", args.model])
        if args.yes:
            sys.argv.append("--yes")
        if args.context:
            sys.argv.extend(["--context", args.context])
        con_main()

    elif args.command == "war":
        from war_duality_engine import main as war_main
        sys.argv = ["war_duality_engine.py"]
        if args.propose:
            sys.argv.append("--propose")
        if args.a_name:
            sys.argv.extend(["--a-name", args.a_name])
        if args.b_name:
            sys.argv.extend(["--b-name", args.b_name])
        if args.json:
            sys.argv.extend(["--json", args.json])
        if args.out:
            sys.argv.extend(["--out", args.out])
        if args.simulate > 0:
            sys.argv.extend(["--simulate", str(args.simulate)])
        if args.estimate:
            sys.argv.extend(["--estimate", args.estimate])
        war_main()

    elif args.command == "incompat":
        from war_incompatibility_index import main as inc_main
        sys.argv = ["war_incompatibility_index.py"]
        if args.json:
            sys.argv.extend(["--json", args.json])
        if args.a_name:
            sys.argv.extend(["--a-name", args.a_name])
        if args.a_form is not None:
            sys.argv.extend(["--a-form", str(args.a_form)])
        if args.a_position is not None:
            sys.argv.extend(["--a-position", str(args.a_position)])
        if args.a_action is not None:
            sys.argv.extend(["--a-action", str(args.a_action)])
        if args.b_name:
            sys.argv.extend(["--b-name", args.b_name])
        if args.b_form is not None:
            sys.argv.extend(["--b-form", str(args.b_form)])
        if args.b_position is not None:
            sys.argv.extend(["--b-position", str(args.b_position)])
        if args.b_action is not None:
            sys.argv.extend(["--b-action", str(args.b_action)])
        if args.out:
            sys.argv.extend(["--out", args.out])
        if args.multi:
            sys.argv.extend(["--multi", args.multi])
        inc_main()


if __name__ == "__main__":
    main()
