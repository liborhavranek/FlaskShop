""" Libor Havránek App Copyright (C)  13.4 2023 """

import unittest
from myshop import create_app
from myshop.forms.brand_form import BrandForm

from myshop.tests.my_test_mixin import TestMixin


class TestRegistrationForm(TestMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()
        self.app.application.config['WTF_CSRF_ENABLED'] = False
        app_context = app.app_context()
        app_context.push()
        self.form = BrandForm()
        super().setUp()

    def test_login_form_have_email_field(self):
        self.assertIn('brand_name', self.form._fields)
