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

