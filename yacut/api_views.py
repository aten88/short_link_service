from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from . import app, db
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    data = request.get_json()
    original_url = data.get('original')
    short_url = data.get('short')
    if not original_url or not short_url:
        return jsonify({'message': 'Отсутствует тело запроса'}), 400
    existing_url_map = URLMap.query.filter_by(original=original_url).first()
    if existing_url_map:
        return jsonify({'message': 'Предложенный вариант полной ссылки уже существует.'}), 400
    url_map = URLMap()
    url_map.from_dict(data)
    try:
        db.session.add(url_map)
        db.session.commit()
        return jsonify({'data': url_map.url_to_dict()}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Ошибка целостности'}), 500


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        return jsonify({'message': 'Указанный id не найден'}), 404
    return jsonify({'url': url_map.original}), 200
