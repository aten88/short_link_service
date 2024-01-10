from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

from .constants import MIN_LENGTH_SHORT_A, MAX_LENGHT_SHORT_A


class URLForm(FlaskForm):
    """ Форма URL-адресов. """
    original_link = TextAreaField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(MIN_LENGTH_SHORT_A, MAX_LENGHT_SHORT_A)]
    )
    submit = SubmitField('Создать')