import random


def create_random_url(original_link):
    """ Метод создания короткой ссылки. """
    valid_chars = [char for char in list(original_link) if char.isalnum()]
    short_link_chars = random.choices(valid_chars, k=6)
    short_link = ''.join(short_link_chars)
    return short_link