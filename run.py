import json
import sys
from pathlib import Path
from src.preprocessing.static_preprocessing import run_static_preprocessing


def load_config(config_path):
    """Load a JSON configuration file."""
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    # Check for skip flags
    skip_static = "--skip-static" in sys.argv

    print("=" * 60)
    print("MIMIC-IV PREPROCESSING PIPELINE")
    print("=" * 60)
    print()
    
    
    # --- Static Preprocessing ---
    if not skip_static:
        static_config = load_config("configs/static_preprocessing_params.json")
        
        in_dir = Path(static_config["paths"]["in_dir"])
        out_path = Path(static_config["paths"]["out_dir"])
        
        run_static_preprocessing(in_dir, "configs/static_preprocessing_params.json", out_path)
    else:
        print("Skipping static preprocessing")
    
    # --- Temporal Preprocessing ---
    # TODO: Temporal Preprocessing (not yet implemented)
    # if not skip_temporal:
    #     print("\nRunning temporal preprocessing...")
    #     temporal_config = load_config("configs/temporal_preprocessing.json")
    #     run_temporal_preprocessing(...)
    
    print("\n" + "=" * 60)
    print("ALL PREPROCSSING COMPLETED!")
    print("=" * 60)
    

if __name__ == "__main__":
    main()
