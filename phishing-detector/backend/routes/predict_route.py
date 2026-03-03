from flask import jsonify, request

from feature_extraction import extract_all_features
from model.model_loader import ModelService
from routes import api_blueprint


model_service = ModelService()


@api_blueprint.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True) or {}
    url = payload.get("url", "").strip()
    html = payload.get("html", "")

    if not url:
        return jsonify({"error": "The 'url' field is required."}), 400

    features = extract_all_features(url, html)
    result = model_service.predict(features)
    return jsonify(result), 200
