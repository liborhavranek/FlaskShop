""" Libor Havránek App Copyright (C)  13.4 2023 """

import unittest

from werkzeug.security import generate_password_hash

from myshop import create_app, db
from bs4 import BeautifulSoup

from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestMixin, TestAllTemplates


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/create-brand'

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

    def test_add_brand_form_have_closed_form_tag(self):
        self.login_user()
        response = self.client.get('/products/create-brand', follow_redirects=True)
        self.assertIn(b'<form method="POST" autocomplete="off">', response.data)
        self.assertIn(b'</form>', response.data)

    def test_brand_form_have_all_input_fields(self):
        self.login_user()
        fields_to_test = ['brand_name']
        response = self.client.get('/products/create-brand', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_input_fields = [input_tag['name'] for input_tag in form_tag.find_all('input')]

        for field in fields_to_test:
            with self.subTest(field=field):

                self.assertIn(field, form_input_fields)

    def test_brand_form_have_all_labels(self):
        self.login_user()
        expected_labels = {
            'brand_name': 'Značka:',
        }
        response = self.client.get('/products/create-brand', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_labels = {label_tag['for']: label_tag.text.strip() for label_tag in soup.find_all('label')}

        for field, label in expected_labels.items():
            with self.subTest(field=field):
                self.assertIn(label, form_labels[field])

    def test_register_form_has_submit_button(self):
        self.login_user()
        response = self.client.get('/products/create-brand', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the form contains a submit button
        submit_button = soup.find('input', {'type': 'submit', 'value': 'Přidat značku'})
        self.assertIsNotNone(submit_button)


if __name__ == '__main__':
    unittest.main()
