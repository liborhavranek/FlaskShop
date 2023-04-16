""" Libor Havránek App Copyright (C)  12.4. 2023 """

import unittest
from myshop import create_app
from bs4 import BeautifulSoup
from myshop.tests.my_test_mixin import TestMixin, TestAllTemplates


class TestLoginTemplate(TestAllTemplates):
    """Test login page."""

    path = '/auth/login'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestAuthTemplateOnlyLoginTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        super().setUp()

    def test_login_form_have_closed_form_tag(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<form method="POST">', response.data)
        self.assertIn(b'</form>', response.data)

    def test_login_form_have_all_input_fields(self):
        fields_to_test = [
            'email', 'password'
                          ]

        response = self.client.get('/auth/login', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_input_fields = [input_tag['name'] for input_tag in form_tag.find_all('input')]

        for field in fields_to_test:
            with self.subTest(field=field):

                self.assertIn(field, form_input_fields)

    def test_login_form_have_all_select_fields(self):
        fields_to_test = [
            'phone_code', 'dodej_phone_code'
        ]

        response = self.client.get('/auth/register', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_tag = soup.find('form', {'method': 'POST'})
        form_select_fields = [select_tag['name'] for select_tag in form_tag.find_all('select')]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_select_fields)

    def test_login_form_have_all_labels(self):
        expected_labels = {
            'email': 'Email:',
            'password': 'Heslo:',
        }
        response = self.client.get('/auth/login', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        form_labels = {label_tag['for']: label_tag.text.strip() for label_tag in soup.find_all('label')}

        for field, label in expected_labels.items():
            with self.subTest(field=field):
                self.assertIn(label, form_labels[field])

    def test_login_form_has_submit_button(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the form contains a submit button
        submit_button = soup.find('input', {'type': 'submit', 'value': 'Přihlásit'})
        self.assertIsNotNone(submit_button)


if __name__ == '__main__':
    unittest.main()
