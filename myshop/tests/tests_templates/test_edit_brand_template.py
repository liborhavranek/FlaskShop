""" Libor Havránek App Copyright (C)  17.4 2023 """
import unittest

from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestAllTemplates, TestMixin


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/edit-brand/1'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestAuthTemplateOnlyRegisterTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

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

    def test_add_brand_form_have_closed_form_tag(self):
        response = self.client.get('/products/edit-brand/1', follow_redirects=True)
        self.assertIn(b'<form method="POST">', response.data)
        self.assertIn(b'</form>', response.data)
