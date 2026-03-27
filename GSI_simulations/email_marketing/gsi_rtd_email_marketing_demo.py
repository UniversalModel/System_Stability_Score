# ========================================================
# GSI-RTD Mini Prototype v3 — Email Marketing Example
# ========================================================
# Author:    Petar Nikolov (with AI assistance)
# Date:      27 March 2026
# Based on:  APPENDIX_GSI-RTD v.28 §1.1 (AD-RTD), §7 (SSS), §20 (Scheduler)
# Repo:      https://github.com/UniversalModel/System_Stability_Score
# DOI:       https://doi.org/10.17605/OSF.IO/74XGR
#
# v3 IMPROVEMENTS (from peer review):
#   P1 fix  — Learning Law rate: 0.12 → 0.052 (prevents false saturation)
#   P3 fix  — Triadic cost model: ∛(C_energy × C_time × C_space) replaces
#              arbitrary index-based cost  (§1.1 Phase 7)
#   New [2] — Exploration Injection: ε=12%, decay=0.7 per generation (§1.1)
#   New [3] — Peak/Dip Analysis + ARMED State Machine (§1.1 Phase 0 IDO)
#   New [1] — Monte Carlo Sensitivity Analysis: N=200 runs, 95% CI
# ========================================================

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import product
import os

print("=" * 72)
print("  GSI-RTD Mini Prototype v3 — Email Marketing Simulation")
print("  144 agents | AD-RTD + SSS + Triadic Scheduler | Monte Carlo N=200")
print("=" * 72)
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
#
#    Canonical ontology (v26 invariant):
#      Form     ↔ Time   (the message carrier / representation)
#      Position ↔ Space  (the recipient context / targeting frame)
#      Action   ↔ Energy (the delivery intervention)
#
#    Operational enumeration order (AD-RTD §1.1): A → F → P
#    This is methodological only; it does NOT invert the ontology.
#
#    Canonical SSS formula (LGP/TAA/SSS):
#      U  = ∛(F × P × A)          geometric mean
#      δ  = (max − min) / (max + ε)  imbalance ratio
#      SI = U / (1 + δ)²           canonical penalty  ← v26 canon
#
#    NON-COMPENSATORY: min(F,P,A) ≤ ε → SI = 0 (COLLAPSE)
# ─────────────────────────────────────────────────────────
def compute_sss(f, p, a, eps=0.01):
    """
    Stability Index (SI) for a triadic system (F, P, A).
    Canonical formula: SI = ∛(F·P·A) / (1+δ)²
    Non-compensatory: collapse if any pillar ≤ eps.
    SSS-Guard: in production, flag if |predicted_SI − real_SI| > 0.06.
    """
    if min(f, p, a) <= eps:
        return 0.0
    U = (f * p * a) ** (1.0 / 3.0)
    delta = (max(f, p, a) - min(f, p, a)) / (max(f, p, a) + eps)
    return U / (1 + delta) ** 2


# ─────────────────────────────────────────────────────────
# 3. TRIADIC COST MODEL — §1.1 Phase 7  (P3 fix)
#    Cost = ∛(C_energy × C_time × C_space)
#    Non-compensatory: a zero cost component = trivially costless = unrealistic.
#    Values are domain estimates, normalized to [0, 1].
# ─────────────────────────────────────────────────────────
action_energy_cost = {
    "Send email":               0.10,
    "Post on forums":           0.15,
    "Fill online media forms":  0.20,
    "Send letters by post":     0.50,
    "Meet key people in person": 0.80,
    "Pay for advertising":      0.70,
}
form_time_cost = {
    "Ready-made template":   0.10,
    "Personalized report":   0.50,
    "Infographic":           0.40,
    "Video pitch":           0.60,
    "HTML email":            0.20,
    "PDF attachment":        0.15,
}
position_space_cost = {
    "By geographic location":       0.30,
    "By workplace / company":       0.25,
    "By hierarchy (CEO / Editor)":  0.40,
    "By thematic interest":         0.20,
}

def triadic_cost(action_idx, form_idx, position_idx):
    """Triadic cost: geometric mean of energy, time, space costs (§1.1 Phase 7)."""
    c_e = action_energy_cost[actions[action_idx]]
    c_t = form_time_cost[forms[form_idx]]
    c_s = position_space_cost[positions[position_idx]]
    return max((c_e * c_t * c_s) ** (1.0 / 3.0), 1e-6)


# ─────────────────────────────────────────────────────────
# 4. PEAK / DIP ANALYSIS + ARMED STATE MACHINE — §1.1 Phase 0 IDO
# ─────────────────────────────────────────────────────────
def detect_peaks_dips(si_history):
    """
    Detect local peaks and dips in an agent's SI trajectory.
    Dip at t:  si[t] < si[t-1] AND si[t] < si[t+1]
    Peak at t: si[t] > si[t-1] AND si[t] > si[t+1]
    """
    events = []
    for t in range(1, len(si_history) - 1):
        if si_history[t] < si_history[t-1] and si_history[t] < si_history[t+1]:
            events.append((t + 1, "DIP",  si_history[t]))
        elif si_history[t] > si_history[t-1] and si_history[t] > si_history[t+1]:
            events.append((t + 1, "PEAK", si_history[t]))
    return events


def armed_state_machine(si_history, min_recovery=0.05, max_armed_age=3):
    """
    ARMED State Machine (§1.1 Phase 0):
    Enters ARMED on confirmed bottom (descent → recovery).
    Triggers intervention when recovery ≥ min_recovery.
    Expires after max_armed_age generations without sufficient recovery.
    "Buy the dip" logic: invest in recovering agents, not still-falling ones.
    """
    interventions = []
    armed_at = armed_min_si = None
    for t in range(2, len(si_history)):
        was_falling = si_history[t-1] < si_history[t-2]
        now_rising  = si_history[t]   > si_history[t-1]
        if was_falling and now_rising and armed_at is None:
            armed_at, armed_min_si = t, si_history[t-1]
        if armed_at is not None:
            recovery = si_history[t] - armed_min_si
            if recovery >= min_recovery:
                interventions.append({
                    "gen": t + 1, "armed_at": armed_at + 1,
                    "min_si": round(armed_min_si, 3),
                    "current_si": round(si_history[t], 3),
                    "recovery": round(recovery, 3),
                })
                armed_at = None
            elif (t - armed_at) > max_armed_age:
                armed_at = None  # expired
    return interventions

# ─────────────────────────────────────────────────────────
# 5. SIMULATION — 5 generations, budget = 20 agents/gen
#    With: Exploration Injection (§1.1), Triadic Cost, SSS-Guard, Random Baseline
# ─────────────────────────────────────────────────────────
np.random.seed(42)
n = len(candidates)

f_scores = np.random.uniform(0.4, 0.95, n)
p_scores = np.random.uniform(0.4, 0.95, n)
a_scores = np.random.uniform(0.4, 0.95, n)

# Precompute triadic costs (fixed per domain, not per run)
costs = [triadic_cost(candidates[i][0], candidates[i][1], candidates[i][2])
         for i in range(n)]

generations    = 5
budget         = 20
learning_rate  = 0.052   # P1 fix: was 0.12 — reduced to prevent false saturation
epsilon_start  = 0.12    # Exploration injection (§1.1): 12% of budget
epsilon_decay  = 0.70    # Decays per generation → 8% → 6% → 4% → 3%
out_dir        = os.path.dirname(os.path.abspath(__file__))

results      = []
all_gen_sis  = []   # track SI history per generation (for Peak/Dip)
epsilon      = epsilon_start

print(f"{'─'*72}")
print(f"{'Gen':>4}  {'Pred':>7}  {'Triadic':>8}  {'Random':>7}  {'Advantage':>10}  {'Guard':>6}  {'Explore':>8}")
print(f"{'─'*72}")

for gen in range(1, generations + 1):
    sis = [compute_sss(f_scores[i], p_scores[i], a_scores[i]) for i in range(n)]
    all_gen_sis.append(sis[:])

    priorities = [sis[i] / (costs[i] + 1e-6) for i in range(n)]

    # Exploration Injection (§1.1 Anti-Bias Safeguard)
    n_explore = max(1, int(budget * epsilon))
    n_exploit = budget - n_explore
    exploit_idx  = list(np.argsort(priorities)[-n_exploit:])
    available    = [i for i in range(n) if i not in set(exploit_idx)]
    explore_idx  = list(np.random.choice(available, n_explore, replace=False))
    top_idx      = exploit_idx + explore_idx

    # Random Baseline — same budget, pure random (Gate 1 ablation, §6.1)
    random_idx = list(np.random.choice(n, budget, replace=False))

    # Execute with environmental noise (LGP-8/9)
    real_sis = [
        compute_sss(f_scores[i], p_scores[i], a_scores[i])
        * max(0.0, 0.97 + np.random.normal(0, 0.04))
        for i in top_idx
    ]
    random_real_sis = [
        compute_sss(f_scores[i], p_scores[i], a_scores[i])
        * max(0.0, 0.97 + np.random.normal(0, 0.04))
        for i in random_idx
    ]

    avg_pred   = float(np.mean([sis[i] for i in top_idx]))
    avg_real   = float(np.mean(real_sis))
    avg_random = float(np.mean(random_real_sis))
    advantage  = avg_real - avg_random

    # SSS-Guard (LGP-10 Pulse Monitor — §7.2)
    deviation = abs(avg_pred - avg_real)
    guard = "ALERT" if deviation > 0.06 else "OK"

    best_i = top_idx[int(np.argmax([sis[i] for i in top_idx]))]
    best_label = (
        f"{actions[candidates[best_i][0]][:18]:18s} | "
        f"{forms[candidates[best_i][1]][:16]:16s} | "
        f"{positions[candidates[best_i][2]][:20]}"
    )

    results.append({
        "Generation":         gen,
        "Predicted_SI":       round(avg_pred,   4),
        "Real_SI_Triadic":    round(avg_real,   4),
        "Real_SI_Random":     round(avg_random, 4),
        "Triadic_Advantage":  round(advantage,  4),
        "SSS_Guard":          guard,
        "Epsilon_Explore":    round(epsilon,    3),
        "Best_Action":        actions[candidates[best_i][0]],
        "Best_Form":          forms[candidates[best_i][1]],
        "Best_Position":      positions[candidates[best_i][2]],
    })

    print(f"  {gen:2d}  {avg_pred:.3f}  {avg_real:.3f}    {avg_random:.3f}   "
          f"{advantage:+.3f}    {guard:5s}  {n_explore}/{budget} (e={epsilon:.2f})")

    # Learning Law (§26) — reduced rate prevents false saturation (P1 fix)
    for i in top_idx:
        f_scores[i] = min(0.98, f_scores[i] + learning_rate)
        p_scores[i] = min(0.98, p_scores[i] + learning_rate)
        a_scores[i] = min(0.98, a_scores[i] + learning_rate)

    epsilon *= epsilon_decay  # exploration decays over time

print(f"{'─'*72}")

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
# 6. PEAK / DIP ANALYSIS — §1.1 Phase 0 IDO
# ─────────────────────────────────────────────────────────
agent_si_histories = np.array(all_gen_sis).T  # shape: (n_agents, n_generations)

print()
print("PEAK/DIP ANALYSIS (top exploited agents — IDO, §1.1 Phase 0):")
ido_found = 0
for agent_idx in exploit_idx[:10]:
    history = agent_si_histories[agent_idx].tolist()
    events  = detect_peaks_dips(history)
    armed   = armed_state_machine(history)
    if events or armed:
        label = (f"{actions[candidates[agent_idx][0]][:20]} | "
                 f"{forms[candidates[agent_idx][1]][:14]}")
        print(f"  Agent {agent_idx:3d} — {label}")
        for ev in events:
            print(f"    {ev[1]:4s} at gen {ev[0]}, SI={ev[2]:.3f}")
        for arm in armed:
            print(f"    ARMED intervention at gen {arm['gen']}, "
                  f"recovery={arm['recovery']:.3f}")
        ido_found += 1
if ido_found == 0:
    print("  (No peaks/dips detected in 5 generations — monotonic convergence.)")
    print("  Increase generations or add external perturbation to activate IDO.")

# ─────────────────────────────────────────────────────────
# 7. MONTE CARLO SENSITIVITY ANALYSIS — §35.5bis
#    N=200 independent runs, 95% confidence intervals
#    Validates statistical significance of Triadic advantage.
# ─────────────────────────────────────────────────────────
print()
print("MONTE CARLO SENSITIVITY ANALYSIS (N=200 runs, §35.5bis):")
N_RUNS = 200
mc_advantages = np.zeros((N_RUNS, generations))

for run in range(N_RUNS):
    np.random.seed(run * 7 + 13)
    mc_f = np.random.uniform(0.4, 0.95, n)
    mc_p = np.random.uniform(0.4, 0.95, n)
    mc_a = np.random.uniform(0.4, 0.95, n)
    mc_eps = epsilon_start

    for g in range(generations):
        mc_sis = [compute_sss(mc_f[i], mc_p[i], mc_a[i]) for i in range(n)]
        mc_prio = [mc_sis[i] / (costs[i] + 1e-6) for i in range(n)]

        n_exp = max(1, int(budget * mc_eps))
        n_expl = budget - n_exp
        mc_exploit = list(np.argsort(mc_prio)[-n_expl:])
        mc_avail   = [i for i in range(n) if i not in set(mc_exploit)]
        mc_explore = list(np.random.choice(mc_avail, n_exp, replace=False))
        mc_top     = mc_exploit + mc_explore
        mc_rand    = list(np.random.choice(n, budget, replace=False))

        tri_real = float(np.mean([
            compute_sss(mc_f[i], mc_p[i], mc_a[i]) * max(0.0, 0.97 + np.random.normal(0, 0.04))
            for i in mc_top
        ]))
        rnd_real = float(np.mean([
            compute_sss(mc_f[i], mc_p[i], mc_a[i]) * max(0.0, 0.97 + np.random.normal(0, 0.04))
            for i in mc_rand
        ]))
        mc_advantages[run, g] = tri_real - rnd_real

        for i in mc_top:
            mc_f[i] = min(0.98, mc_f[i] + learning_rate)
            mc_p[i] = min(0.98, mc_p[i] + learning_rate)
            mc_a[i] = min(0.98, mc_a[i] + learning_rate)
        mc_eps *= epsilon_decay

mean_adv = mc_advantages.mean(axis=0)
std_adv  = mc_advantages.std(axis=0)
print(f"  {'Gen':>4}  {'Mean Advantage':>16}  {'Std':>8}  {'95% CI':>24}  {'Sig?':>6}")
mc_results = []
for g in range(generations):
    ci_lo = mean_adv[g] - 1.96 * std_adv[g]
    ci_hi = mean_adv[g] + 1.96 * std_adv[g]
    sig = "YES" if ci_lo > 0 else "NO"
    print(f"  {g+1:4d}  {mean_adv[g]:+.4f}           {std_adv[g]:.4f}  [{ci_lo:+.4f}, {ci_hi:+.4f}]  {sig:>6}")
    mc_results.append({
        "Generation": g + 1,
        "Mean_Advantage": round(float(mean_adv[g]), 4),
        "Std": round(float(std_adv[g]), 4),
        "CI_Low_95": round(float(ci_lo), 4),
        "CI_High_95": round(float(ci_hi), 4),
        "Significant": sig,
    })

# Save Monte Carlo results
mc_csv_path = os.path.join(out_dir, "gsi_rtd_monte_carlo_results.csv")
pd.DataFrame(mc_results).to_csv(mc_csv_path, index=False)

# ─────────────────────────────────────────────────────────
# 8. SAVE MAIN RESULTS
# ─────────────────────────────────────────────────────────

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
# 9. PLOT — 3 panels
# ─────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# — Left: SI evolution over generations
gens  = [r["Generation"]        for r in results]
pred  = [r["Predicted_SI"]      for r in results]
real_ = [r["Real_SI_Triadic"]   for r in results]
rand_ = [r["Real_SI_Random"]    for r in results]

axes[0].axhline(theta_stable,   color="green",  linestyle="--", alpha=0.5, label=f"θ_stable={theta_stable}")
axes[0].axhline(theta_critical, color="orange", linestyle="--", alpha=0.5, label=f"θ_critical={theta_critical}")
axes[0].plot(gens, pred,  "o--", color="#3A6BC8", linewidth=2, markersize=7, label="Predicted SI (Triadic)")
axes[0].plot(gens, real_, "s-",  color="#2E9E4F", linewidth=2, markersize=7, label="Real SI — Triadic")
axes[0].plot(gens, rand_, "x:",  color="#C0392B", linewidth=1.5, markersize=7, label="Real SI — Random")
axes[0].fill_between(gens, real_, rand_, alpha=0.12, color="#2E9E4F", label="Triadic advantage")
axes[0].set_title("GSI-RTD Mini Prototype v3\nTriadic vs. Random Baseline (seed=42)", fontsize=11, fontweight="bold")
axes[0].set_xlabel("Generation")
axes[0].set_ylabel("Stability Index (SI)")
axes[0].set_ylim(0, 1.05)
axes[0].grid(True, alpha=0.25)
axes[0].legend(fontsize=9)

# — Middle: Final SI distribution (histogram)
axes[1].hist(final_sis, bins=20, color="#6B3A8A", alpha=0.75, edgecolor="white")
axes[1].axvline(theta_stable,   color="green",  linestyle="--", linewidth=1.5, label=f"θ_stable={theta_stable}")
axes[1].axvline(theta_critical, color="orange", linestyle="--", linewidth=1.5, label=f"θ_critical={theta_critical}")
axes[1].set_title("Final SI Distribution\n(all 144 candidate systems)", fontsize=11, fontweight="bold")
axes[1].set_xlabel("Stability Index (SI)")
axes[1].set_ylabel("Count")
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.25)
axes[1].text(0.96, 0.95, f"High: {high}\nMid:  {mid}\nLow:  {low}",
             transform=axes[1].transAxes, ha="right", va="top",
             fontsize=10, bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

# — Right: Monte Carlo CI chart  (§35.5bis)
mc_gens  = [r["Generation"]    for r in mc_results]
mc_means = [r["Mean_Advantage"] for r in mc_results]
mc_ci_lo = [r["CI_Low_95"]     for r in mc_results]
mc_ci_hi = [r["CI_High_95"]    for r in mc_results]

axes[2].bar(mc_gens, mc_means, color="#3A6BC8", alpha=0.7, label="Mean advantage")
axes[2].errorbar(mc_gens, mc_means,
                 yerr=[[m - lo for m, lo in zip(mc_means, mc_ci_lo)],
                       [hi - m for m, hi in zip(mc_means, mc_ci_hi)]],
                 fmt="none", color="black", capsize=5, linewidth=1.5)
axes[2].axhline(0, color="red", linestyle="--", linewidth=1, label="No advantage (H0)")
axes[2].set_title(f"Monte Carlo Validation (N=200)\nTriadic Advantage ± 95% CI", fontsize=11, fontweight="bold")
axes[2].set_xlabel("Generation")
axes[2].set_ylabel("Triadic SI − Random SI")
axes[2].legend(fontsize=9)
axes[2].grid(True, alpha=0.25)

plt.tight_layout()
png_path = os.path.join(out_dir, "gsi_rtd_email_marketing_v2.png")
plt.savefig(png_path, dpi=200)
plt.close()

print()
print("Saved:")
print(f"   {png_path}")
print(f"   {csv_path}")
print(f"   {all_csv_path}")
print(f"   {mc_csv_path}")
print()
print("=" * 72)
print("  GSI-RTD: Intelligence = structured elimination of instability.")
print("  The survivors ARE the solution.")
print("=" * 72)
