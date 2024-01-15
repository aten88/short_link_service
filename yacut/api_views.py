from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap
from .services import URLService
from .error_handlers import InvalidURLException


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    try:
        if not request.get_json():
            raise InvalidURLException('Отсутствует тело запроса')
        result = URLService.create_url(request.get_json().get('url'), request.get_json().get('custom_id'))
    except InvalidURLException as e:
        return jsonify({'message': str(e)}), HTTPStatus.BAD_REQUEST
    return jsonify(result), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    short_url_object = URLMap.query.filter_by(short=short_id).first()
    if short_url_object is None:
        return jsonify({'message': 'Указанный id не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': short_url_object.original}), HTTPStatus.OK
