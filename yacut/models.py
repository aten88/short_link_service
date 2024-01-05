from datetime import datetime

from . import db


class URLMap(db.Model):
    """ Модель URL-адресов. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def url_to_dict(url_map):
        """ Метод преобразования данных в словарь. """
        return dict(
            id=url_map.id,
            original=url_map.original,
            short=url_map.short,
            timestamp=url_map.timestamp
        )

    def from_dict(self, data):
        """Метод преобразования данных из словаря. """
        for field in ['original', 'short', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
