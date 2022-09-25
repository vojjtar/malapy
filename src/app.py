""" MALAPY API """

# loading libraries
from flask import Flask
import sys

# loading modules
from src.endpoints.basic_info_routes import basic_info


app = Flask(__name__)


app.register_blueprint(basic_info, url_prefix='/api/v1/anime/basic_info')