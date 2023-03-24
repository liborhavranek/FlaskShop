""" Libor Havránek App Copyright (C)  23.3 2023 """

import os
import unittest
from myshop import create_app
from webassets.filter import get_filter
from flask_assets import Environment, Bundle


class TestCreateApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def set_bundles(self):
        self.assets = Environment(self.app)
        self.bundles = {
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
        self.assets.register(self.bundles)

    def test_create_app_have_secret_key(self):
        # Test that the app has the expected configuration
        self.assertEqual(self.app.config['SECRET_KEY'], 'secret_key')

    def test_app_have_admin_blueprint(self):
        self.assertIn('admin', self.app.blueprints)

    def test_app_have_products_blueprint(self):
        self.assertIn('products', self.app.blueprints)

    def test_app_have_views_blueprint(self):
        self.assertIn('views', self.app.blueprints)

    def test_app_have_auth_blueprint(self):
        self.assertIn('auth', self.app.blueprints)

    def test_admin_blueprint_responds_to_correct_url(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_products_blueprint_responds_to_correct_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_views_blueprint_responds_to_correct_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auth_blueprint_responds_to_correct_url(self):
        response = self.client.get('/auth/')
        self.assertEqual(response.status_code, 200)

    def test_app_shutdown(self):
        # Test that the app can be shut down without errors
        with self.app.test_client() as client:
            response = client.get('/shutdown')
            self.assertEqual(response.status_code, 404)

    def test_index_style_is_registered_in_bundles(self):
        self.set_bundles()
        registered_bundles = self.assets._named_bundles.keys()
        self.assertIn("index_style", registered_bundles)

    def test_register_style_is_registered_in_bundles(self):
        self.set_bundles()
        registered_bundles = self.assets._named_bundles.keys()
        self.assertIn("register_style", registered_bundles)

    def test_product_style_is_registered_in_bundles(self):
        self.set_bundles()
        registered_bundles = self.assets._named_bundles.keys()
        self.assertIn("product_style", registered_bundles)

    def test_libsass_filter_is_used_for_index_style(self):
        self.set_bundles()
        bundle = self.assets['index_style']
        for filter_name in bundle.filters:
            if filter_name == 'libsass':
                sass_filter = get_filter(filter_name)
                self.assertIsNotNone(sass_filter)

    def test_libsass_filter_is_used_for_register_style(self):
        self.set_bundles()
        bundle = self.assets['register_style']
        for filter_name in bundle.filters:
            if filter_name == 'libsass':
                sass_filter = get_filter(filter_name)
                self.assertIsNotNone(sass_filter)

    def test_libsass_filter_is_used_for_product_style(self):
        self.set_bundles()
        bundle = self.assets['product_style']
        for filter_name in bundle.filters:
            if filter_name == 'libsass':
                sass_filter = get_filter(filter_name)
                self.assertIsNotNone(sass_filter)

    def test_sqlalchemy_database_is_set(self):
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], "sqlite:///myshop.db")

    def test_database_created_if_not_exists(self):
        db_name = "myshop.db"
        db_file_path = os.path.join(os.getcwd(), 'myshop', db_name)
        if os.path.exists(db_file_path):
            os.remove(db_file_path)
        self.assertFalse(os.path.exists(db_file_path))


if __name__ == '__main__':
    unittest.main()
