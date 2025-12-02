import json
from pathlib import Path
import pandas as pd
import numpy as np


CONFIG_PATH = Path("configs/static_preprocessing.json")
OUT_PATH = Path("data/processed/static_features.parquet")

def load_config(config_path):
    """Load configuration from specified path."""
    with open(config_path, "r") as f:
        return json.load(f)


def load_static_data(config):
    """Load all static CSV files defined in config."""
    in_dir = Path(config["paths"]["in_dir"])
    s = config["static_sources"]
    
    def r(p): return in_dir / p
    
    # Load all CSVs in order
    patients = pd.read_csv(r(s["patients"]))
    admissions = pd.read_csv(r(s["admissions"]))
    hosp_diagnosis = pd.read_csv(r(s["hosp_diagnosis"]))
    drgcodes = pd.read_csv(r(s["drgcodes"]))
    icustays = pd.read_csv(r(s["icustays"]))
    edstays = pd.read_csv(r(s["edstays"]))
    ed_diagnosis = pd.read_csv(r(s["ed_diagnosis"]))
    record_list = pd.read_csv(r(s["record_list"]))
    
    return patients, admissions, hosp_diagnosis, drgcodes, icustays, edstays, ed_diagnosis, record_list


def clean_cols_types(df):
    """
    Normalize column types:
      - Convert columns containing 'date' or 'time' in their names to datetime.
      - Convert all other object columns to Pandas string dtype.
    """
    time_keywords = ("date", "time", "dod")

    for col in df.columns:
        col_lower = col.lower()

        if any(k in col_lower for k in time_keywords):
            df[col] = pd.to_datetime(df[col], errors="coerce")
            continue

        # Convert object columns to Pandas string
        if df[col].dtype == "object":
            df[col] = df[col].astype("string")

    return df

def clean_diagnosis_data(df):

    df = clean_cols_types(df)

    # Sort to preserve order
    df = df.sort_values(["subject_id", "hadm_id", "seq_num"])

    # Group by subject_id and hadm_id and aggregate lists directly
    df_diag_agg = (
        df
        .groupby(["subject_id", "hadm_id"], as_index=False)
        .agg({
            "icd_code": list,      # list of ICD codes
            "long_title": list     # list of diagnosis names
        })
        .rename(columns={"icd_code": "hosp_icd_codes_diagnosis", "long_title": "hosp_diagnosis"})
    )
    return df_diag_agg

def preprocess_admissions(df):
    df = df.drop(columns=['insurance', 'admission_location', 'marital_status', 'hospital_expire_flag', 'language', 'marital_status'])
    df = clean_cols_types(df)
    return df

def preprocess_patient(df):
    df = df.drop(columns=['anchor_year', 'anchor_year_group'])
    df = clean_cols_types(df)
    return df