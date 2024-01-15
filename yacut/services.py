from . import db
from .models import URLMap
from .validators import validate_url
from .utils import create_random_url
from .constants import MAX_ATTEMPTS


class URLService:
    """ Класс с универсальными методами бизнес-логики. """

    def create_url(original_link, short_link=None):
        """ Метод создания короткой ссылки. """
        if not short_link:
            short_link = create_random_url(MAX_ATTEMPTS)
            validate_url(original_link, short_link, is_generated=True)
        else:
            validate_url(original_link, short_link)
        url_map = URLMap(original=original_link, short=short_link)
        db.session.add(url_map)
        db.session.commit()
        return url_map.url_to_dict()