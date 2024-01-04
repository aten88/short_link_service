from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


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