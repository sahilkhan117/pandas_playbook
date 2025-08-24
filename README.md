# 🐼📊 Pandas Playbook — Learn. Code. Analyze.

<div align="center">
<img src="./public/icon.png" alt="Pandas Icon" width="80">

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Advanced-red?logo=pandas)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Progress](https://img.shields.io/badge/Progress-100%25-brightgreen)](https://github.com/sahilkhan117/pandas_playbook)

</div>

<p align="center">
  <img src="./public/main.png" alt="Pandas Example" width="500">
</p>

---

> 🚀 **Your one-stop, hands-on journey from Pandas basics to real-world data analysis projects** — fully powered by [uv](https://github.com/astral-sh/uv) for ultra-fast dependency management.

## 💡 Why This Repo?
My Pandas learning journey covers **all essential Pandas topics**—from basics to advanced, with multiple Business Problems, LeetCode challenges and projects. It’s:
## 💡 Why Pandas Playbook?
Unlike scattered tutorials, this playbook is:
- 🧩 **Structured** from basics to projects
- 📂 **Organized** with datasets, scripts, and notebooks
- ⚡ **Fast** — powered by `uv` for dependency management


Perfect for mastering Pandas efficiently!

---

| Tool | Purpose |
|------|---------|
| 🐍 Python 3.12 | Core language |
| 🐼 Pandas | Data manipulation |
| 📊 Matplotlib | Visualization |
| 📓 Jupyter | Interactive notebooks |

---

## 📂 Project Structure

```sh
pandas-playbook/
├── README.md                   # 📄 Main guide to the repo and learning path
├── requirements.txt            # 📋 List of dependencies (pandas, matplotlib, jupyter)
├── .gitignore                  # 🗑 Ignores .ipynb_checkpoints, __pycache__, etc.
├── CONTRIBUTING.md             # 🤝 Guidelines for contributing to the repo
├── data/                       # 📁 Practice datasets
│   ├── raw/                    # 📂 Unprocessed datasets (iris.csv, titanic.csv, sales.csv, world_gdp_data.csv)
│   └── processed/              # 📂 Cleaned datasets from notebooks/projects
├── beginner/                   # 🌱 Fundamental Pandas concepts
│   ├── 1_dataframes_series.ipynb # 🛠 Creates and manipulates DataFrames and Series
│   ├── 2_reading_writing_data.ipynb # 📥 Reads/writes data (CSV, Excel, JSON)
│   ├── 3_data_exploration.ipynb  # 🔍 Explores data with head, tail, info, describe
│   ├── 4_indexing_slicing.ipynb  # ✂️ Selects data using loc, iloc, columns
│   └── 5_data_cleaning.ipynb     # 🧹 Handles missing values, duplicates, strings
├── intermediate/               # 🔄 Data wrangling techniques
│   ├── 6_filtering_sorting.ipynb # 🔎 Filters and sorts data with query, sort_values
│   ├── 7_grouping_aggregation.ipynb # 📊 Groups and aggregates with groupby, pivot_table
│   ├── 8_merging_joining.ipynb   # 🔗 Merges and joins data with merge, concat
│   └── 9_applying_functions.ipynb # ⚙️ Applies functions with apply, map, lambda
├── advanced/                   # 🚀 Advanced Pandas techniques
│   ├── 10_time_series_analysis.ipynb # 📅 Handles time-series with datetime, resample
│   ├── 11_performance_optimization.ipynb # ⚡ Optimizes with vectorization, category dtype
│   ├── 12_advanced_visualization.ipynb # 📈 Visualizes with Pandas plots, Matplotlib
│   ├── 13_multiindex_hierarchical.ipynb # 🏢 Manages MultiIndex and hierarchical data
│   └── 14_reshaping_data.ipynb     # 🔄 Reshapes data with pivot, melt, wide_to_long
├── leetcode-pandas-basics/     # 🎯 Solutions for Introduction to Pandas
│   ├── notes.md                # 📝 Summary of key learnings from problems
│   ├── ... (15 problems)       # ... Additional LeetCode solutions
│   └── datasets/               # 📂 Problem-specific input data
├── leetcode-30-days/           # 🏆 Solutions for 30 Days of Pandas
│   ├── notes.md                # 📝 Summary of techniques from problems
│   ├── ... (30+ problems)       # ... Additional LeetCode solutions
│   └── datasets/               # 📂 Problem-specific input data
├── projects/                   # 🛠 Real-world applications
│   ├── titanic_eda/            # 📊 Exploratory data analysis on Titanic
│   │   ├── README.md           # 📄 Project overview and goals
│   │   ├── notebook.ipynb      # 📓 Cleans, explores, visualizes Titanic data
│   │   └── data/titanic.csv    # 📂 Titanic dataset for EDA
│   └── sales_analysis/         # 📈 Analyzes sales trends
│       ├── README.md           # 📄 Project overview and insights
│       ├── notebook.ipynb      # 📓 Groups and visualizes sales data
│       └── data/sales.csv      # 📂 Sales dataset for analysis
└── resources/                  # 📚 Extra learning materials
    ├── cheatsheet.pdf          # 📋 Quick reference for Pandas commands
    └── links.md                # 🔗 Links to Pandas docs, tutorials
```
---

## 🛣 Learning Roadmap

| Step | Topic                     | Status         | Key Topics |
|------|---------------------------|----------------|------------|
| 1️⃣  | Beginner Concepts          | ✅ Done         | DataFrames, IO, exploration, cleaning |
| 2️⃣  | Intermediate Manipulation  | ✅ Done         | Filtering, grouping, merging, apply |
| 3️⃣  | Advanced Techniques       | ✅ Done         | Time-series, optimization, visuals, MultiIndex, reshaping |
| 4️⃣  | LeetCode Challenges       | ✅ Done         | Intro & 30 Days of Pandas |
| 5️⃣  | Projects                  | ✅ Done         | EDA, sales analysis |

---

## ⚡ Getting Started

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/sahilkhan117/pandas_playbook.git
   cd pandas-playbook
   ```

### 2. With uv
2. **Install Dependencies**:
   ```bash
   uv install
   ```
   or
   ```bash
   uv sync
   ```


### 2. With requirements.txt
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```
   or
   ```bash
   uv run <file-name>
   ```

Start with `beginner/dataframes_series.ipynb` and progress sequentially.

---

## 📊 Datasets Included

- **`data/raw/world_gdp_data.csv`**
- **`data/raw/amazon.csv`**
- **`data/raw/Cancer_Data.csv`**
- **`data/raw/NIFTY/-50`**

Cleaned data saved to `data/processed/`.

---

## ⭐ Support

If this helps you master Pandas, **star the repo** 🌟!  
Questions? Open an issue. Share your journey with #PandasLearning!

<p align="center">
  <b>Master Data with Pandas! 🐼</b>
</p>