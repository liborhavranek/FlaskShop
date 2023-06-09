""" Libor Havránek App Copyright (C)  8.6. 2023 """

import unittest
from myshop import create_app
from myshop.forms.add_monitor_form import MonitorForm
from myshop.tests.my_test_mixin import TestMixin


class TestMonitorForm(TestMixin, unittest.TestCase):
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
        self.form = MonitorForm()
        super().setUp()

    def test_product_form_have_csrf_token_field(self):
        self.assertIn("csrf_token", self.form._fields)

    def test_product_form_have_product_name_field(self):
        self.assertIn("product_name", self.form._fields)

    def test_product_form_have_price_field(self):
        self.assertIn("price", self.form._fields)

    def test_product_form_have_discount_field(self):
        self.assertIn("discount", self.form._fields)

    def test_product_form_have_stock_field(self):
        self.assertIn("stock", self.form._fields)

    def test_product_form_have_description_field(self):
        self.assertIn("description", self.form._fields)

    def test_product_form_have_subheading_field(self):
        self.assertIn("subheading", self.form._fields)

    def test_product_form_have_display_size_field(self):
        self.assertIn("display_size", self.form._fields)

    def test_product_form_have_display_resolution_field(self):
        self.assertIn("display_resolution", self.form._fields)

    def test_product_form_have_refresh_rate_field(self):
        self.assertIn("refresh_rate", self.form._fields)

    def test_product_form_have_response_time_field(self):
        self.assertIn("response_time", self.form._fields)

    def test_product_form_have_aspect_ratio_field(self):
        self.assertIn("aspect_ratio", self.form._fields)

    def test_product_form_have_connectivity_field(self):
        self.assertIn("connectivity", self.form._fields)

    def test_product_form_have_color_depth_field(self):
        self.assertIn("color_depth", self.form._fields)

    def test_product_form_have_curvature_field(self):
        self.assertIn("curvature", self.form._fields)

    def test_product_form_have_height_field(self):
        self.assertIn("height", self.form._fields)

    def test_product_form_have_height_units_field(self):
        self.assertIn("height_units", self.form._fields)

    def test_product_form_have_width_field(self):
        self.assertIn("width", self.form._fields)

    def test_product_form_have_width_units_field(self):
        self.assertIn("width_units", self.form._fields)

    def test_product_form_have_depth_field(self):
        self.assertIn("depth", self.form._fields)

    def test_product_form_have_depth_units_field(self):
        self.assertIn("depth_units", self.form._fields)

    def test_product_form_have_weight_field(self):
        self.assertIn("weight", self.form._fields)

    def test_product_form_have_weight_units_field(self):
        self.assertIn("weight_units", self.form._fields)

    def test_product_form_have_brand_id_field(self):
        self.assertIn("brand_id", self.form._fields)

    def test_product_form_have_category_id_field(self):
        self.assertIn("category_id", self.form._fields)

    def test_product_form_have_product_image_field(self):
        self.assertIn("product_image", self.form._fields)

    def test_product_form_have_additional_images_field(self):
        self.assertIn("additional_images", self.form._fields)

    def test_product_form_have_add_product_submit_field(self):
        self.assertIn("add_product_submit", self.form._fields)

    def test_product_form_have_edit_product_submit_field(self):
        self.assertIn("edit_product_submit", self.form._fields)
