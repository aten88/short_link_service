from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class URLMap(db.Model):
    """ Модель URL- адреса. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def my_index_view():
    # urlmap = URLMap.query.get(1)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()