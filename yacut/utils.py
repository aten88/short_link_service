import random
import string

from .constants import AUTO_MAX_LENGTH


def create_random_url():
    """ Метод создания короткой ссылки. """
    chars = string.ascii_letters + string.digits
    short_link_chars = random.choices(chars, k=AUTO_MAX_LENGTH)
    short_link = ''.join(short_link_chars)
    return short_link
