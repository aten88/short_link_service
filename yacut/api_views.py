from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap
from .services import URLService


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    if not request.get_json():
        return jsonify({'message': 'Отсутствует тело запроса'}), HTTPStatus.BAD_REQUEST
    result = URLService.validate_create_url(request.get_json())
    if 'errors' in result:
        return jsonify({'message': result['errors']}), result['status']
    return jsonify(result['data']), result['status']


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    if URLMap.query.filter_by(short=short_id).first() is None:
        return jsonify({'message': 'Указанный id не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': URLMap.query.filter_by(short=short_id).first().original}), HTTPStatus.OK
