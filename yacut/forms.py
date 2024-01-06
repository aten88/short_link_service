from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class URLForm(FlaskForm):
    """ Форма URL-адресов. """
    original_link = TextAreaField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(0, 16)]
    )
    submit = SubmitField('Создать')