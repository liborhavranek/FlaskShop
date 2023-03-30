""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest
from myshop import create_app
from bs4 import BeautifulSoup
from myshop.tests.my_test_mixin import TestMixin


class TestRegisterTemplateAllTemplates(TestMixin, unittest.TestCase):
    """ Test tags and things what will have almost all templates """

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        super().setUp()

    def test_response_status(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_template_have_doctype(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertTrue(b'<!DOCTYPE html>' in response.data)

    def test_template_have_utf(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_template_have_correct_title(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertTrue(b'<title>Flask shop</title>' in response.data)

    def test_template_have_closed_body_tag(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertTrue(b'<body>' in response.data)
        self.assertTrue(b'</body>' in response.data)

    def test_template_have_close_head_tag(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertTrue(b'<head>' in response.data)
        self.assertTrue(b'</head>' in response.data)

    def test_template_have_close_html_tag(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<html lang="en">', response.data)
        self.assertTrue(b'</html>' in response.data)

    def test_template_have_set_index_css(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/index.css', response.data)

    def test_template_have_set_product_css(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/product.css', response.data)

    def test_template_have_set_register_css(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/register.css', response.data)

    def test_template_have_bootstrap(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"',
                      response.data)

    def test_template_have_bootstrap_scripts(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"',
                      response.data)

    def test_template_have_jquery_scripts(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>',
                      response.data)


class TestAuthTemplateOnlyRegisterTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        super().setUp()

    def test_register_form_have_closed_form_tag(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<form method="POST" action="/auth/register">', response.data)
        self.assertIn(b'</form>', response.data)

    def test_register_form_username_label(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(bytes('<label for="username">Přihlašovací jméno:</label>', 'utf-8'), response.data)
# label tests ^ /////////////////////////////////////////////////////////////////////////////////////

    def test_register_form_has_username_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="text" class="form-control" id="username" name="username" required>', response.data)

    def test_register_form_has_email_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="email" class="form-control" id="email" name="email" required>', response.data)

    def test_register_form_has_phone_code_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="text" class="form-control" id="phone_code" name="phone_code" required>',
                      response.data)

    def test_register_form_has_phone_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="text" class="form-control" id="phone" name="phone" required>', response.data)

    def test_register_form_has_password1_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="password" class="form-control" id="password1" name="password1" required>',
                      response.data)

    def test_register_form_has_password2_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<input type="password" class="form-control" id="password2" name="password2" required>',
                      response.data)

    def test_register_form_has_faktura_first_name_input(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(
            b'<input type="text" class="form-control" id="faktura_first_name" name="faktura_first_name" required>',
            response.data)

    def test_register_form_has_register_button(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertIn(b'<button type="submit" class="btn btn-primary">Register</button>', response.data)

    def test_register_form_have_closed_form_tags(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the form tag exists
        form_tag = soup.find('form', {'method': 'POST', 'action': '/auth/register'})
        print(form_tag)
        self.assertIsNotNone(form_tag)

        # Check that the form tag is properly closed
        self.assertFalse(form_tag.is_empty_element)

        # Check that the form contains the expected input fields
        expected_fields = ['username', 'email', 'phone_code', 'phone', 'password1', 'password2', 'faktura_first_name']
        form_input_fields = [input_tag['name'] for input_tag in form_tag.find_all('input')]
        self.assertCountEqual(expected_fields, form_input_fields)

        expected_labels = {
            'username': 'Přihlašovací jméno:',
            'email': 'Email:',
            'phone_code': 'Phone Code',
            'phone': 'Phone Number',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'faktura_first_name': 'Jméno:'
        }
        for field_name, expected_label in expected_labels.items():
            label = soup.find('label', {'for': field_name})
            self.assertIsNotNone(label)
            self.assertEqual(label.text.strip(), expected_label)

    def test_register_form_has_submit_button(self):
        response = self.client.get('/auth/register', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the form contains a submit button
        submit_button = soup.find('button', {'type': 'submit'})
        self.assertIsNotNone(submit_button)
        self.assertEqual(submit_button.text.strip(), 'Register')

    # def test_register_form_has_open_and_close_form_tags(self):
    #     response = self.client.get('/auth/register', follow_redirects=True)
    #     soup = BeautifulSoup(response.data, 'html.parser')
    #
    #     # Check that the form has an opening tag
    #     form_open_tag = soup.find('form', {'method': 'POST', 'action': '/auth/register'})
    #     self.assertIsNotNone(form_open_tag)
    #
    #     # Check that the form has a closing tag
    #     form_close_tag = form_open_tag.find_next('form')
    #     print(response.data)  # Add this line to print out the HTML response
    #     self.assertIsNotNone(form_close_tag)


if __name__ == '__main__':
    unittest.main()
