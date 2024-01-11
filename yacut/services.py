from http import HTTPStatus

from . import db
from .models import URLMap
from .constants import MAX_LENGHT_SHORT_A
from .utils import create_random_url


class URLService:
    """ Класс с универсальными методами бизнес-логики. """

    def validate_create_url(data):
        """ Метод создания короткой ссылки. """
        errors = []
        original_url = data.get('url')
        short_url = data.get('custom_id')
        if not original_url:
            errors.append('\"url\" является обязательным полем!')
        if not short_url:
            short_url = create_random_url()
        if not (short_url.isalnum() and short_url.isascii()):
            errors.append('Указано недопустимое имя для короткой ссылки')
        if len(short_url) > MAX_LENGHT_SHORT_A:
            errors.append('Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=short_url).first():
            errors.append('Предложенный вариант короткой ссылки уже существует.')
        if errors:
            return {'errors': errors[0], 'status': HTTPStatus.BAD_REQUEST}

        existing_url_map = URLMap.query.filter_by(original=original_url).first()
        if existing_url_map:
            existing_url_map.short = create_random_url()
            db.session.commit()
            return {'data': existing_url_map.url_to_dict(), 'status': HTTPStatus.CREATED}
        url_map = URLMap(original=original_url, short=short_url)
        db.session.add(url_map)
        db.session.commit()
        return {'data': url_map.url_to_dict(), 'status': HTTPStatus.CREATED}