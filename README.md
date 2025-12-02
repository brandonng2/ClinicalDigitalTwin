# ClinicalDigitalTwin

A clean, modular pipeline for preprocessing MIMIC-IV ECG and hospital data.

## Project Structure

```
.
├── configs/
│   ├── static_preprocessing.json     # Configuration for static/column-based CSV preprocessing
│   └── temporal_preprocessing.json   # Configuration for temporal/row-based CSV preprocessing
├── data/
│   ├── raw/                          # Raw input data files (e.g., MIMIC-IV CSVs)
│   └── processed/                    # Output of preprocessing scripts
├── notebooks/                         # Jupyter notebooks for testing and exploration
├── src/
│   └── preprocessing/
│       ├── static_preprocessing.py   # Functions to preprocess static/column-based data
│       └── temporal_preprocessing.py # Functions to preprocess temporal/row-based data
├── run.py                             # Main script to execute the preprocessing pipeline
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## License

This project is for research purposes using MIMIC-IV data. Please ensure compliance with MIMIC-IV data use agreements.