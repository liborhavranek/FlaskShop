""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest
from myshop import create_app
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


if __name__ == '__main__':
    unittest.main()
