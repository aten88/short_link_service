from . import db
from .models import URLMap
from .utils import create_random_url
from .validators import validate_url


class URLService:
    """ Класс с универсальными методами бизнес-логики. """

    def create_url(response_json_data):
        """ Метод создания короткой ссылки. """
        original_url = response_json_data.get('url')
        short_url = response_json_data.get('custom_id')
        if not short_url:
            short_url = create_random_url()

        if validate_url(original_url, short_url):
            raise ValueError(validate_url(original_url, short_url))

        url_map = URLMap(original=original_url, short=short_url)
        db.session.add(url_map)
        db.session.commit()
        return url_map.url_to_dict()