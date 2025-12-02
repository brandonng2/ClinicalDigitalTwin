# run.py
import json
import os
from src.preprocessing.static_preprocessing import process_static_data
from src.preprocessing.temporal_preprocessing import process_temporal_data

def load_config(config_path):
    """Load a JSON configuration file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    print("=== Starting Preprocessing Pipeline ===\n")
    
    # --- Static Preprocessing ---
    static_config_path = "configs/static_preprocessing.json"
    static_config = load_config(static_config_path)
    
    print("Running static preprocessing...")
    process_static_data(static_config)
    print("Static preprocessing complete!\n")
    
    # --- Temporal Preprocessing ---
    temporal_config_path = "configs/temporal_preprocessing.json"
    temporal_config = load_config(temporal_config_path)
    
    print("Running temporal preprocessing...")
    process_temporal_data(temporal_config)
    print("Temporal preprocessing complete!\n")
    
    print("=== All Preprocessing Done! ===")

if __name__ == "__main__":
    main()
