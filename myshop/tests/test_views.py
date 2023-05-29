""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestMixin


class TestCreateApp(TestMixin, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app(config={'TESTING': True})
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.secret_key = 'test_secret_key'
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def create_category(self):
        self.data = {
            "category_name": "Mobily",
        }
        self.client.post('/products/create-category', data=self.data, follow_redirects=True)

    def create_brand(self):
        self.data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=self.data, follow_redirects=True)

    def test_view_have_set_correct_template(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertTrue(response, 'views.html')

    def test_get_products_by_category_have_set_correct_template(self):
        self.login_user()
        self.create_category()
        response = self.client.get('/category/Mobily')
        self.assertTrue(response, 'views_categories_products.html')

    def test_get_products_by_category_route_returns_correct_status_code(self):
        self.login_user()
        self.create_category()
        response = self.client.get('/category/Mobily', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_products_by_category_and_brand_have_set_correct_template(self):
        self.login_user()
        self.create_category()
        self.create_brand()
        response = self.client.get('/Mobily/Apple')
        self.assertTrue(response, 'views_categories_products.html')

    def test_get_products_by_category_and_brand_route_returns_correct_status_code(self):
        self.login_user()
        self.create_category()
        self.create_brand()
        response = self.client.get('/Mobily/Apple', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
