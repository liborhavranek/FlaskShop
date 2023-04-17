""" Libor Havránek App Copyright (C)  23.3 2023 """

import warnings
from os import path
from flask import Flask
from datetime import datetime
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

DB_NAME = "myshop.db"
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'

    if app.config['TESTING']:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    migrate.init_app(app, db, compare_type=True)

    warnings.simplefilter("ignore", category=DeprecationWarning)

    from myshop.models.customer_model import Customer
    from myshop.models.brand_model import Brand

    create_database(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(id)

    assets = Environment(app)
    bundles = {  # define nested Bundle
        'index_style': Bundle(
            'SCSS/index.scss',
            filters='libsass',
            output='Gen/index.css',
        ),
        'register_style': Bundle(
            'SCSS/register.scss',
            filters='libsass',
            output='Gen/register.css',
        ),
        'product_style': Bundle(
            'SCSS/product.scss',
            filters='libsass',
            output='Gen/product.css',
        )
    }
    assets.register(bundles)

    from .admin import admin
    from .products import products
    from .views import views
    from .auth import auth

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    @app.template_filter('custom_date_format')
    def custom_date_format(date):
        return datetime.strftime(date, '%H hod : %M min : %S sec,   %m.%d.  %Y ')

    return app


def create_database(app):
    if not path.exists('myshop/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('db created')
