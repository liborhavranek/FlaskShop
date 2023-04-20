""" Libor Havránek App Copyright (C)  20.4 2023 """

import unittest
from myshop import create_app
from myshop.forms.category_form import CategoryForm

from myshop.tests.my_test_mixin import TestMixin


class TestCategoryForm(TestMixin, unittest.TestCase):

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
        self.form = CategoryForm()
        super().setUp()

    def test_login_form_have_email_field(self):
        self.assertIn('category_name', self.form._fields)
