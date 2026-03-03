from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "phishing_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"

HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
