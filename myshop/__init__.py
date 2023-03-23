from flask import Flask
from flask_assets import Environment, Bundle


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'

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

    return app
