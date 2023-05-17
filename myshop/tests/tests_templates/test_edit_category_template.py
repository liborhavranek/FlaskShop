""" Libor Havránek App Copyright (C)  12.5 2023 """

import unittest

from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestAllTemplates, TestMixin


class TestEditCategory(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/edit-category/1'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestAuthTemplateOnlyRegisterTemplate(TestMixin, unittest.TestCase):
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

    def create_category(self):
        self.login_user()
        data = {
            "category_name": "Notebooky",
        }
        self.client.post('/products/create-category', data=data, follow_redirects=True)

    def test_add_brand_form_have_closed_form_tag(self):
        self.create_category()
        response = self.client.get('/products/edit-brand/1', follow_redirects=True)
        self.assertIn(b'<form method="POST" autocomplete="off">', response.data)
        self.assertIn(b'</form>', response.data)

    def test_brand_form_have_all_input_fields(self):
        self.create_category()
        fields_to_test = ['category_name']
        response = self.client.get('/products/edit-category/1', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_input_fields = [input_tag['name'] for input_tag in form_tag.find_all('input')]

        for field in fields_to_test:
            with self.subTest(field=field):

                self.assertIn(field, form_input_fields)

    def test_brand_form_have_all_labels(self):
        self.create_category()
        expected_labels = {
            'category_name': 'Kategorie:',
        }
        response = self.client.get('/products/edit-category/1', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_labels = {label_tag['for']: label_tag.text.strip() for label_tag in soup.find_all('label')}

        for field, label in expected_labels.items():
            with self.subTest(field=field):
                self.assertIn(label, form_labels[field])

    def test_register_form_has_submit_button(self):
        self.create_category()
        response = self.client.get('/products/edit-category/1', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the form contains a submit button
        submit_button = soup.find('input', {'type': 'submit', 'value': 'Upravit kategorii'})
        self.assertIsNotNone(submit_button)