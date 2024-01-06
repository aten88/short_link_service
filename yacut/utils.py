import random
import string


def create_random_url():
    """ Метод создания короткой ссылки. """
    chars = string.ascii_letters + string.digits
    short_link_chars = random.choices(chars, k=6)
    short_link = ''.join(short_link_chars)
    return short_link