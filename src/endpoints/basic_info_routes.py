from crypt import methods
import json
from flask import Blueprint, request, jsonify
from src.scrapers import basic_info_scraper

basic_info = Blueprint(name='basic_anime_info', import_name=__name__)


@basic_info.route('/<string:anime_id>', methods=['GET'])
def basic_info_func(anime_id: str) -> object:
    output = basic_info_scraper.get_info(anime_id)
    return jsonify(output)

