""" Libor Havránek App Copyright (C)  12.4. 2023 """

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
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_template_have_doctype(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertTrue(b'<!DOCTYPE html>' in response.data)

    def test_template_have_utf(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_template_have_correct_title(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertTrue(b'<title>Flask shop</title>' in response.data)

    def test_template_have_closed_body_tag(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertTrue(b'<body>' in response.data)
        self.assertTrue(b'</body>' in response.data)

    def test_template_have_close_head_tag(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertTrue(b'<head>' in response.data)
        self.assertTrue(b'</head>' in response.data)

    def test_template_have_close_html_tag(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<html lang="en">', response.data)
        self.assertTrue(b'</html>' in response.data)

    def test_template_have_set_index_css(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/index.css', response.data)

    def test_template_have_set_product_css(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/product.css', response.data)

    def test_template_have_set_register_css(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<link rel="stylesheet" type="text/css" href="/static/Gen/register.css', response.data)

    def test_template_have_bootstrap(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"',
                      response.data)

    def test_template_have_bootstrap_scripts(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"',
                      response.data)

    def test_template_have_jquery_scripts(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertIn(b'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>',
                      response.data)

    def test_template_have_top_nav_bar(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        navbar = soup.find('nav', class_='navbar')
        self.assertIsNotNone(navbar)
