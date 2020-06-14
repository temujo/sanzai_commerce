from flask import Flask

from sanzai.blueprints.page import page
from sanzai.blueprints.product import product
from sanzai.blueprints.cart import cart


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    app.register_blueprint(product, url_prefix='/delguur')
    app.register_blueprint(cart, url_prefix='/sags')

    return app
