from . import db
from .models import URLMap
from .validators import validate_url


class URLService:
    """ Класс с универсальными методами бизнес-логики. """

    def create_url(response_json_data):
        """ Метод создания короткой ссылки. """
        validated_long_url, validated_short_url = validate_url(response_json_data.get('url'), response_json_data.get('custom_id'))
        url_map = URLMap(original=validated_long_url, short=validated_short_url)
        db.session.add(url_map)
        db.session.commit()
        return url_map.url_to_dict()