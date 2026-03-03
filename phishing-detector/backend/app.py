from flask import Flask
from flask_cors import CORS

from config.settings import DEBUG, HOST, PORT
from routes import api_blueprint
import routes.health_route  # noqa: F401
import routes.predict_route  # noqa: F401


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(api_blueprint)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
