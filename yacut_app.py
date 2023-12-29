from datetime import datetime

from flask import Flask, render_template
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
    short = db.Column(db.String(16))
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


@app.route('/')
def my_index_view():
    form = URLForm()
    return render_template('yacut.html', form=form)


if __name__ == '__main__':
    app.run()