from .models import URLMap
from .constants import MAX_LENGHT_SHORT_A
from .utils import create_random_url
from .error_handlers import InvalidURLException


def validate_url(long_url, short_url=None):
    """ Метод валидации URLS. """
    if not short_url:
        short_url = create_random_url()
    if not long_url:
        raise InvalidURLException('\"url\" является обязательным полем!')
    if not (short_url.isalnum() and short_url.isascii()):
        raise InvalidURLException('Указано недопустимое имя для короткой ссылки')
    if len(short_url) > MAX_LENGHT_SHORT_A:
        raise InvalidURLException('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short_url).first():
        raise InvalidURLException('Предложенный вариант короткой ссылки уже существует.')
    return long_url, short_url