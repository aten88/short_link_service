from datetime import datetime

from flask import request

from . import db
from .constants import MAX_LENGHT_SHORT_A


class URLMap(db.Model):
    """ Модель URL-адресов. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(MAX_LENGHT_SHORT_A), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def url_to_dict(url_map):
        """ Метод преобразования данных в словарь. """
        return dict(
            url=url_map.original,
            short_link=f'{request.host_url}{url_map.short}'
        )

    def from_dict(self, data):
        """Метод преобразования данных из словаря. """
        for field in ['original', 'short', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
