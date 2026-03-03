# Current Implementation

## Implemented Now

- Project documentation folder at `docs/`
- Flask backend bootstrap with `GET /health` and `POST /predict`
- Feature extraction modules for URL, HTML, SSL, and domain signals
- Model loading with graceful fallback when `.pkl` files are empty or missing
- ML scripts for preprocessing, training, and evaluation
- Starter dataset with the required feature columns
- Chrome extension manifest, background worker, content script, and popup UI

## Current Behavior

### Backend

- Accepts JSON payloads in the format:

```json
{
  "url": "https://example.com",
  "html": "<html>...</html>"
}
```

- Returns:

```json
{
  "label": "legitimate",
  "risk_score": 0.14,
  "used_trained_model": false,
  "features": {}
}
```

- If no trained model is present, a heuristic score is returned instead of failing.

### ML

- `train.py` expects a CSV with a `label` column.
- The included sample dataset is only for structure validation, not for production training.

### Extension

- Automatically scans pages after navigation completes.
- Saves the most recent backend result in `chrome.storage.local`.
- Displays the last result in the popup.

## Placeholders Still Needed

- Real trained model artifacts in:
  - `backend/model/phishing_model.pkl`
  - `backend/model/scaler.pkl`
  - `ml/models/phishing_model.pkl`
  - `ml/models/scaler.pkl`
- Real icon files in `extension/icons/`
- A larger labeled dataset in `ml/dataset/`
- More accurate domain and SSL lookups

## Known Limits

- Domain age and registration length are heuristic estimates right now.
- SSL validation currently checks only URL scheme and suspicious domain tokens.
- Extension warning is a badge indicator, not a blocking interstitial.
