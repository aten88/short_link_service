from flask import render_template, flash, redirect, request

from . import app
from .models import URLMap
from .forms import URLForm
from .services import URLService


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    """ Метод получения короткой ссылки. """
    form = URLForm()
    if form.validate_on_submit():
        original_url = form.original_link.data
        short_url = URLService.create_short_url({'custom_id': form.custom_id.data})
        if URLService.validate_url(original_url, short_url):
            for error in URLService.validate_url(original_url, short_url):
                flash(error)
            return redirect('/')
        url = URLMap(original=original_url, short=short_url)
        if URLService.create_record(url):
            for error in URLService.create_record(url):
                flash(error)
            return redirect('/')
        flash(f'Ваша новая ссылка готова: <a href="{request.host_url}{url.short}">{request.host_url}{url.short}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<short>')
def redirect_short_url(short):
    """ Метод перехода по короткой ссылке. """
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)