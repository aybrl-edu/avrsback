from flask import Flask
from .database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ncc:nccfisa@172.31.254.21:3306/db2'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app