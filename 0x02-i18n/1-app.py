from flask import Flask
from flask_babel import Babel
"""
a module to set a basic babel setup
"""


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
