from flask import Flask
from src.controllers.pessoa_fisica_controller import pessoa_fisica_bp
from src.controllers.pessoa_juridica_controller import pessoa_juridica_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pessoa_fisica_bp)
    app.register_blueprint(pessoa_juridica_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
