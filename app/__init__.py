from flask import Flask
from app.word_occurrences_blueprint.views import word_occurrences

def create_app():
    app = Flask(__name__)
    app.register_blueprint(word_occurrences)

    return app