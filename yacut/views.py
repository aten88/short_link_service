from flask import render_template, flash, redirect

from . import app, db
from .models import URLMap
from .forms import URLForm
from .utils import create_random_url


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
            flash('"Предложенный вариант короткой ссылки уже существует."')
            redirect('/')
        else:
            url = URLMap(
                original=original,
                short=short_form
            )
            db.session.add(url)
            db.session.commit()
            flash(f'Ваша новая ссылка готова: <a href="/{url.short}">http://127.0.0.1:5000/{url.short}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<short>')
def redirect_short_url(short):
    """ Метод перехода по короткой ссылке. """
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)