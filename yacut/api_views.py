from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap
from .services import URLService


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    try:
        if not request.get_json():
            raise ValueError('Отсутствует тело запроса')
        result = URLService.create_url(request.get_json())
    except ValueError as e:
        return jsonify({'message': str(e)}), HTTPStatus.BAD_REQUEST
    return jsonify(result), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    if URLMap.query.filter_by(short=short_id).first() is None:
        return jsonify({'message': 'Указанный id не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': URLMap.query.filter_by(short=short_id).first().original}), HTTPStatus.OK
