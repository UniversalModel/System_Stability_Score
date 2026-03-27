# ========================================================
# GSI-RTD Mini Prototype v2 — Email Marketing Example
# ========================================================
# Author:    Petar Nikolov (with AI assistance)
# Date:      27 March 2026
# Based on:  APPENDIX_GSI-RTD v.28 §1.1 (AD-RTD), §7 (SSS), §20 (Scheduler)
# Repo:      https://github.com/UniversalModel/System_Stability_Score
# DOI:       https://doi.org/10.17605/OSF.IO/74XGR
#
# WHAT THIS DEMONSTRATES:
# ─────────────────────────────────────────────────────────
# The GSI-RTD method decomposes any problem into three triadic axes:
#
#   Action   — What can be done? (6 actions)
#   Form     — What structure carries the action? (6 forms)
#   Position — In what context? (4 positions)
#
#   Total candidate systems = 6 × 6 × 4 = 144 agents
#
# Each "system" is a unique (Form_i, Position_j, Action_k) triple.
# The Stability Index (SI) is computed via the System Stability Score (SSS).
# Non-compensatory rule: a zero in ANY pillar collapses the entire system.
# The Triadic Scheduler selects the top-priority agents each generation.
# The Learning Law improves scores over 5 generations.
#
# RESULT: Only the most stable systems survive — that is the intelligence output.
# ========================================================

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import product
import os

print("=" * 60)
print("🚀 GSI-RTD Mini Prototype v2 — Email Marketing Simulation")
print("   144 agents → AD-RTD + SSS + Triadic Scheduler")
print("=" * 60)
print()

# ─────────────────────────────────────────────────────────
# 1. TRIADIC AXES — Action-Driven Decomposition (AD-RTD)
#    Order: Action → Form → Position  (§1.1)
# ─────────────────────────────────────────────────────────
actions = [
    "Send email",
    "Post on forums",
    "Fill online media forms",
    "Send letters by post",
    "Meet key people in person",
    "Pay for advertising",
]

forms = [
    "Ready-made template",
    "Personalized report",
    "Infographic",
    "Video pitch",
    "HTML email",
    "PDF attachment",
]

positions = [
    "By geographic location",
    "By workplace / company",
    "By hierarchy (CEO / Editor)",
    "By thematic interest",
]

# Generate all 144 candidate systems: (action_i, form_j, position_k)
candidates = list(product(range(len(actions)), range(len(forms)), range(len(positions))))
print(f"✅ Generated {len(candidates)} candidate systems ({len(actions)}×{len(forms)}×{len(positions)})")
print()
print("Each system = (Form_i @ Position_j performing Action_k)")
print("Example: 'HTML email' @ 'By hierarchy (CEO/Editor)' performing 'Send email'")
print()

# ─────────────────────────────────────────────────────────
# 2. SYSTEM STABILITY SCORE (SSS) — §7
#    U = ∛(F × P × A)
#    δ = imbalance ratio
#    SI = U / (1 + δ²)
#    NON-COMPENSATORY: min(F,P,A) ≤ ε → SI = 0 (COLLAPSE)
# ─────────────────────────────────────────────────────────
def compute_sss(f, p, a, eps=0.01):
    """
    Compute the Stability Index (SI) for a triadic system (F, P, A).

    Non-compensatory rule: if any pillar is at or near zero, the system collapses.
    This mirrors the GSI-RTD invariant: a zero in any dimension = total failure.
    """
    if min(f, p, a) <= eps:
        return 0.0  # COLLAPSE — non-compensatory rule
    U = (f * p * a) ** (1.0 / 3.0)        # geometric mean
    delta = (max(f, p, a) - min(f, p, a)) / (max(f, p, a) + eps)  # imbalance
    SI = U / (1 + delta ** 2)             # penalise imbalance
    return SI

# ─────────────────────────────────────────────────────────
# 3. SIMULATION — 5 generations, budget = 20 agents/gen
# ─────────────────────────────────────────────────────────
np.random.seed(42)
n = len(candidates)

# Initial random scores for each pillar of each candidate system
f_scores = np.random.uniform(0.4, 0.95, n)
p_scores = np.random.uniform(0.4, 0.95, n)
a_scores = np.random.uniform(0.4, 0.95, n)

generations = 5
budget = 20    # agents deployed per generation (§20 Scheduler)

results = []
all_gen_sis = []

print(f"{'─'*60}")
print(f"{'Gen':>4}  {'Predicted SI':>14}  {'Real SI':>10}  {'Best system'}")
print(f"{'─'*60}")

for gen in range(1, generations + 1):
    # Compute SI for all candidates
    sis = [compute_sss(f_scores[i], p_scores[i], a_scores[i]) for i in range(n)]
    all_gen_sis.append(sis[:])

    # Triadic Scheduler: priority = SI / cost  (§20)
    costs = [0.1 + (i % n) / n * 0.8 for i in range(n)]
    priorities = [sis[i] / (costs[i] + 0.01) for i in range(n)]
    top_idx = np.argsort(priorities)[-budget:]

    # Simulate real-world execution (with environmental noise)
    real_sis = [
        compute_sss(f_scores[i], p_scores[i], a_scores[i])
        * max(0.0, 0.97 + np.random.normal(0, 0.04))
        for i in top_idx
    ]

    avg_pred = float(np.mean([sis[i] for i in top_idx]))
    avg_real = float(np.mean(real_sis))
    best_i = top_idx[int(np.argmax([sis[i] for i in top_idx]))]
    best_label = (
        f"{actions[candidates[best_i][0]][:18]:18s} | "
        f"{forms[candidates[best_i][1]][:16]:16s} | "
        f"{positions[candidates[best_i][2]][:22]}"
    )

    results.append({
        "Generation": gen,
        "Predicted_SI": round(avg_pred, 4),
        "Real_SI": round(avg_real, 4),
        "Best_Action": actions[candidates[best_i][0]],
        "Best_Form": forms[candidates[best_i][1]],
        "Best_Position": positions[candidates[best_i][2]],
    })

    print(f"  {gen:2d}   Pred={avg_pred:.3f}   Real={avg_real:.3f}   {best_label}")

    # Learning Law (§26): reinforce the best-performing agents
    for i in top_idx:
        f_scores[i] = min(0.98, f_scores[i] + 0.12)
        p_scores[i] = min(0.98, p_scores[i] + 0.12)
        a_scores[i] = min(0.98, a_scores[i] + 0.12)

print(f"{'─'*60}")

# ─────────────────────────────────────────────────────────
# 4. FINAL WINNER — the most stable triadic system
# ─────────────────────────────────────────────────────────
final_sis = [compute_sss(f_scores[i], p_scores[i], a_scores[i]) for i in range(n)]
best = int(np.argmax(final_sis))

print()
print("🏆 MOST STABLE SYSTEM (final generation)")
print(f"   SI        = {final_sis[best]:.4f}")
print(f"   Action    = {actions[candidates[best][0]]}")
print(f"   Form      = {forms[candidates[best][1]]}")
print(f"   Position  = {positions[candidates[best][2]]}")
print()
print("   → This is the intelligence output of the GSI-RTD process.")
print("   → Millions of real-world problems can be solved this way.")

# ─────────────────────────────────────────────────────────
# 5. TRIAGE TABLE — High / Mid / Low SI  (§1.1 Phase 6)
# ─────────────────────────────────────────────────────────
theta_stable   = 0.618   # golden ratio threshold
theta_critical = 0.380

high = sum(1 for s in final_sis if s >= theta_stable)
mid  = sum(1 for s in final_sis if theta_critical <= s < theta_stable)
low  = sum(1 for s in final_sis if s < theta_critical)

print()
print("📊 TRIAGE (final generation):")
print(f"   High SI (≥{theta_stable})  — Exploit/Transfer : {high:3d} systems")
print(f"   Mid  SI ({theta_critical}–{theta_stable}) — Optimise        : {mid:3d} systems")
print(f"   Low  SI (<{theta_critical})  — Redesign/Reject : {low:3d} systems")

# ─────────────────────────────────────────────────────────
# 6. SAVE RESULTS
# ─────────────────────────────────────────────────────────
out_dir = os.path.dirname(os.path.abspath(__file__))

df_results = pd.DataFrame(results)
csv_path = os.path.join(out_dir, "gsi_rtd_email_marketing_results.csv")
df_results.to_csv(csv_path, index=False)

# All-systems triage snapshot (final gen)
all_systems = [
    {
        "Action": actions[candidates[i][0]],
        "Form": forms[candidates[i][1]],
        "Position": positions[candidates[i][2]],
        "SI": round(final_sis[i], 4),
        "Triage": (
            "High" if final_sis[i] >= theta_stable
            else "Mid" if final_sis[i] >= theta_critical
            else "Low"
        ),
    }
    for i in range(n)
]
df_all = pd.DataFrame(all_systems).sort_values("SI", ascending=False)
all_csv_path = os.path.join(out_dir, "gsi_rtd_email_marketing_all_systems.csv")
df_all.to_csv(all_csv_path, index=False)

# ─────────────────────────────────────────────────────────
# 7. PLOT
# ─────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# — Left: SI evolution over generations
gens  = [r["Generation"]    for r in results]
pred  = [r["Predicted_SI"]  for r in results]
real_ = [r["Real_SI"]       for r in results]

axes[0].axhline(theta_stable,   color="green",  linestyle="--", alpha=0.5, label=f"θ_stable={theta_stable}")
axes[0].axhline(theta_critical, color="orange", linestyle="--", alpha=0.5, label=f"θ_critical={theta_critical}")
axes[0].plot(gens, pred,  "o--", color="#3A6BC8", linewidth=2, markersize=7, label="Predicted SI")
axes[0].plot(gens, real_, "s-",  color="#E07B2A", linewidth=2, markersize=7, label="Real SI (environment)")
axes[0].fill_between(gens, pred, real_, alpha=0.08, color="gray")
axes[0].set_title("GSI-RTD Mini Prototype v2\nEmail Marketing — 144 Agents", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Generation")
axes[0].set_ylabel("Stability Index (SI)")
axes[0].set_ylim(0, 1.05)
axes[0].grid(True, alpha=0.25)
axes[0].legend(fontsize=9)

# — Right: Final SI distribution (histogram)
axes[1].hist(final_sis, bins=20, color="#6B3A8A", alpha=0.75, edgecolor="white")
axes[1].axvline(theta_stable,   color="green",  linestyle="--", linewidth=1.5, label=f"θ_stable={theta_stable}")
axes[1].axvline(theta_critical, color="orange", linestyle="--", linewidth=1.5, label=f"θ_critical={theta_critical}")
axes[1].set_title("Final SI Distribution\n(all 144 candidate systems)", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Stability Index (SI)")
axes[1].set_ylabel("Count")
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.25)

# Triage annotation
axes[1].text(0.96, 0.95, f"High: {high}\nMid:  {mid}\nLow:  {low}",
             transform=axes[1].transAxes, ha="right", va="top",
             fontsize=10, bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

plt.tight_layout()
png_path = os.path.join(out_dir, "gsi_rtd_email_marketing_v2.png")
plt.savefig(png_path, dpi=200)
plt.close()

print()
print("✅ Saved:")
print(f"   {png_path}")
print(f"   {csv_path}")
print(f"   {all_csv_path}")
print()
print("=" * 60)
print("  GSI-RTD: Intelligence = structured elimination of instability.")
print("  The survivors ARE the solution.")
print("=" * 60)
