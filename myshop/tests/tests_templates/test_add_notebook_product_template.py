""" Libor Havránek App Copyright (C)  17.5. 2023 """

import unittest

from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestAllTemplates, TestMixin


class TestAddNotebookProduct(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/create-notebook-product'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestNotebookProductTemplateOnlyAddProductTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

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

    def test_add_product_form_have_closed_form_tag(self):
        self.login_user()
        response = self.client.get('/products/create-notebook-product', follow_redirects=True)
        self.assertIn(b'<form method="POST" autocomplete="off" enctype=multipart/form-data>', response.data)
        self.assertIn(b'</form>', response.data)

    def test_product_form_have_all_input_fields(self):
        self.login_user()
        fields_to_test = [
            'product_name', 'price', 'discount', 'stock',
                          ]

        response = self.client.get('/products/create-notebook-product', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_input_fields = [input_tag['name'] for input_tag in form_tag.find_all('input')]

        for field in fields_to_test:
            with self.subTest(field=field):

                self.assertIn(field, form_input_fields)

    def test_product_form_have_all_text_area_fields(self):
        self.login_user()
        fields_to_test = [
            "subheading", "description"
        ]

        response = self.client.get('/products/create-notebook-product', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_select_fields = [select_tag['name'] for select_tag in form_tag.find_all('textarea')]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_select_fields)

