""" Libor Havránek App Copyright (C)  3.4 2023 """

import unittest
from myshop import create_app
from myshop.forms.forms import RegistrationForm
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

    def test_registration_form_have_username_field(self):
        self.assertIn('username', self.form._fields)

    def test_registration_form_have_email_field(self):
        self.assertIn('email', self.form._fields)

    def test_registration_form_have_phone_code_field(self):
        self.assertIn('phone_code', self.form._fields)

    def test_registration_from_have_phone_field(self):
        self.assertIn('phone', self.form._fields)

    def test_registration_from_have_password_field(self):
        self.assertIn('password', self.form._fields)

    def test_registration_from_have_confirm_password_field(self):
        self.assertIn('confirm_password', self.form._fields)

    def test_registration_form_have_faktura_first_name_field(self):
        self.assertIn('faktura_first_name', self.form._fields)

    def test_registration_form_have_faktura_last_name_field(self):
        self.assertIn('faktura_last_name', self.form._fields)

    def test_registration_form_have_faktura_city_field(self):
        self.assertIn('faktura_city', self.form._fields)

    def test_registration_form_have_faktura_street_field(self):
        self.assertIn('faktura_street', self.form._fields)

    def test_registration_form_have_faktura_zipcode_field(self):
        self.assertIn('faktura_zipcode', self.form._fields)

    def test_registration_form_have_dodej_first_name_field(self):
        self.assertIn('dodej_first_name', self.form._fields)

    def test_registration_form_have_dodej_last_name_field(self):
        self.assertIn('dodej_last_name', self.form._fields)

    def test_registration_form_have_dodej_companyfield(self):
        self.assertIn('dodej_company', self.form._fields)

    def test_registration_form_have_dodej_city_field(self):
        self.assertIn('dodej_city', self.form._fields)

    def test_registration_form_have_dodej_street_field(self):
        self.assertIn('dodej_street', self.form._fields)

    def test_registration_form_have_dodej_zipcode_field(self):
        self.assertIn('dodej_zipcode', self.form._fields)

    def test_registration_form_have_dodej_info_field(self):
        self.assertIn('dodej_info', self.form._fields)

    def test_registration_form_have_dodej_phone_code_field(self):
        self.assertIn('dodej_phone_code', self.form._fields)

    def test_registration_form_have_dodej_phone_field(self):
        self.assertIn('dodej_phone', self.form._fields)

    def test_registration_form_have_firma_ico_field(self):
        self.assertIn('firma_ico', self.form._fields)

    def test_registration_form_have_firma_dic_field(self):
        self.assertIn('firma_dic', self.form._fields)

    def test_registration_form_have_firma_bank_acc_field(self):
        self.assertIn('firma_bank_acc', self.form._fields)

    def test_registration_form_have_firma_bank_number_field(self):
        self.assertIn('firma_bank_number', self.form._fields)

    def test_registration_form_have_firma_spec_symbol_field(self):
        self.assertIn('firma_spec_symbol', self.form._fields)

    def test_registration_form_have_submit_field(self):
        self.assertIn('submit', self.form._fields)
