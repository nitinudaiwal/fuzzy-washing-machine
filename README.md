# 🧺 Fuzzy Logic System – Washing Machine Cycle Time

**Course**: Introduction to Intelligent Systems  
**Assignment**: Q1  
**Author**: Nitin Udaiwal  
**Reg. No**: 23FE10CCE00056  
**University**: Manipal University Jaipur  

---

## 📌 Problem Statement

Design a fuzzy logic system to determine the **washing machine cycle time** based on:
- **Dirt Level** (0–10)
- **Load Size** (0–10)

---

## 🧠 System Design

### Inputs & Outputs

| Variable     | Type   | Range  | Fuzzy Sets            |
|--------------|--------|--------|-----------------------|
| Dirt Level   | Input  | 0–10   | Low, Medium, High     |
| Load Size    | Input  | 0–10   | Small, Medium, Large  |
| Cycle Time   | Output | 0–60 min | Short, Medium, Long |

### Membership Functions (Triangular)

**Dirt Level:**
- Low    → trimf [0, 0, 5]
- Medium → trimf [2, 5, 8]
- High   → trimf [5, 10, 10]

**Load Size:**
- Small  → trimf [0, 0, 5]
- Medium → trimf [2, 5, 8]
- Large  → trimf [5, 10, 10]

**Cycle Time:**
- Short  → trimf [0, 0, 30]
- Medium → trimf [15, 30, 45]
- Long   → trimf [30, 60, 60]

---

## 📋 Fuzzy Rules (9 Rules)

| Rule | Dirt Level | Load Size | Cycle Time |
|------|------------|-----------|------------|
| 1    | Low        | Small     | Short      |
| 2    | Low        | Medium    | Short      |
| 3    | Low        | Large     | Medium     |
| 4    | Medium     | Small     | Short      |
| 5    | Medium     | Medium    | Medium     |
| 6    | Medium     | Large     | Medium     |
| 7    | High       | Small     | Medium     |
| 8    | High       | Medium    | Long       |
| 9    | High       | Large     | Long       |

---

## 🔄 Fuzzy Inference Process

```
Raw Input → Fuzzification → Rule Evaluation → Aggregation → Defuzzification → Crisp Output
```

1. **Fuzzification** – Map crisp input to membership degrees
2. **Rule Evaluation** – Apply AND (min) for each rule condition
3. **Aggregation** – Combine all rule outputs using OR (max)
4. **Defuzzification** – Centroid method to get crisp output

---

## 📊 Sample Results (Rule Viewer)

| Test Case               | Dirt | Load | Cycle Time |
|-------------------------|------|------|------------|
| Low Dirt, Small Load    | 2    | 2    | ~11.1 min  |
| Low Dirt, Large Load    | 2    | 8    | ~30.0 min  |
| Medium Dirt, Medium Load| 5    | 5    | ~30.0 min  |
| High Dirt, Small Load   | 8    | 2    | ~30.0 min  |
| High Dirt, Large Load   | 8    | 8    | ~48.9 min  |
| Medium Dirt, Large Load | 5    | 8    | ~30.0 min  |

---

## 🛠️ How to Run

```bash
pip install scikit-fuzzy numpy matplotlib
python washing_machine_fuzzy.py
```

**Outputs generated:**
- `membership_functions.png` – All 3 membership function plots
- `rule_viewer_surface.png`  – 2D heatmap surface view

---

## 📁 Files

```
washing_machine_fuzzy/
├── washing_machine_fuzzy.py     # Main Python implementation
├── membership_functions.png     # MF plots
├── rule_viewer_surface.png      # Surface/heatmap output
└── README.md                    # This documentation
```

---

## 🔍 Note on MATLAB Equivalent

This system mirrors the MATLAB Fuzzy Logic Toolbox implementation:
- `trimf()` → Triangular membership function
- `mamdani` inference engine
- `centroid` defuzzification
- The `rule_viewer_surface.png` shows the same output as MATLAB's Rule Viewer
