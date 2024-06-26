import random
import string

from .models import URLMap
from .constants import AUTO_MAX_LENGTH, ITERATION_VALUE


def create_random_url(max_attempts):
    """ Метод создания короткой ссылки. """
    chars = string.ascii_letters + string.digits
    attemts = 0
    while attemts < max_attempts:
        short_link_chars = random.choices(chars, k=AUTO_MAX_LENGTH)
        short_link = ''.join(short_link_chars)
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link
        attemts += ITERATION_VALUE
