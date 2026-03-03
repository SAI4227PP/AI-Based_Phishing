from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np

from config.constants import FEATURE_COLUMNS
from config.settings import MODEL_PATH, SCALER_PATH


class ModelService:
    def __init__(self, model_path: Path = MODEL_PATH, scaler_path: Path = SCALER_PATH) -> None:
        self.model = self._load_pickle(model_path)
        self.scaler = self._load_pickle(scaler_path)

    @staticmethod
    def _load_pickle(path: Path):
        if not path.exists() or path.stat().st_size == 0:
            return None
        try:
            return joblib.load(path)
        except Exception:
            return None

    def _prepare_vector(self, features: dict) -> np.ndarray:
        return np.array([[features.get(column, 0) for column in FEATURE_COLUMNS]], dtype=float)

    def _heuristic_score(self, features: dict) -> float:
        score = 0.0
        score += 0.12 if features.get("having_IP_Address") else 0.0
        score += 0.10 if features.get("Shortining_Service") else 0.0
        score += 0.08 if features.get("having_At_Symbol") else 0.0
        score += 0.08 if features.get("HTTPS_token") else 0.0
        score += 0.06 if features.get("RightClick") else 0.0
        score += 0.06 if features.get("Iframe", 0) > 0 else 0.0
        score += 0.06 if features.get("Submitting_to_email") else 0.0
        score += min(features.get("having_Sub_Domain", 0) * 0.05, 0.15)
        score += 0.08 if features.get("SSLfinal_State") == 0 else 0.0
        score += min(features.get("URL_Length", 0) / 500.0, 0.15)
        return min(score, 0.99)

    def predict(self, features: dict) -> dict:
        vector = self._prepare_vector(features)
        transformed = self.scaler.transform(vector) if self.scaler is not None else vector

        if self.model is not None:
            if hasattr(self.model, "predict_proba"):
                probability = float(self.model.predict_proba(transformed)[0][1])
            else:
                raw_prediction = float(self.model.predict(transformed)[0])
                probability = 1.0 if raw_prediction >= 1 else 0.0
        else:
            probability = self._heuristic_score(features)

        label = "phishing" if probability >= 0.5 else "legitimate"
        return {
            "label": label,
            "risk_score": round(probability, 4),
            "used_trained_model": self.model is not None,
            "features": features,
        }
