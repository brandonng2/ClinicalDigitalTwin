# ClinicalDigitalTwin

A clean, modular pipeline for preprocessing MIMIC-IV ECG and hospital data.

## Project Structure

```
.
├── configs/
│   └── preprocessing_config.json   # Configuration settings
├── data/
│   ├── raw/                        # Raw data files
│   └── processed/                  # Processed output files
├── notebooks/                      # Jupyter notebooks for exploration
├── preprocessing.py                # Core preprocessing module
├── run.py                          # Main execution script
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## License

This project is for research purposes using MIMIC-IV data. Please ensure compliance with MIMIC-IV data use agreements.