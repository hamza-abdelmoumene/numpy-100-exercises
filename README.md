# NumPy 100 Exercises

Solutions to the canonical [100 NumPy Exercises](https://github.com/rougier/numpy-100) by Nicolas Rougier, organized by topic and implemented with explanatory comments.

Part of the AI Engineering roadmap at ESI Algeria (Ecole Superieure d'Informatique).

---

## Structure

```
numpy-100-exercises/
├── exercises/
│   └── 100_numpy_exercises.ipynb   original exercises (unmodified)
├── solutions/
│   ├── 01_10_array_creation.py
│   ├── 11_20_indexing.py
│   ├── 21_30_math_operations.py
│   ├── 31_40_array_manipulation.py
│   ├── 41_50_linear_algebra.py
│   ├── 51_60_random.py
│   ├── 61_70_sorting_searching.py
│   ├── 71_80_broadcasting.py
│   ├── 81_90_advanced.py
│   └── 91_100_ml_applications.py
└── README.md
```

---

## Progress

| Range | Topic | Status |
|---|---|:---:|
| 1–10 | Array creation and initialization | Done |
| 11–20 | Indexing and slicing | Done |
| 21–30 | Mathematical operations | Done |
| 31–40 | Array manipulation and reshaping | Done |
| 41–50 | Linear algebra | In progress |
| 51–60 | Random sampling | In progress |
| 61–70 | Sorting and searching | Pending |
| 71–80 | Broadcasting | Pending |
| 81–90 | Advanced indexing and tricks | Pending |
| 91–100 | ML-relevant applications | Pending |

---

## Setup

```bash
git clone https://github.com/hamza-abdelmoumene/numpy-100-exercises.git
cd numpy-100-exercises

pip install numpy jupyter

jupyter notebook exercises/100_numpy_exercises.ipynb
```

To run a solution file directly:

```bash
python solutions/01_10_array_creation.py
```

---

## Why This Matters

NumPy is the computational backbone of the entire scientific Python ecosystem: pandas, scikit-learn, PyTorch, and TensorFlow all build on NumPy arrays. Mastering vectorization, broadcasting, and linear algebra operations here eliminates the common bottleneck where ML students understand the theory but cannot implement it efficiently.

---

## Stack

Python 3.12 · NumPy 1.26 · Jupyter

---

**Author:** [Hamza Abdelmoumene](https://github.com/hamza-abdelmoumene) — ESI Algiers, AI Engineering
