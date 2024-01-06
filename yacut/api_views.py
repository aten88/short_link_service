from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from . import app, db
from .models import URLMap
from .utils import create_random_url


@app.route('/api/id/', methods=['POST'])
def create_id():
    """ Метод создания записи через API. """
    data = request.get_json()
    original_url = data.get('url')
    short_url = data.get('custom_id')
    if short_url is None:
        short_url = create_random_url()
    if len(short_url) > 16:
        return jsonify({'message': 'Указано недопустимое имя для короткой ссылки'}), 400
    existing_short_url = URLMap.query.filter_by(short=short_url).first()
    if existing_short_url:
        return jsonify({'message': 'Предложенный вариант короткой ссылки уже существует.'}), 400
    if not (short_url.isalnum() and short_url.isascii()):
        return jsonify({'message': 'Указано недопустимое имя для короткой ссылки'}), 400
    url_map = URLMap(original=original_url, short=short_url)
    try:
        db.session.add(url_map)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Отсутствует тело запроса'}), 400
    return jsonify(url_map.url_to_dict()), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """ Метод получения ссылки по идентификатору. """
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        return jsonify({'message': 'Указанный id не найден'}), 404
    return jsonify({'url': url_map.original}), 200
