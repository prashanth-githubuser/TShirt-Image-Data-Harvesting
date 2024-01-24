import ast
import pandas as pd
from pathlib import Path
from tqdm import tqdm

def perform_cleaning(metadata_path_list):
    """
    Perform cleaning on a list of metadata files.

    Args:
        metadata_path_list (list): A list of file paths containing metadata.

    Returns:
        None
    """
    try:
        print("Performing cleaning...")
        for path_root in tqdm(metadata_path_list, desc="Cleaning..."):
            df = pd.read_csv(path_root)
            path_out = Path(f"{path_root.parent}\cleaned_metadata")
            print(f"Dropping {df['Images'].duplicated().sum()} duplicates")
            df.drop_duplicates(subset='Images', inplace=True)
            path_out.mkdir(parents=True, exist_ok=True)  # Create the output directory if it doesn't exist
            df.to_csv(path_out / path_root.name, index=False, encoding='utf-8-sig')
        print(f"Cleaning completed.\nData saved to {path_out}")
    except Exception as e:
        print(e)