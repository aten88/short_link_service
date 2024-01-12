from flask import render_template

from . import app, db


class InvalidURLException(Exception):
    """ Кастомный класс исключения для работы с URL. """
    pass


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500