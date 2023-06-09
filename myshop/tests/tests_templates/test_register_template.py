""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest
from myshop import create_app
from bs4 import BeautifulSoup
from myshop.tests.my_test_mixin import TestMixin, TestAllTemplates


class TestLoginTemplate(TestAllTemplates):
    """Test register page."""

    path = "/auth/register"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_template_have_event_listener_form_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get("/auth/register", follow_redirects=True)
        self.assertIn(b"event_listener.js", response.data)


class TestAuthTemplateOnlyRegisterTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

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
        super().setUp()

    def test_register_form_have_closed_form_tag(self):
        response = self.client.get("/auth/register", follow_redirects=True)
        self.assertIn(b'<form method="POST">', response.data)
        self.assertIn(b"</form>", response.data)

    def test_register_form_have_all_input_fields(self):
        fields_to_test = [
            "username",
            "email",
            "phone",
            "password",
            "confirm_password",
            "faktura_first_name",
            "faktura_last_name",
            "faktura_city",
            "faktura_street",
            "faktura_zipcode",
            "dodej_first_name",
            "dodej_last_name",
            "dodej_company",
            "dodej_city",
            "dodej_street",
            "dodej_zipcode",
            "dodej_info",
            "dodej_phone",
            "firma_ico",
            "firma_dic",
            "firma_bank_acc",
            "firma_bank_number",
            "firma_spec_symbol",
        ]

        response = self.client.get("/auth/register", follow_redirects=True)
        soup = BeautifulSoup(response.data, "html.parser")
        form_tag = soup.find("form", {"method": "POST"})
        form_input_fields = [
            input_tag["name"] for input_tag in form_tag.find_all("input")
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_input_fields)

    def test_register_form_have_all_select_fields(self):
        fields_to_test = ["phone_code", "dodej_phone_code"]

        response = self.client.get("/auth/register", follow_redirects=True)
        soup = BeautifulSoup(response.data, "html.parser")
        form_tag = soup.find("form", {"method": "POST"})
        form_select_fields = [
            select_tag["name"] for select_tag in form_tag.find_all("select")
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_select_fields)

    def test_register_form_have_all_labels(self):
        expected_labels = {
            "username": "Přihlašovací jméno:",
            "email": "Email:",
            "phone": "Telefon:",
            "password": "Heslo:",
            "confirm_password": "Potvrdit heslo:",
            "faktura_first_name": "Jméno:",
            "faktura_last_name": "Příjmení:",
            "faktura_city": "Město:",
            "faktura_street": "Ulice:",
            "faktura_zipcode": "PSČ:",
            "dodej_first_name": "Jméno:",
            "dodej_last_name": "Příjmení:",
            "dodej_company": "Firma:",
            "dodej_city": "Město:",
            "dodej_street": "Ulice:",
            "dodej_zipcode": "PSČ:",
            "dodej_info": "Info(např. patro):",
            "dodej_phone": "Telefon:",
            "firma_ico": "IČO:",
            "firma_dic": "DIČ:",
            "firma_bank_acc": "Číslo účtu:",
            "firma_bank_number": "Kód banky:",
            "firma_spec_symbol": "Specifický symbol:",
        }
        response = self.client.get("/auth/register", follow_redirects=True)
        soup = BeautifulSoup(response.data, "html.parser")
        form_labels = {
            label_tag["for"]: label_tag.text.strip()
            for label_tag in soup.find_all("label")
        }

        for field, label in expected_labels.items():
            with self.subTest(field=field):
                self.assertIn(label, form_labels[field])

    def test_register_form_has_submit_button(self):
        response = self.client.get("/auth/register", follow_redirects=True)
        soup = BeautifulSoup(response.data, "html.parser")

        # Check that the form contains a submit button
        submit_button = soup.find("input", {"type": "submit", "value": "Registrovat"})
        self.assertIsNotNone(submit_button)


if __name__ == "__main__":
    unittest.main()
