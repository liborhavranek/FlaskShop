""" Libor Havránek App Copyright (C)  3.4 2023 """

import unittest
from myshop import create_app
from myshop.forms.registration_form import RegistrationForm
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
        self.form = RegistrationForm()
        super().setUp()

    def test_login_form_have_email_field(self):
        self.assertIn('email', self.form._fields)

    def test_login_from_have_password_field(self):
        self.assertIn('password', self.form._fields)
