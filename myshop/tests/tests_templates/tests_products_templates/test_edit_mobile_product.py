""" Libor Havránek App Copyright (C)  7.5 2023 """

import unittest

from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestAllTemplates, TestMixin


class TestProductList(TestAllTemplates):
    """Test edit brand page."""

    path = "/products/edit-mobile-product/1"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestProductTemplateOnlyEditProductTemplate(TestMixin, unittest.TestCase):
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

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method="sha256")
        db.session.add(customer)
        db.session.commit()
        data = {"email": "testuser@example.com", "password": "password"}
        self.client.post("/auth/login", data=data, follow_redirects=True)

    def create_product(self):
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post(
            "/products/create-brand", data=brand_data, follow_redirects=True
        )

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post(
            "/products/create-category", data=category_data, follow_redirects=True
        )

        product_data = {
            "product_name": "iPhone 13 Pro Max 1T černá",
            "price": 47390,
            "discount": 0,
            "stock": 20,
            "display_size": 6.7,
            "display_resolution": "2160x1080",
            "operating_system": "iOS",
            "operating_memory": 6,
            "memory": 1024,
            "height": 160.8,
            "height_units": "mm",
            "width": 78.1,
            "width_units": "mm",
            "depth": 7.65,
            "depth_units": "mm",
            "weight": 238,
            "weight_units": "g",
            "battery_capacity": 4352,
            "memory_card_slot": False,
            "face_id": True,
            "touch_screen": True,
            "front_camera": 12,
            "back_camera": 12,
            "convertible": False,
            "wifi": True,
            "bluetooth": True,
            "nfc": True,
            "processor": "Apple A14 Bionic",
            "processor_cores": 6,
            "esim": True,
            "color": "cerna",
            "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
            "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
            "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí chod",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "images1.jpg",
        }

        self.client.post(
            "/products/create-mobile-product", data=product_data, follow_redirects=True
        )

    def test_edit_product_form_have_closed_form_tag(self):
        self.create_product()
        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        self.assertIn(
            b'<form method="POST" autocomplete="off" enctype=multipart/form-data>',
            response.data,
        )
        self.assertIn(b"</form>", response.data)

    def test_product_form_have_all_input_fields(self):
        self.login_user()
        fields_to_test = [
            "product_name",
            "price",
            "discount",
            "height",
            "width",
            "depth",
            "weight",
            "display_size",
            "operating_memory",
            "memory",
            "battery_capacity",
            "memory_card_slot",
            "wifi",
            "bluetooth",
            "nfc",
            "esim",
            "processor_cores",
            "face_id",
            "touch_screen",
            "convertible",
            "back_camera",
            "front_camera",
            "edit_product_submit",
        ]

        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        soup = BeautifulSoup(response.data, "html.parser")
        form_tag = soup.find("form", {"method": "POST"})
        form_input_fields = [
            input_tag["name"] for input_tag in form_tag.find_all("input")
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_input_fields)

    def test_product_form_have_all_select_fields(self):
        self.login_user()
        fields_to_test = [
            "height_units",
            "width_units",
            "depth_units",
            "weight_units",
            "display_resolution",
            "operating_system",
            "processor",
            "color",
            "brand_id",
            "category_id",
        ]

        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        soup = BeautifulSoup(response.data, "html.parser")
        form_tag = soup.find("form", {"method": "POST"})
        form_select_fields = [
            select_tag["name"] for select_tag in form_tag.find_all("select")
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_select_fields)

    def test_product_form_have_all_text_area_fields(self):
        self.login_user()
        fields_to_test = ["subheading", "description"]

        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        soup = BeautifulSoup(response.data, "html.parser")
        form_tag = soup.find("form", {"method": "POST"})
        form_select_fields = [
            select_tag["name"] for select_tag in form_tag.find_all("textarea")
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                self.assertIn(field, form_select_fields)

    def test_edit_product_form_have_all_labels(self):
        self.login_user()
        expected_labels = {
            "product_name": "Název *:",
            "subheading": "Podnadpis *:",
            "description": "Popis *:",
            "price": "Cena *:",
            "discount": "Sleva:",
            "height": "Výška:",
            "width": "Šířka:",
            "depth": "Hloubka:",
            "weight": "Váha:",
            "color": "Barva:",
            "brand_id": "Značka:",
            "category_id": "Kategorie:",
            "display_size": "Velikost displeje *:",
            "display_resolution": "Rozlišení displeje *:",
            "operating_memory": "Operační paměť *:",
            "memory": "Velikost disku *:",
            "operating_system": "Operační systém *:",
            "battery_capacity": "Kapacita baterie:",
            "memory_card_slot": "Slot na paměťovou kartu:",
            "wifi": "WiFi:",
            "bluetooth": "Bluetooth:",
            "nfc": "NFC:",
            "esim": "eSIM:",
            "processor": "Procesor:",
            "processor_cores": "Počet jader:",
            "face_id": "Face ID:",
            "touch_screen": "Dotyková obrazovka:",
            "convertible": "Ohebný:",
            "back_camera": "Zadní kamera:",
            "front_camera": "Přední kamera:",
        }
        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        soup = BeautifulSoup(response.data, "html.parser")
        form_labels = {
            label_tag["for"]: label_tag.text.strip()
            for label_tag in soup.find_all("label")
        }

        for field, label in expected_labels.items():
            with self.subTest(field=field):
                self.assertIn(label, form_labels[field])

    def test_edit_product_form_have_submit_field(self):
        self.login_user()
        response = self.client.get(
            "/products/edit-mobile-product/1", follow_redirects=True
        )
        soup = BeautifulSoup(response.data, "html.parser")

        # Check that the form contains a submit button
        submit_button = soup.find(
            "input", {"type": "submit", "value": "Upravit produkt"}
        )
        self.assertIsNotNone(submit_button)
