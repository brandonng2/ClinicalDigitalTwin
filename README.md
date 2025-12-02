# ClinicalDigitalTwin

A clean, modular pipeline for preprocessing MIMIC-IV hospital, ICU, ED, and ECG data.  
**Note:** Temporal preprocessing is still in progress.

## Project Structure
```
.
├── configs/
│   ├── static_preprocessing.json      # Configuration for static/column-based CSV preprocessing
│   └── temporal_preprocessing.json    # Configuration for temporal/row-based CSV preprocessing
├── data/
│   ├── raw/                           # Raw input data files (e.g., MIMIC-IV CSVs)
│   └── processed/                     # Output of preprocessing scripts
├── notebooks/                         # Jupyter notebooks for testing and exploration
├── src/
│   └── preprocessing/
│       ├── static_preprocessing.py    # Functions to preprocess static/column-based data
│       └── temporal_preprocessing.py  # Functions to preprocess temporal/row-based data
├── run.py                             # Main script to execute the preprocessing pipeline
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Running the Preprocessing Pipeline

```bash
python run.py
```

This will execute both static and temporal preprocessing according to their respective configuration files in `configs/`.

- Static preprocessing: Processes demographic, comorbidity, and baseline features.

- Temporal preprocessing: Processes time-series events such as ICU stays, vitals, labs, medications, and procedures.

### 3. Notebooks

Use the notebooks in `notebooks/` to test and explore preprocessing functions before running the full pipeline.

## License

This project is for research purposes using MIMIC-IV data. Please ensure compliance with MIMIC-IV data use agreements.