from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap
from .services import URLService


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Отсутствует тело запроса'}), HTTPStatus.BAD_REQUEST
    original_url = data.get('url')
    short_url = URLService.create_short_url(data)
    if URLService.check_for_validate(original_url, short_url):
        for errors in URLService.check_for_validate(original_url, short_url):
            return jsonify({'message': errors}), HTTPStatus.BAD_REQUEST
    url_map = URLMap(original=original_url, short=short_url)
    if URLService.create_record(url_map):
        for error in URLService.create_record(url_map):
            return jsonify({'message': error}), HTTPStatus.BAD_REQUEST
    return jsonify(url_map.url_to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        return jsonify({'message': 'Указанный id не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': url_map.original}), HTTPStatus.OK
