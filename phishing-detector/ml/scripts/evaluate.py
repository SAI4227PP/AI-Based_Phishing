from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "dataset" / "phishing_dataset.csv"
MODEL_PATH = ROOT / "models" / "phishing_model.pkl"
SCALER_PATH = ROOT / "models" / "scaler.pkl"
TARGET_COLUMN = "label"


def evaluate_model():
    df = pd.read_csv(DATASET_PATH)
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    predictions = model.predict(scaler.transform(X))

    print(f"Accuracy: {accuracy_score(y, predictions):.4f}")
    print(classification_report(y, predictions))


if __name__ == "__main__":
    evaluate_model()
