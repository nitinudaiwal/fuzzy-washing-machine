"""
Fuzzy Logic System - Washing Machine Cycle Time
================================================
Author  : Nitin Udaiwal
Course  : Introduction to Intelligent Systems
Topic   : Fuzzy Logic System Design

Inputs  : Dirt Level (0-10), Load Size (0-10)
Output  : Cycle Time in minutes (0-60)

Fuzzy Sets:
  Dirt Level : Low, Medium, High
  Load Size  : Small, Medium, Large
  Cycle Time : Short, Medium, Long
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving figures

# ─────────────────────────────────────────────
# 1. DEFINE UNIVERSE OF DISCOURSE
# ─────────────────────────────────────────────
dirt_level = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt_level')
load_size   = ctrl.Antecedent(np.arange(0, 11, 1), 'load_size')
cycle_time  = ctrl.Consequent(np.arange(0, 61, 1), 'cycle_time')

# ─────────────────────────────────────────────
# 2. DEFINE FUZZY MEMBERSHIP FUNCTIONS
# ─────────────────────────────────────────────

# --- Dirt Level ---
dirt_level['low']    = fuzz.trimf(dirt_level.universe, [0, 0, 5])
dirt_level['medium'] = fuzz.trimf(dirt_level.universe, [2, 5, 8])
dirt_level['high']   = fuzz.trimf(dirt_level.universe, [5, 10, 10])

# --- Load Size ---
load_size['small']   = fuzz.trimf(load_size.universe, [0, 0, 5])
load_size['medium']  = fuzz.trimf(load_size.universe, [2, 5, 8])
load_size['large']   = fuzz.trimf(load_size.universe, [5, 10, 10])

# --- Cycle Time (minutes) ---
cycle_time['short']  = fuzz.trimf(cycle_time.universe, [0, 0, 30])
cycle_time['medium'] = fuzz.trimf(cycle_time.universe, [15, 30, 45])
cycle_time['long']   = fuzz.trimf(cycle_time.universe, [30, 60, 60])

# ─────────────────────────────────────────────
# 3. DEFINE FUZZY RULES (minimum 6 required)
# ─────────────────────────────────────────────
rule1 = ctrl.Rule(dirt_level['low']    & load_size['small'],  cycle_time['short'])
rule2 = ctrl.Rule(dirt_level['low']    & load_size['medium'], cycle_time['short'])
rule3 = ctrl.Rule(dirt_level['low']    & load_size['large'],  cycle_time['medium'])
rule4 = ctrl.Rule(dirt_level['medium'] & load_size['small'],  cycle_time['short'])
rule5 = ctrl.Rule(dirt_level['medium'] & load_size['medium'], cycle_time['medium'])
rule6 = ctrl.Rule(dirt_level['medium'] & load_size['large'],  cycle_time['medium'])
rule7 = ctrl.Rule(dirt_level['high']   & load_size['small'],  cycle_time['medium'])
rule8 = ctrl.Rule(dirt_level['high']   & load_size['medium'], cycle_time['long'])
rule9 = ctrl.Rule(dirt_level['high']   & load_size['large'],  cycle_time['long'])

# ─────────────────────────────────────────────
# 4. BUILD CONTROL SYSTEM & SIMULATION
# ─────────────────────────────────────────────
washing_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5,
    rule6, rule7, rule8, rule9
])
washing_sim = ctrl.ControlSystemSimulation(washing_ctrl)

# ─────────────────────────────────────────────
# 5. PLOT MEMBERSHIP FUNCTIONS
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('Fuzzy Logic – Washing Machine System\nMembership Functions', fontsize=14, fontweight='bold')

# Dirt Level
axes[0].plot(dirt_level.universe, fuzz.trimf(dirt_level.universe, [0, 0, 5]),   'b-',  label='Low',    linewidth=2)
axes[0].plot(dirt_level.universe, fuzz.trimf(dirt_level.universe, [2, 5, 8]),   'g--', label='Medium', linewidth=2)
axes[0].plot(dirt_level.universe, fuzz.trimf(dirt_level.universe, [5, 10, 10]), 'r-',  label='High',   linewidth=2)
axes[0].set_title('Dirt Level', fontweight='bold')
axes[0].set_xlabel('Dirt Level (0-10)'); axes[0].set_ylabel('Membership Degree')
axes[0].legend(); axes[0].grid(True, alpha=0.3)

# Load Size
axes[1].plot(load_size.universe, fuzz.trimf(load_size.universe, [0, 0, 5]),   'b-',  label='Small',  linewidth=2)
axes[1].plot(load_size.universe, fuzz.trimf(load_size.universe, [2, 5, 8]),   'g--', label='Medium', linewidth=2)
axes[1].plot(load_size.universe, fuzz.trimf(load_size.universe, [5, 10, 10]), 'r-',  label='Large',  linewidth=2)
axes[1].set_title('Load Size', fontweight='bold')
axes[1].set_xlabel('Load Size (0-10)')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

# Cycle Time
axes[2].plot(cycle_time.universe, fuzz.trimf(cycle_time.universe, [0, 0, 30]),   'b-',  label='Short',  linewidth=2)
axes[2].plot(cycle_time.universe, fuzz.trimf(cycle_time.universe, [15, 30, 45]), 'g--', label='Medium', linewidth=2)
axes[2].plot(cycle_time.universe, fuzz.trimf(cycle_time.universe, [30, 60, 60]), 'r-',  label='Long',   linewidth=2)
axes[2].set_title('Cycle Time (Output)', fontweight='bold')
axes[2].set_xlabel('Cycle Time (minutes)')
axes[2].legend(); axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('membership_functions.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Membership functions saved.")

# ─────────────────────────────────────────────
# 6. TEST CASES (RULE VIEWER EQUIVALENT)
# ─────────────────────────────────────────────
test_cases = [
    (2, 2,  "Low Dirt, Small Load   "),
    (2, 8,  "Low Dirt, Large Load   "),
    (5, 5,  "Medium Dirt, Medium Load"),
    (8, 2,  "High Dirt, Small Load  "),
    (8, 8,  "High Dirt, Large Load  "),
    (5, 8,  "Medium Dirt, Large Load"),
]

print("\n" + "="*60)
print("  RULE VIEWER — FUZZY INFERENCE RESULTS")
print("="*60)
print(f"  {'Test Case':<28} {'Dirt':>6} {'Load':>6} {'Time (min)':>12}")
print("-"*60)

results = []
for dirt, load, label in test_cases:
    washing_sim.input['dirt_level'] = dirt
    washing_sim.input['load_size']  = load
    washing_sim.compute()
    t = washing_sim.output['cycle_time']
    results.append((dirt, load, t))
    print(f"  {label:<28} {dirt:>6} {load:>6} {t:>11.1f}")

print("="*60)

# ─────────────────────────────────────────────
# 7. HEATMAP — SURFACE VIEW
# ─────────────────────────────────────────────
dirt_range = np.linspace(0, 10, 20)
load_range = np.linspace(0, 10, 20)
Z = np.zeros((len(dirt_range), len(load_range)))

for i, d in enumerate(dirt_range):
    for j, l in enumerate(load_range):
        washing_sim.input['dirt_level'] = d
        washing_sim.input['load_size']  = l
        washing_sim.compute()
        Z[i, j] = washing_sim.output['cycle_time']

fig, ax = plt.subplots(figsize=(8, 6))
heatmap = ax.contourf(load_range, dirt_range, Z, levels=20, cmap='RdYlGn_r')
cbar = plt.colorbar(heatmap, ax=ax)
cbar.set_label('Cycle Time (minutes)', fontsize=11)
ax.set_xlabel('Load Size (0–10)',  fontsize=12)
ax.set_ylabel('Dirt Level (0–10)', fontsize=12)
ax.set_title('Fuzzy System Output – Surface View\n(Cycle Time Heatmap)', fontsize=13, fontweight='bold')

# Mark test cases
for (d, l, t) in results:
    ax.plot(l, d, 'w*', markersize=10)

plt.tight_layout()
plt.savefig('rule_viewer_surface.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✅ Rule viewer surface saved.")
print("\n✅ All done! Check membership_functions.png and rule_viewer_surface.png")
