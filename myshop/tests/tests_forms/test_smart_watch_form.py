""" Libor Havránek App Copyright (C)  8.6. 2023 """

import unittest
from myshop import create_app
from myshop.forms.add_smart_watch_form import SmartWatchForm


class TestSmartWatchForm(unittest.TestCase):
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
        self.form = SmartWatchForm()
        super().setUp()

    def test_product_form_exists(self):
        self.assertIsNotNone(self.form)

    def test_product_name_field_exists(self):
        self.assertIn("product_name", self.form._fields)

    def test_price_field_exists(self):
        self.assertIn("price", self.form._fields)

    def test_discount_field_exists(self):
        self.assertIn("discount", self.form._fields)

    def test_stock_field_exists(self):
        self.assertIn("stock", self.form._fields)

    def test_description_field_exists(self):
        self.assertIn("description", self.form._fields)

    def test_subheading_field_exists(self):
        self.assertIn("subheading", self.form._fields)

    def test_display_size_field_exists(self):
        self.assertIn("display_size", self.form._fields)

    def test_display_resolution_field_exists(self):
        self.assertIn("display_resolution", self.form._fields)

    def test_operating_system_field_exists(self):
        self.assertIn("operating_system", self.form._fields)

    def test_memory_field_exists(self):
        self.assertIn("memory", self.form._fields)

    def test_battery_capacity_field_exists(self):
        self.assertIn("battery_capacity", self.form._fields)

    def test_weight_field_exists(self):
        self.assertIn("weight", self.form._fields)

    def test_weight_units_field_exists(self):
        self.assertIn("weight_units", self.form._fields)

    def test_color_field_exists(self):
        self.assertIn("color", self.form._fields)

    def test_wifi_field_exists(self):
        self.assertIn("wifi", self.form._fields)

    def test_bluetooth_field_exists(self):
        self.assertIn("bluetooth", self.form._fields)

    def test_nfc_field_exists(self):
        self.assertIn("nfc", self.form._fields)

    def test_esim_field_exists(self):
        self.assertIn("esim", self.form._fields)

    def test_heart_rate_monitor_field_exists(self):
        self.assertIn("heart_rate_monitor", self.form._fields)

    def test_step_counter_field_exists(self):
        self.assertIn("step_counter", self.form._fields)

    def test_sleep_tracker_field_exists(self):
        self.assertIn("sleep_tracker", self.form._fields)

    def test_gps_field_exists(self):
        self.assertIn("gps", self.form._fields)

    def test_water_resistant_field_exists(self):
        self.assertIn("water_resistant", self.form._fields)

    def test_music_player_field_exists(self):
        self.assertIn("music_player", self.form._fields)

    def test_voice_assistant_field_exists(self):
        self.assertIn("voice_assistant", self.form._fields)

    def test_brand_id_field_exists(self):
        self.assertIn("brand_id", self.form._fields)

    def test_category_id_field_exists(self):
        self.assertIn("category_id", self.form._fields)

    def test_product_image_field_exists(self):
        self.assertIn("product_image", self.form._fields)

    def test_additional_images_field_exists(self):
        self.assertIn("additional_images", self.form._fields)

    def test_add_product_submit_field_exists(self):
        self.assertIn("add_product_submit", self.form._fields)

    def test_edit_product_submit_field_exists(self):
        self.assertIn("edit_product_submit", self.form._fields)
