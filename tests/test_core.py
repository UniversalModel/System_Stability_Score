#!/usr/bin/env python3
"""
tests/test_core.py — Unit tests for System_Stability_Score ecosystem.

Run: python -m pytest tests/test_core.py -v

Covers:
  - compute_si() from gsi_multi_domain.py
  - _parse() from System_Stability_Score.py
  - _clamp_score() from System_Stability_Score.py
  - war_index computation from war_incompatibility_index.py
  - estimate_cost() from sss_llm_adapter.py
  - TriadicScheduler.step() from gsi_multi_domain.py
"""

import json
import math
import sys
from pathlib import Path

# Ensure project root is on path
_HERE = Path(__file__).parent.parent
sys.path.insert(0, str(_HERE))


# ── Test: compute_si (SSS formulas) ─────────────────────────────────────────
class TestComputeSI:
    def test_perfect_system(self):
        from gsi_multi_domain import compute_si
        r = compute_si(1.0, 1.0, 1.0)
        assert r["U"] == 1.0
        assert r["delta"] == 0.0
        assert r["SI"] == 1.0

    def test_collapsed_pillar(self):
        from gsi_multi_domain import compute_si
        r = compute_si(1.0, 1.0, 0.001)
        assert r["SI"] < 0.01  # near-zero when one pillar collapses

    def test_balanced_mid(self):
        from gsi_multi_domain import compute_si
        r = compute_si(0.5, 0.5, 0.5)
        assert 0.0 < r["U"] < 1.0
        assert 0.0 < r["SI"] < r["U"]  # delta penalty

    def test_clamping(self):
        from gsi_multi_domain import compute_si
        r = compute_si(0.0, 0.5, 0.5)  # 0 gets clamped to 0.001
        assert r["U"] > 0

    def test_golden_ratio_threshold(self):
        from gsi_multi_domain import compute_si
        # At F=P=A=0.618, SI should be >= 0.618 (delta=0)
        r = compute_si(0.618, 0.618, 0.618)
        assert r["SI"] >= 0.6


# ── Test: _parse (JSON repair) ───────────────────────────────────────────────
class TestParse:
    def test_clean_json(self):
        from System_Stability_Score import _parse
        result = _parse('{"Form": [{"score": 50}]}')
        assert result is not None
        assert result["Form"][0]["score"] == 50

    def test_markdown_wrapped(self):
        from System_Stability_Score import _parse
        result = _parse('```json\n{"Form": []}\n```')
        assert result is not None

    def test_trailing_comma(self):
        from System_Stability_Score import _parse
        result = _parse('{"Form": [{"score": 50,},]}')
        assert result is not None

    def test_garbage_returns_none(self):
        from System_Stability_Score import _parse
        assert _parse("not json at all") is None

    def test_extract_json_from_text(self):
        from System_Stability_Score import _parse
        text = 'Here is the result: {"Form": [{"score": 75}]} and some extra text'
        result = _parse(text)
        assert result is not None


# ── Test: _clamp_score ───────────────────────────────────────────────────────
class TestClampScore:
    def test_normal(self):
        from System_Stability_Score import _clamp_score
        v, susp = _clamp_score(50)
        assert v == 50 and not susp

    def test_negative(self):
        from System_Stability_Score import _clamp_score
        v, susp = _clamp_score(-10)
        assert v == 0 and susp

    def test_over_100(self):
        from System_Stability_Score import _clamp_score
        v, susp = _clamp_score(999)
        assert v == 100 and susp

    def test_non_numeric(self):
        from System_Stability_Score import _clamp_score
        v, susp = _clamp_score("abc")
        assert v == 50.0 and susp


# ── Test: war_index ──────────────────────────────────────────────────────────
class TestWarIndex:
    def test_identical_systems(self):
        from war_incompatibility_index import compute_indices
        sys_a = {"name": "A", "form": 0.8, "position": 0.7, "action": 0.6}
        sys_b = {"name": "B", "form": 0.8, "position": 0.7, "action": 0.6}
        r = compute_indices(sys_a, sys_b)
        assert r["pairwise"]["incompatibility"] < 0.01

    def test_opposite_systems(self):
        from war_incompatibility_index import compute_indices
        sys_a = {"name": "A", "form": 1.0, "position": 1.0, "action": 1.0}
        sys_b = {"name": "B", "form": 0.0, "position": 0.0, "action": 0.0}
        r = compute_indices(sys_a, sys_b)
        assert r["pairwise"]["war_index"] > 0.5

    def test_accepts_percentages(self):
        from war_incompatibility_index import compute_indices
        sys_a = {"name": "A", "form": 80, "position": 70, "action": 60}
        sys_b = {"name": "B", "form": 50, "position": 40, "action": 30}
        r = compute_indices(sys_a, sys_b)
        assert 0 <= r["pairwise"]["war_index"] <= 1.0


# ── Test: estimate_cost ──────────────────────────────────────────────────────
class TestEstimateCost:
    def test_known_model(self):
        from sss_llm_adapter import estimate_cost
        cost = estimate_cost("openai/gpt-4o-mini", 1000, max_tokens=100)
        assert cost > 0

    def test_unknown_model(self):
        from sss_llm_adapter import estimate_cost
        cost = estimate_cost("unknown/model", 1000)
        assert cost == 0.0

    def test_batch_cost(self):
        from sss_llm_adapter import estimate_batch_cost
        models = ["openai/gpt-4o-mini", "openai/gpt-4o"]
        cost = estimate_batch_cost(models, 2000)
        assert cost > 0


# ── Test: TriadicScheduler ───────────────────────────────────────────────────
class TestScheduler:
    def test_step_improves_si(self):
        from gsi_multi_domain import TriadicScheduler, Domain
        d = Domain(
            name="Test",
            actions=[("a1", 0.5), ("a2", 0.6)],
            forms=[("f1", 0.5), ("f2", 0.6)],
            positions=[("p1", 0.5), ("p2", 0.6)],
        )
        import random
        random.seed(42)
        sched = TriadicScheduler(d)
        si_before = max(s.SI for s in sched.population)
        sched.step(top_k=4)
        si_after = max(s.SI for s in sched.population)
        assert si_after >= si_before * 0.95  # should not degrade much

    def test_population_cap(self):
        from gsi_multi_domain import TriadicScheduler, Domain, MAX_POPULATION_SIZE
        d = Domain(
            name="Test",
            actions=[("a1", 0.5)],
            forms=[("f1", 0.5)],
            positions=[("p1", 0.5)],
        )
        sched = TriadicScheduler(d)
        for _ in range(100):
            sched.step(top_k=2)
        assert len(sched.population) <= MAX_POPULATION_SIZE


# ── Test: TriadicBudget ─────────────────────────────────────────────────────
class TestBudget:
    def test_exhausted(self):
        from gsi_runtime import TriadicBudget
        b = TriadicBudget(T_max=1, S_max=1, E_max=1)
        assert not b.exhausted
        b.charge(1, 1, 1)
        assert b.exhausted

    def test_serialization(self):
        from gsi_runtime import TriadicBudget
        b = TriadicBudget(T_max=10, S_max=20, E_max=30)
        b.charge(1, 2, 3)
        d = b.to_dict()
        b2 = TriadicBudget.from_dict(d)
        assert b2.T_used == b.T_used
        assert b2.exhausted == b.exhausted
