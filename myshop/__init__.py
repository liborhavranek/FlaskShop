""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path


DB_NAME = "myshop.db"
db = SQLAlchemy()

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    migrate.init_app(app, db, compare_type=True)

    from .models import Costumer
    create_database(app)



    from .admin import admin
    from .products import products
    from .views import views
    from .auth import auth

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app


def create_database(app):
    if not path.exists('myshop/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('table created')
        print('Created Database!')