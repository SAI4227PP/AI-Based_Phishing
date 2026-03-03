from flask import jsonify

from routes import api_blueprint


@api_blueprint.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200
