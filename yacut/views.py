from flask import render_template, flash, redirect

from . import app
from .models import URLMap
from .forms import URLForm
from .services import URLService
from .error_handlers import InvalidURLException


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    """ Метод получения короткой ссылки. """
    form = URLForm()
    if form.validate_on_submit():
        try:
            result = URLService.create_url({'url': form.original_link.data, 'custom_id': form.custom_id.data})
        except InvalidURLException as e:
            flash(str(e))
            return redirect('/')
        flash(f'Ваша новая ссылка готова: <a href="{result["short_link"]}">{result["short_link"]}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<short>')
def redirect_short_url(short):
    """ Метод перехода по короткой ссылке. """
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)