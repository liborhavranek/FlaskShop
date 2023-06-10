""" Libor Havránek App Copyright (C)  8.6. 2023 """

import unittest

from wtforms.validators import Email, Length

from myshop import create_app
from myshop.forms.customer_order_form import CustomerOrderForm


class TestCustomerOrderForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app(config={"TESTING": True})
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        self.app.config["TESTING"] = True
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.secret_key = "test_secret_key"
        self.form = CustomerOrderForm()
        super().setUp()

    def test_order_form_exists(self):
        self.assertIsNotNone(self.form)

    def test_customer_first_name_field_exists(self):
        self.assertIn("customer_first_name", self.form._fields)

    def test_customer_last_name_field_exists(self):
        self.assertIn("customer_last_name", self.form._fields)

    def test_customer_email_field_exists(self):
        self.assertIn("customer_email", self.form._fields)

    def test_customer_phone_code_field_exists(self):
        self.assertIn("customer_phone_code", self.form._fields)

    def test_customer_phone_field_exists(self):
        self.assertIn("customer_phone", self.form._fields)

    def test_customer_city_field_exists(self):
        self.assertIn("customer_city", self.form._fields)

    def test_customer_street_field_exists(self):
        self.assertIn("customer_street", self.form._fields)

    def test_customer_zipcode_field_exists(self):
        self.assertIn("customer_zipcode", self.form._fields)

    def test_customer_info_field_exists(self):
        self.assertIn("customer_info", self.form._fields)

    def test_order_delivery_submit_field_exists(self):
        self.assertIn("order_delivery_submit", self.form._fields)

    def test_customer_first_name_required(self):
        field = self.form.customer_first_name
        self.assertTrue(field.flags.required)

    def test_customer_last_name_length_validation(self):
        field = self.form.customer_last_name
        self.assertTrue(isinstance(field.validators[0], Length))
        self.assertEqual(field.validators[0].min, 2)
        self.assertEqual(field.validators[0].max, 30)

    def test_customer_email_required(self):
        field = self.form.customer_email
        self.assertTrue(field.flags.required)

    def test_customer_email_valid_email_validation(self):
        field = self.form.customer_email
        self.assertTrue(isinstance(field.validators[1], Email))

    def test_customer_phone_code_choices(self):
        field = self.form.customer_phone_code
        self.assertEqual(field.choices, [("+420", "+420"), ("+421", "+421")])

    def test_customer_phone_required(self):
        field = self.form.customer_phone
        self.assertTrue(field.flags.required)

    def test_customer_city_required(self):
        field = self.form.customer_city
        self.assertTrue(field.flags.required)

    def test_customer_street_required(self):
        field = self.form.customer_street
        self.assertTrue(field.flags.required)

    def test_customer_zipcode_required(self):
        field = self.form.customer_zipcode
        self.assertTrue(field.flags.required)

    def test_customer_info_optional(self):
        field = self.form.customer_info
        self.assertFalse(field.flags.required)

    def test_order_delivery_submit_exists(self):
        field = self.form.order_delivery_submit
        self.assertIn(field.name, self.form._fields)
