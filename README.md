# ClinicalDigitalTwin

A clean, modular pipeline for preprocessing MIMIC-IV hospital, ICU, ED, and ECG data.  
**Note:** Temporal preprocessing is still in progress.

## Project Overview

This repository provides an end-to-end framework for preparing MIMIC-IV datasets for clinical digital twin modeling. It supports both static (column-based) and temporal (row-based) preprocessing of patient data, enabling streamlined integration for downstream analyses and predictive modeling.

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

## Prerequisites

- **Python:** 3.8 or higher
- **MIMIC-IV Access:** Credentialed access through PhysioNet (see below)
- **Required Training:** CITI "Data or Specimens Only Research" certification

This project requires the MIMIC-IV dataset, which is a **restricted-access resource**.

### Steps to Obtain Access:

1. Complete the CITI "Data or Specimens Only Research" course: https://about.citiprogram.org/
2. Create a PhysioNet account: https://physionet.org/register/
3. Request access to MIMIC-IV v3.1: https://physionet.org/content/mimiciv/
4. Sign the PhysioNet Credentialed Health Data Use Agreement
5. Once approved, download the dataset and place CSV files in `data/raw/`

**Note:** Approval typically takes a few business days after submitting your request.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ClinicalDigitalTwin.git
cd ClinicalDigitalTwin
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Data Placement

Ensure MIMIC-IV CSV files are in the `data/raw/` directory before running preprocessing.

## Usage

### Running the Preprocessing Pipeline
```bash
python run.py
```

This executes both static and temporal preprocessing according to the configuration files in `configs/`:

- **Static preprocessing:** Processes demographic, comorbidity, and baseline features
- **Temporal preprocessing:** Processes time-series events such as ICU stays, vitals, labs, medications, and procedures (**Note:** Still in progress)


### 3. Notebooks

Use the notebooks in `notebooks/` to test and explore preprocessing functions before running the full pipeline.

## License

This project is intended for **research use only** with MIMIC-IV data. By using this repository, you agree to comply with:

- The MIMIC-IV Data Use Agreement: [PhysioNet Credentialing](https://physionet.org/content/mimiciv/view-dua/3.1/)
- Any institutional or IRB requirements for working with de-identified patient data.

**Full License:** [PhysioNet Data License](https://physionet.org/content/mimiciv/view-license/3.1/)
Redistribution and commercial use are prohibited.

## Acknowledgments

This project was built using the MIMIC-IV dataset provided by the MIT Laboratory for Computational Physiology.