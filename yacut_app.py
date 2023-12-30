from datetime import datetime

from flask import Flask, render_template, flash
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
    """ Модель URL- адреса. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class URLForm(FlaskForm):
    original_link = TextAreaField(
        'Укажите полную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Укажите короткую ссылку',
        validators=[Length(1, 6)]
    )
    submit = SubmitField('Создать')


@app.route('/', methods=['GET', 'POST'])
def my_index_view():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if URLMap.query.filter_by(original=original).first() is not None:
            flash('Такой вариант полной ссылки уже существует в БД')
            return render_template('yacut.html', form=form)
        elif URLMap.query.filter_by(short=short).first() is not None:
            flash('Такой вариант короткой ссылки уже существует в БД')
            return render_template('yacut.html', form=form)
        else:
            flash(f'Ваша новая ссылка готова: <a href="{short}">{short}</a>')
            url = URLMap(
                original=form.original_link.data,
                short=form.custom_id.data
            )
            db.session.add(url)
            db.session.commit()
    return render_template('yacut.html', form=form)


if __name__ == '__main__':
    app.run()