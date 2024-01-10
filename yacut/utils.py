import random
import string
from http import HTTPStatus

from flask import jsonify


def create_random_url():
    """ Метод создания короткой ссылки. """
    chars = string.ascii_letters + string.digits
    short_link_chars = random.choices(chars, k=6)
    short_link = ''.join(short_link_chars)
    return short_link


def send_errors(list_errors):
    for error in list_errors:
        return jsonify({'message': error}), HTTPStatus.BAD_REQUEST