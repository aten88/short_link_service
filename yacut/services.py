from sqlalchemy.exc import SQLAlchemyError

from . import db
from .models import URLMap
from .constants import MAX_LENGHT_SHORT_A
from .utils import create_random_url


class URLService:
    """ Класс с универсальными методами бизнес-логики. """

    def create_short_url(data):
        """ Метод создания короткой ссылки. """
        short_url = data.get('custom_id')
        if not short_url:
            short_url = create_random_url()
        return short_url

    def check_for_validate(original_url, short_url=None):
        """ Метод валидации ссылок. """
        errors = []
        if len(short_url) > MAX_LENGHT_SHORT_A:
            errors.append('Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=short_url).first():
            errors.append('Предложенный вариант короткой ссылки уже существует.')
        if not (short_url.isalnum() and short_url.isascii()):
            errors.append('Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(original=original_url).first():
            errors.append('Предложенный вариант полной ссылки уже существует.')
        return errors

    def create_record(object):
        """ Метод создания записи в БД. """
        errors = []
        try:
            db.session.add(object)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            errors.append('\"url\" является обязательным полем!')
            return errors
