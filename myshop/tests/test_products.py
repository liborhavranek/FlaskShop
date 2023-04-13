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
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.secret_key = 'test_secret_key'
        db.create_all()
        super().setUp()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

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

    def test_view_have_set_correct_template(self):
        response = self.client.get('/products')
        self.assertTrue(response, 'products.html')

    def test_products_route_returns_correct_status_code(self):
        response = self.client.get('/products', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_create_brand_return_correct_status_code(self):
        response = self.client.get('/products/create-brand', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_create_brand_return_correct_template(self):
        response = self.client.get('/products/create-brand')
        self.assertTrue(response, 'add_brand.html')

    def test_products_create_brand_return_correct_message_when_brand_created(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Značka byla vytvořena.", "utf-8"), response.data)

    def test_product_create_brand_cant_save_in_db_the_same_brand_again(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=data, follow_redirects=True)

        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Tato značka je už zaregistrována v naší databázi.", "utf-8"), response.data)

    def test_product_create_brand_cant_be_less_than_two_char(self):
        self.login_user()
        data = {
            "brand_name": "A",
        }
        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Značka musí mít alespoň dva znaky.", "utf-8"), response.data)


if __name__ == '__main__':
    unittest.main()
