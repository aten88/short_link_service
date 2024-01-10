from flask import render_template, flash, redirect, request

from . import app, db
from .models import URLMap
from .forms import URLForm
from .services import URLService


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    """ Метод получения короткой ссылки. """
    form = URLForm()
    if form.validate_on_submit():
        data = {'url': form.original_link.data, 'custom_id': form.custom_id.data}
        original_url = form.original_link.data
        short_url = URLService.create_short_url(data)
        if URLService.check_for_validate(original_url, short_url):
            for error in URLService.check_for_validate(original_url, short_url):
                flash(error)
            return redirect('/')
        url = URLMap(original=original_url, short=short_url)
        db.session.add(url)
        db.session.commit()
        flash(f'Ваша новая ссылка готова: <a href="{request.host_url}{url.short}">{request.host_url}{url.short}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<short>')
def redirect_short_url(short):
    """ Метод перехода по короткой ссылке. """
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)