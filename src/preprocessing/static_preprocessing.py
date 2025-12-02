import json
from pathlib import Path
import pandas as pd
import numpy as np
import os


CONFIG_PATH = Path("configs/static_preprocessing.json")
OUT_PATH = Path("data/processed/static_features.parquet")

import json
from pathlib import Path
import pandas as pd
import numpy as np


def load_config(config_path):
    """Load configuration from specified path."""
    with open(config_path, "r") as f:
        return json.load(f)


def load_static_data(in_dir, config):
    """Load all static CSV files defined in config."""
    in_dir = Path(in_dir)
    s = config["static_sources"]
    
    # Load all CSVs in order
    patients = pd.read_csv(in_dir / s["patients"])
    admissions = pd.read_csv(in_dir / s["admissions"])
    hosp_diagnosis = pd.read_csv(in_dir / s["hosp_diagnosis"])
    drgcodes = pd.read_csv(in_dir / s["drgcodes"])
    icustays = pd.read_csv(in_dir / s["icustays"])
    edstays = pd.read_csv(in_dir / s["edstays"])
    ed_diagnosis = pd.read_csv(in_dir / s["ed_diagnosis"])
    record_list = pd.read_csv(in_dir / s["record_list"])
    
    return patients, admissions, hosp_diagnosis, drgcodes, icustays, edstays, ed_diagnosis, record_list


def clean_cols_types(df):
    """
    Normalize column types:
      - Convert columns containing 'date', 'time', or 'dod' to datetime.
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


def clean_diagnosis_data(df, prefix):
    """
    Aggregate diagnosis data by subject_id and ID column.
    Returns lists of ICD codes and diagnosis names per admission/stay.
    """

    df = clean_cols_types(df)

    # Sort by first 3 columns to preserve order
    sort_cols = df.columns[:3].tolist()
    df = df.sort_values(sort_cols)

    # Group by first 2 columns (typically subject_id and hadm_id/stay_id)
    group_cols = df.columns[:2].tolist()
    
    df_diag_agg = (
        df
        .groupby(group_cols, as_index=False)
        .agg({
            "icd_code": list,
            "long_title": list
        })
        .rename(columns={
            "icd_code": f"{prefix}_icd_codes_diagnosis",
            "long_title": f"{prefix}_diagnosis"
        })
    )
    return df_diag_agg


def preprocess_admissions(df):
    """Drop unnecessary columns from admissions data."""
    df = df.drop(columns=[
        'insurance', 'admission_location', 'marital_status',
        'hospital_expire_flag', 'language', 'admit_provider_id'
    ])
    df = clean_cols_types(df)
    df = df.rename(columns={'admittime': 'hosp_dischtime', 'dischtime': 'hosp_dischtime'})

    return df

def preprocess_patient(df):
    """Drop anchor columns from patient data."""
    df = df.drop(columns=['anchor_year', 'anchor_year_group'])
    df = clean_cols_types(df)
    return df


def preprocess_drgcodes(df):
    """
    Flatten DRG codes dataframe so each admission has one row.
    Keep APR (drg_code, description, severity, mortality) and HCFA (drg_code, description).
    """
    # Select relevant columns
    cols = ["subject_id", "hadm_id", "drg_type", "drg_code", 
            "description", "drg_severity", "drg_mortality"]
    df = df[cols].copy()

    # Pivot to wide format
    df_flat = df.pivot(
        index=["subject_id", "hadm_id"],
        columns="drg_type",
        values=["drg_code", "description", "drg_severity", "drg_mortality"]
    )

    # Flatten MultiIndex columns
    df_flat.columns = [f"{val}_{typ.lower()}" for val, typ in df_flat.columns]

    # Keep only needed columns
    columns_to_keep = [
        "drg_code_apr", "description_apr", "drg_severity_apr", "drg_mortality_apr",
        "drg_code_hcfa", "description_hcfa"
    ]
    df_flat = df_flat[columns_to_keep].reset_index()
    df_flat = clean_cols_types(df_flat)

    return df_flat


def add_prefix_to_columns(df, prefix):
    """
    Add prefix to all columns except subject_id and hadm_id.
    """
    exclude_cols = ['subject_id', 'hadm_id']
    
    rename_dict = {
        col: f"{prefix}_{col}" 
        for col in df.columns 
        if col not in exclude_cols
    }
    
    return df.rename(columns=rename_dict)