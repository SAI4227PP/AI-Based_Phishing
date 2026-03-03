# Implementation Guide

## Overview

This project is split into three runtime layers:

- `backend/`: Flask API that extracts phishing features and returns a risk score.
- `ml/`: Dataset, preprocessing, training, and evaluation scripts.
- `extension/`: Chrome extension that inspects the active page and calls the backend.

## Backend Folder Explanation

### `backend/feature_extraction/`

Each module extracts one feature group used by the phishing classifier.

`url_features.py` implements:

- `having_IP_Address`
- `URL_Length`
- `Shortining_Service`
- `having_At_Symbol`
- `double_slash_redirecting`
- `Prefix_Suffix`
- `having_Sub_Domain`

`html_features.py` implements:

- `Request_URL`
- `URL_of_Anchor`
- `Links_in_tags`
- `SFH`
- `Submitting_to_email`
- `Abnormal_URL`
- `Redirect`
- `on_mouseover`
- `RightClick`
- `popUpWidnow`
- `Iframe`

`ssl_features.py` implements:

- `SSLfinal_State`
- `HTTPS_token`

`domain_features.py` implements:

- `Domain_registeration_length`
- `age_of_domain`
- `DNSRecord`

`__init__.py` combines all groups into a single feature dictionary.

### `backend/model/`

- `model_loader.py` loads `phishing_model.pkl` and `scaler.pkl` if they exist.
- If no trained artifacts are present, it falls back to a heuristic risk score so the API still works.

### `backend/routes/`

- `predict_route.py` exposes `POST /predict`.
- `health_route.py` exposes `GET /health`.

### `backend/app.py`

Creates the Flask app, enables CORS, and registers the API routes.

## ML Folder Explanation

### `ml/scripts/train.py`

- Loads the dataset
- Splits train and test data
- Trains a `RandomForestClassifier`
- Saves `phishing_model.pkl` and `scaler.pkl`

### `ml/dataset/`

- Store the UCI/USC phishing dataset or your own engineered dataset here.
- The included CSV is a tiny starter sample with the required columns.

### `ml/notebooks/training.ipynb`

Use this notebook for experimentation, feature analysis, and model validation.

## Chrome Extension Structure

### `extension/background/background.js`

- Listens for completed page loads
- Captures the current tab URL and HTML
- Sends the payload to the Flask backend
- Stores the latest result for the popup
- Shows a badge warning for high-risk pages

### `extension/content/content.js`

- Reads page HTML
- Detects hidden forms
- Detects JavaScript traps like mouseover and right-click blocking
- Collects iframe counts
- Sends the result to the background worker

### `extension/popup/popup.html`

Provides a simple UI that displays:

- Risk score
- Classification label
- Whether the response came from the ML model or heuristic fallback

## Suggested Next Steps

1. Replace heuristic domain/SSL placeholders with live WHOIS, DNS, and certificate checks.
2. Train a real model and copy the generated `ml/models/*.pkl` files into `backend/model/`.
3. Add tests for feature extraction and API routes.
