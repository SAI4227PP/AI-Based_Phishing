from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "dataset" / "phishing_dataset.csv"
PROCESSED_PATH = ROOT / "dataset" / "processed" / "phishing_dataset_processed.csv"


def preprocess_dataset(input_path: Path = DATASET_PATH, output_path: Path = PROCESSED_PATH) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    df = df.dropna().drop_duplicates()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    processed = preprocess_dataset()
    print(f"Processed rows: {len(processed)}")
