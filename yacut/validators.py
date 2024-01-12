from .models import URLMap
from .constants import MAX_LENGHT_SHORT_A


def validate_url(long_url, short_url):
    """ Метод валидации URLS. """
    if not long_url:
        return '\"url\" является обязательным полем!'
    if not (short_url.isalnum() and short_url.isascii()):
        return 'Указано недопустимое имя для короткой ссылки'
    if len(short_url) > MAX_LENGHT_SHORT_A:
        return 'Указано недопустимое имя для короткой ссылки'
    if URLMap.query.filter_by(short=short_url).first():
        return 'Предложенный вариант короткой ссылки уже существует.'
