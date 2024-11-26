# About

This is an automatisation script that creates a new data science project

# Tree

```bash
project-name/
│
├── data/
│   ├── raw/            # Unprocessed datasets
│   ├── interim/        # Partially processed data
│   ├── processed/      # Clean, final datasets
│   └── external/       # External datasets (e.g., APIs, public sources)
│
├── notebooks/          # Jupyter notebooks for exploration and prototyping
│
├── src/                # Source code for scripts, models, and pipelines
│   ├── data/           # Data processing/cleaning scripts
│   ├── features/       # Feature engineering scripts
│   ├── models/         # Model training and evaluation scripts
│   └── visualization/  # Code for plots, dashboards, etc.
│
├── reports/            # Generated analysis, reports, and presentations
│   ├── figures/        # Images, plots, etc.
│
├── tests/              # Unit and integration tests
│
├── requirements.txt    # List of dependencies (for pip/conda)
├── README.md           # Overview of the project
├── config.yaml         # Configuration file for project settings
└── .gitignore          # Files and folders to ignore in Git
```

# Usage

```bash
python3 ds_proj_create/src/main.py
```