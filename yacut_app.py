import random
from datetime import datetime

from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'H4#dl2Fm7'

db = SQLAlchemy(app)


class URLMap(db.Model):
    """ Модель URL-адресов. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class URLForm(FlaskForm):
    """ Форма URL-адресов. """
    original_link = TextAreaField(
        'Укажите полную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Укажите короткую ссылку',
        validators=[Length(0, 16)]
    )
    submit = SubmitField('Создать')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


def create_random_url(original_link):
    """ Метод создания короткой ссылки. """
    valid_chars = [char for char in list(original_link) if char.isalnum()]
    short_link_chars = random.choices(valid_chars, k=6)
    short_link = ''.join(short_link_chars)
    return short_link


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    """ Метод получения короткой ссылки. """
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short_form = form.custom_id.data
        if not short_form:
            short_form = create_random_url(original)
        if URLMap.query.filter_by(original=original).first() is not None:
            flash('Предложенный вариант полной ссылки уже существует.')
            redirect('/')
        elif URLMap.query.filter_by(short=short_form).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            redirect('/')
        else:
            url = URLMap(
                original=original,
                short=short_form
            )
            db.session.add(url)
            db.session.commit()
            flash(f'Ваша новая короткая ссылка: <a href="/redirect/{url.short}">{url.short}</a>')
    return render_template('yacut.html', form=form)


@app.route('/redirect/<short>')
def redirect_short_url(short):
    """ Метод перехода по короткой ссылке. """
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)


if __name__ == '__main__':
    app.run()