"""
GSI-RTD Medical Domain Simulation — Full-Scale Real Ontology Demo
=================================================================
Domain  : Clinical Medicine (Real CSV Ontology)
Axes    : F=Symptoms (1052) | P=Medical Specialties (35) | A=Lab Tests (3361)
Space   : 1052 × 35 × 3361 = 123,752,020 candidate triadic systems
Method  : Triadic Scheduler vs. Random Baseline (N=200 Monte Carlo runs)
Author  : Petar Nikolov / U-Theory v26
"""

import os
import csv
import math
import random
import hashlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# 0. PATHS
# ─────────────────────────────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
MEDICAL_DIR = r"C:\Users\PC\OneDrive\Documents\u-score\v.26\Medical"

# ─────────────────────────────────────────────────────────────────────────────
# 1. LOAD REAL MEDICAL ONTOLOGY FROM CSV FILES
# ─────────────────────────────────────────────────────────────────────────────

def load_csv_column(filepath):
    """Load a single-column CSV into a deduplicated list of non-empty strings."""
    items = []
    seen = set()
    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            for row in csv.reader(f):
                if row:
                    val = row[0].strip()
                    if val and val not in seen:
                        seen.add(val)
                        items.append(val)
    except FileNotFoundError:
        print(f"WARNING: file not found: {filepath}")
    return items


def load_ontology():
    symptoms    = load_csv_column(os.path.join(MEDICAL_DIR, "Symptoms --- .csv"))
    tests_raw   = load_csv_column(os.path.join(MEDICAL_DIR, "Tests - Clinical Laboratory.csv"))
    specialties = load_csv_column(os.path.join(MEDICAL_DIR, "Medical specialties.csv"))

    # Normalise test names (strip "..... abnormal" suffix)
    tests = list(dict.fromkeys(
        t.replace(" ..... abnormal", "").replace(".....abnormal", "").strip()
        for t in tests_raw
    ))
    tests = [t for t in tests if t]

    return symptoms, specialties, tests


# ─────────────────────────────────────────────────────────────────────────────
# 2. SSS FORMULA (v26 canonical — non-compensatory)
# ─────────────────────────────────────────────────────────────────────────────
KILL_THRESHOLD = 0.30
THETA_STABLE   = 0.618
THETA_CRITICAL = 0.380
ALPHA          = 0.052   # learning rate (consistent across all domains)


def sss(f, p, a):
    """System Stability Score: SI = U / (1 + δ)²"""
    if min(f, p, a) < KILL_THRESHOLD:
        return 0.0, 0.0, 0.0
    u     = (f * p * a) ** (1 / 3)
    hi    = max(f, p, a)
    lo    = min(f, p, a)
    delta = (hi - lo) / (hi + 0.01)
    si    = u / (1 + delta) ** 2
    return round(si, 6), round(u, 6), round(delta, 6)


# ─────────────────────────────────────────────────────────────────────────────
# 3. DETERMINISTIC PILLAR SCORES FROM ONTOLOGY NAMES
# ─────────────────────────────────────────────────────────────────────────────

def _hash_score(name: str, seed_int: int, lo=0.25, hi=0.95) -> float:
    """Map a name → deterministic float in [lo, hi] via SHA-256."""
    h   = hashlib.sha256(f"{seed_int}:{name}".encode()).hexdigest()
    raw = int(h[:8], 16) / 0xFFFFFFFF
    return round(lo + raw * (hi - lo), 4)


# Specialty P-scores: hand-crafted from real-world resource density
SPECIALTY_COVERAGE = {
    "Cardiology and Vascular Medicine": 0.88,
    "Oncology":                          0.85,
    "Surgery, General":                  0.84,
    "Emergency Medicine":                0.82,
    "Neurology":                         0.80,
    "Gastroenterology and Hepatology":   0.78,
    "Endocrinology and Metabolic Disorders": 0.76,
    "Pulmonary Medicine":                0.75,
    "Nephrology":                        0.74,
    "Infectious Diseases":               0.73,
    "Hematology":                        0.72,
    "Clinical Laboratory":               0.72,
    "Rheumatology":                      0.70,
    "Psychiatry":                        0.69,
    "Dermatology":                       0.68,
    "Surgery, Orthopedics":              0.67,
    "Surgery, Urology":                  0.66,
    "Ophthalmology":                     0.65,
    "Allergy and Immunology":            0.64,
    "Critical Care Medicine":            0.63,
    "Obstetrician / Gynecologist":       0.62,
    "Pediatrics and Adolescent Medicine": 0.61,
    "Surgery, Thoracic":                 0.60,
    "Surgery, Neurosurgery":             0.59,
    "Surgery, Vascular":                 0.58,
    "Surgery, ENT":                      0.57,
    "Geriatric Medicine":                0.55,
    "instrumental diagnostics and treatment": 0.55,
    "Genetics":                          0.52,
    "Nutrition":                         0.50,
    "Health Maintenance":                0.50,
    "Dental / Oral Care":                0.48,
    "Veterinary medicine":               0.45,
    "Other and More...":                 0.40,
}


def build_pillar_scores(symptoms, specialties, tests, seed=42):
    """
    Assign base pillar scores derived from ontology names.

    U-Theory v26 mapping:
      F (Form / Time)      = Symptom specificity
      P (Position / Space) = Specialty coverage / resource density
      A (Action / Energy)  = Test sensitivity / reliability
    """
    F = {s:  _hash_score(s, seed * 3)  for s in symptoms}
    P = {sp: SPECIALTY_COVERAGE.get(sp, _hash_score(sp, seed * 7, 0.35, 0.80))
         for sp in specialties}
    A = {t:  _hash_score(t, seed * 11) for t in tests}
    return F, P, A


# ─────────────────────────────────────────────────────────────────────────────
# 4. TRIADIC SYSTEM — ONE CANDIDATE
# ─────────────────────────────────────────────────────────────────────────────

class TriadicSystem:
    __slots__ = ("symptom", "specialty", "test", "f", "p", "a", "si", "u", "delta")

    def __init__(self, symptom, specialty, test, f, p, a):
        self.symptom   = symptom
        self.specialty = specialty
        self.test      = test
        self.f = f
        self.p = p
        self.a = a
        self.si, self.u, self.delta = sss(f, p, a)

    def recompute(self):
        self.si, self.u, self.delta = sss(self.f, self.p, self.a)

    def triadic_cost(self):
        """Geometric mean of axis effort costs (§1.1 Phase 7).
        Low current score → high effort to improve → higher cost."""
        c_f = max(0.01, 1.0 - self.f)   # symptom assessment effort
        c_p = max(0.01, 1.0 - self.p)   # specialty resource effort
        c_a = max(0.01, 1.0 - self.a)   # test execution effort
        return (c_f * c_p * c_a) ** (1 / 3)

    def weakest_pillar(self):
        d = {"F": self.f, "P": self.p, "A": self.a}
        return min(d, key=d.get)


# ─────────────────────────────────────────────────────────────────────────────
# 5. SIMULATION PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
POOL_SIZE  = 2_000   # systems sampled from the full space per run
GEN_BATCH  = 50      # systems evaluated per generation
N_GENS     = 5       # generations per run
N_RUNS     = 200     # Monte Carlo independent runs
TOP_K_FRAC = 0.40    # exploit fraction in triadic scheduler


# ─────────────────────────────────────────────────────────────────────────────
# 6. MEDICAL HARD GATES (non-compensatory)
# ─────────────────────────────────────────────────────────────────────────────

def passes_gates(sys_: TriadicSystem) -> bool:
    """
    G1 Safety:   no pillar below KILL_THRESHOLD (patient safety floor)
    G2 Clarity:  symptom specificity (F) >= 0.32
    G3 Reach:    specialty coverage (P) >= 0.38
    G4 Accuracy: test reliability (A) >= 0.35
    Non-compensatory: one failure => rejected.
    """
    return (sys_.f >= 0.32 and sys_.p >= 0.38 and sys_.a >= 0.35
            and min(sys_.f, sys_.p, sys_.a) >= KILL_THRESHOLD)


# ─────────────────────────────────────────────────────────────────────────────
# 7. TRIADIC SCHEDULER
# ─────────────────────────────────────────────────────────────────────────────

class TriadicScheduler:
    """
    Two-stage selector: exploit top-K by SI/cost + explore random remainder.
    Learning Law (§26): after selection, improve selected systems' weakest pillar.
    """

    def __init__(self):
        self.epsilon = 0.12    # exploration fraction (§1.1 anti-bias)
        self.eps_decay = 0.70  # decay per generation

    def priority(self, sys_: TriadicSystem) -> float:
        """Priority = SI / triadic_cost  (§1.1 Phase 7, mirroring email demo)."""
        return sys_.si / (sys_.triadic_cost() + 1e-6)

    def select(self, pool, batch, rng):
        """Exploit top-k by priority + explore random remainder."""
        pool.sort(key=self.priority, reverse=True)
        n_explore = max(1, int(batch * self.epsilon))
        n_exploit = batch - n_explore
        chosen    = pool[:n_exploit]
        rest      = pool[n_exploit:]
        if rest:
            chosen += rng.sample(rest, min(n_explore, len(rest)))
        self.epsilon *= self.eps_decay
        return chosen

    @staticmethod
    def learn(batch):
        """Learning Law (§26): improve weakest pillar of each selected system."""
        for sys_ in batch:
            wp = sys_.weakest_pillar()
            if wp == "F":
                sys_.f = min(0.98, sys_.f + ALPHA)
            elif wp == "P":
                sys_.p = min(0.98, sys_.p + ALPHA)
            else:
                sys_.a = min(0.98, sys_.a + ALPHA)
            sys_.recompute()


# ─────────────────────────────────────────────────────────────────────────────
# 8. SINGLE RUN
# ─────────────────────────────────────────────────────────────────────────────

def run_one(symptoms, specialties, tests, F, P, A, run_id):
    rng  = random.Random(run_id * 13 + 23)

    # Build a fresh mutable pool for this run (scores start from hash baseline)
    pool = []
    for _ in range(POOL_SIZE):
        s  = rng.choice(symptoms)
        sp = rng.choice(specialties)
        t  = rng.choice(tests)
        pool.append(TriadicSystem(s, sp, t, F[s], P[sp], A[t]))

    valid = [x for x in pool if passes_gates(x)]
    if len(valid) < GEN_BATCH * 2:
        return None

    sched  = TriadicScheduler()
    t_gens = []
    r_gens = []

    for _ in range(N_GENS):
        # Triadic: priority = SI / cost, then learn (improve weakest pillar)
        t_batch = sched.select(list(valid), GEN_BATCH, rng)
        TriadicScheduler.learn(t_batch)
        t_gens.append(float(np.mean([x.si for x in t_batch])))

        # Random baseline: uniform sample, no learning
        r_batch = rng.sample(valid, min(GEN_BATCH, len(valid)))
        r_gens.append(float(np.mean([x.si for x in r_batch])))

    return t_gens, r_gens


# ─────────────────────────────────────────────────────────────────────────────
# 9. MONTE CARLO
# ─────────────────────────────────────────────────────────────────────────────

def monte_carlo(symptoms, specialties, tests, F, P, A):
    t_all, r_all = [], []
    skipped = 0
    for run in range(N_RUNS):
        result = run_one(symptoms, specialties, tests, F, P, A, run)
        if result is None:
            skipped += 1
            continue
        t_all.append(result[0])
        r_all.append(result[1])
    if skipped:
        print(f"  (skipped {skipped}/{N_RUNS} runs — insufficient valid systems in pool)")
    return np.array(t_all, dtype=float), np.array(r_all, dtype=float)


# ─────────────────────────────────────────────────────────────────────────────
# 10. PLOT
# ─────────────────────────────────────────────────────────────────────────────
TC = "#1A6B8A"
RC = "#C0392B"


def make_plot(t_arr, r_arr, total_space):
    n     = t_arr.shape[0]
    gens  = np.arange(1, N_GENS + 1)
    t_m   = t_arr.mean(0);  r_m   = r_arr.mean(0)
    t_ci  = 1.96 * t_arr.std(0, ddof=1) / math.sqrt(n)
    r_ci  = 1.96 * r_arr.std(0, ddof=1) / math.sqrt(n)
    diffs = t_arr[:, -1] - r_arr[:, -1]
    adv   = float(diffs.mean())
    ci    = float(1.96 * diffs.std(ddof=1) / math.sqrt(n))
    pct   = float((diffs > 0).mean() * 100)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    fig.patch.set_facecolor("#F8F9FB")

    # Left — SI learning curves
    ax = axes[0]
    ax.set_facecolor("#FFFFFF")
    ax.plot(gens, t_m, color=TC, lw=2.5, marker="o", markersize=7,
            label="Triadic Scheduler (AD-RTD)", zorder=3)
    ax.fill_between(gens, t_m - t_ci, t_m + t_ci, color=TC, alpha=0.15)
    ax.plot(gens, r_m, color=RC, lw=2.5, marker="s", markersize=7,
            linestyle="--", label="Random Baseline", zorder=3)
    ax.fill_between(gens, r_m - r_ci, r_m + r_ci, color=RC, alpha=0.15)
    ax.axhline(THETA_STABLE,   color="#2ECC71", lw=1.5, ls=":",
               label=f"θ_stable ({THETA_STABLE})")
    ax.axhline(THETA_CRITICAL, color="#E67E22", lw=1.5, ls=":",
               label=f"θ_critical ({THETA_CRITICAL})")
    ax.set_xlabel("Generation", fontsize=12)
    ax.set_ylabel("Mean System Stability Index (SI)", fontsize=12)
    ax.set_title(
        f"Triadic vs. Random — Real Clinical Ontology\n"
        f"{total_space:,} candidate systems | N={n} MC runs",
        fontsize=11, fontweight="bold"
    )
    ax.legend(fontsize=9, framealpha=0.9)
    ax.set_ylim(0, 1.0)
    ax.set_xticks(gens)
    ax.grid(True, alpha=0.35, linestyle="--")

    # Right — advantage distribution
    ax2 = axes[1]
    ax2.set_facecolor("#FFFFFF")
    ax2.hist(diffs, bins=30, color=TC, edgecolor="white", alpha=0.85)
    ax2.axvline(0,   color=RC, lw=2.0, ls="--", label="Zero line")
    ax2.axvline(adv, color=TC, lw=2.5,
                label=f"Mean Δ = {adv:+.3f}")
    ax2.axvspan(adv - ci, adv + ci, color=TC, alpha=0.15,
                label=f"95% CI [{adv-ci:+.3f}, {adv+ci:+.3f}]")
    ax2.set_xlabel("Final-Gen ΔSI (Triadic − Random)", fontsize=12)
    ax2.set_ylabel("Count (runs)", fontsize=12)
    ax2.set_title(
        f"Advantage Distribution — Gen {N_GENS}\n"
        f"Triadic beats Random in {pct:.1f}% of runs",
        fontsize=11, fontweight="bold"
    )
    ax2.legend(fontsize=9, framealpha=0.9)
    ax2.grid(True, alpha=0.35, linestyle="--")

    plt.tight_layout(pad=2.0)
    out = os.path.join(SCRIPT_DIR, "gsi_rtd_medical_results.png")
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    return out, adv, ci, pct


# ─────────────────────────────────────────────────────────────────────────────
# 11. MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("  GSI-RTD  Medical Domain — Full-Scale Real Ontology Simulation")
    print("  U-Theory v26 | Petar Nikolov")
    print("=" * 70)

    print("\n[1/5] Loading real medical ontology CSV files...")
    symptoms, specialties, tests = load_ontology()

    total_space = len(symptoms) * len(specialties) * len(tests)

    print(f"      Symptoms   (F / Form):       {len(symptoms):>6,d}")
    print(f"      Specialties(P / Position):   {len(specialties):>6,d}")
    print(f"      Lab Tests  (A / Action):     {len(tests):>6,d}")
    print()
    print(f"      ╔═══════════════════════════════════════════════════════╗")
    print(f"      ║  FULL TRIADIC SPACE: {total_space:>13,d} candidate systems ║")
    print(f"      ╚═══════════════════════════════════════════════════════╝")
    print(f"      {len(symptoms)} × {len(specialties)} × {len(tests)} = {total_space:,}")

    print("\n[2/5] Building deterministic pillar scores from ontology names...")
    F, P, A = build_pillar_scores(symptoms, specialties, tests)
    print(f"      F (symptom specificity):    "
          f"min={min(F.values()):.3f}  max={max(F.values()):.3f}  "
          f"mean={sum(F.values())/len(F):.3f}")
    print(f"      P (specialty coverage):     "
          f"min={min(P.values()):.3f}  max={max(P.values()):.3f}  "
          f"mean={sum(P.values())/len(P):.3f}")
    print(f"      A (test reliability):       "
          f"min={min(A.values()):.3f}  max={max(A.values()):.3f}  "
          f"mean={sum(A.values())/len(A):.3f}")

    print("\n      Medical Hard Gates (non-compensatory):")
    print("        G1 Safety:   all pillars ≥ 0.30")
    print("        G2 Clarity:  symptom specificity (F) ≥ 0.32")
    print("        G3 Reach:    specialty coverage   (P) ≥ 0.38")
    print("        G4 Accuracy: test reliability     (A) ≥ 0.35")

    print(f"\n[3/5] Monte Carlo ({N_RUNS} runs × {N_GENS} gens × {GEN_BATCH} sys/gen)...")
    print(f"      Pool per run: {POOL_SIZE:,} randomly sampled from {total_space:,}")
    print(f"      Learning rate α = {ALPHA}")

    t_arr, r_arr = monte_carlo(symptoms, specialties, tests, F, P, A)

    print("\n[4/5] Statistics:")
    gens = np.arange(1, N_GENS + 1)
    t_m  = t_arr.mean(0)
    r_m  = r_arr.mean(0)
    diffs = t_arr[:, -1] - r_arr[:, -1]
    adv  = float(diffs.mean())
    ci   = float(1.96 * diffs.std(ddof=1) / math.sqrt(t_arr.shape[0]))
    pct  = float((diffs > 0).mean() * 100)

    print(f"\n  ┌─ RESULTS (n={t_arr.shape[0]} valid runs) ─────────────────────────┐")
    for g in range(N_GENS):
        print(f"  │  Gen {g+1}: Triadic={t_m[g]:.4f}  Random={r_m[g]:.4f}"
              f"  Δ={t_m[g]-r_m[g]:+.4f}")
    print(f"  ├───────────────────────────────────────────────────────────┤")
    print(f"  │  Final Δ = {adv:+.3f}  95% CI [{adv-ci:+.3f}, {adv+ci:+.3f}]")
    print(f"  │  Triadic > Random in {pct:.1f}% of {t_arr.shape[0]} runs")
    print(f"  │  Triadic space: {total_space:,} systems")
    print(f"  └───────────────────────────────────────────────────────────┘")

    print("\n[5/5] Generating plot...")
    plot_path, adv, ci, pct = make_plot(t_arr, r_arr, total_space)
    print(f"      Saved → {plot_path}")

    print("\n  TRIADIC INTERPRETATION (U-Theory v26):")
    print("  ─────────────────────────────────────────────────────────────")
    print("  Each candidate system = (Symptom, Specialty, Test):")
    print("    F (Form   / Time)     = Symptom specificity")
    print("    P (Position / Space)  = Specialty resource coverage")
    print("    A (Action  / Energy)  = Lab test sensitivity/reliability")
    print("  The Triadic Scheduler targets the WEAKEST pillar per cycle,")
    print("  mirroring clinical triage: address the most critical gap first.")
    print(f"  Real-world ontology yields {total_space:,} candidate systems —")
    print("  demonstrating the combinatorial scale of GSI-RTD in practice.")
    print("\n  Done.")


if __name__ == "__main__":
    main()
