from flask import jsonify

from . import app
from .models import URLMap


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return jsonify({'url': url_map.original}), 200
