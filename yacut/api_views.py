from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap
from .services import URLService
from .utils import send_errors


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    if not request.get_json():
        return jsonify({'message': 'Отсутствует тело запроса'}), HTTPStatus.BAD_REQUEST
    short_url = URLService.create_short_url(request.get_json())
    if URLService.validate_url(request.get_json().get('url'), short_url):
        return send_errors(URLService.validate_url(request.get_json().get('url'), short_url))
    url_map = URLMap(original=request.get_json().get('url'), short=short_url)
    if URLService.create_record(url_map):
        return send_errors(URLService.create_record(url_map))
    return jsonify(url_map.url_to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    if URLMap.query.filter_by(short=short_id).first() is None:
        return jsonify({'message': 'Указанный id не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': URLMap.query.filter_by(short=short_id).first().original}), HTTPStatus.OK
