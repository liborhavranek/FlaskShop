""" Libor Havránek App Copyright (C)  21.4 2023 """

import unittest

from myshop import create_app
from myshop.forms.product_form import ProductForm
from myshop.tests.my_test_mixin import TestMixin


class TestProductForm(TestMixin, unittest.TestCase):
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
        self.form = ProductForm()
        super().setUp()

    def test_product_form_have_csrf_token_field(self):
        self.assertIn('csrf_token', self.form._fields)

    def test_product_form_have_product_name_field(self):
        self.assertIn('product_name', self.form._fields)

    def test_product_form_have_price_field(self):
        self.assertIn('price', self.form._fields)

    def test_product_form_have_discount_field(self):
        self.assertIn('discount', self.form._fields)

    def test_product_form_have_stock_field(self):
        self.assertIn('stock', self.form._fields)

    def test_product_form_have_size_field(self):
        self.assertIn('size', self.form._fields)

    def test_product_form_have_size_units_field(self):
        self.assertIn('size_units', self.form._fields)

    def test_product_form_have_weight_field(self):
        self.assertIn('weight', self.form._fields)

    def test_product_form_have_weight_units_field(self):
        self.assertIn('weight_units', self.form._fields)

    def test_product_form_have_color_field(self):
        self.assertIn('color', self.form._fields)

    def test_product_form_have_subheading_field(self):
        self.assertIn('subheading', self.form._fields)

    def test_product_form_have_description_field(self):
        self.assertIn('description', self.form._fields)

    def test_product_form_have_brand_id_field(self):
        self.assertIn('brand_id', self.form._fields)

    def test_product_form_have_category_id_field(self):
        self.assertIn('category_id', self.form._fields)

    def test_product_form_have_add_product_submit_field(self):
        self.assertIn('add_product_submit', self.form._fields)

    def test_product_form_have_edit_product_submit_field(self):
        self.assertIn('edit_product_submit', self.form._fields)

    def test_product_form_have_product_image(self):
        self.assertIn('product_image', self.form._fields)

    def test_product_form_have_additional_images(self):
        self.assertIn('additional_images', self.form._fields)

    def test_product_form_have_product_name_label(self):
        field = self.form._fields['product_name']
        self.assertEqual(field.label.text, 'Název *:')

    def test_price_label(self):
        field = self.form._fields['price']
        self.assertEqual(field.label.text, 'Cena *:')

    def test_discount_label(self):
        field = self.form._fields['discount']
        self.assertEqual(field.label.text, 'Sleva:')

    def test_stock_label(self):
        field = self.form._fields['stock']
        self.assertEqual(field.label.text, 'Počet kusů:')

    def test_size_label(self):
        field = self.form._fields['size']
        self.assertEqual(field.label.text, 'Velikost:')

    def test_size_units_label(self):
        field = self.form._fields['size_units']
        self.assertEqual(field.label.text, 'Velikostní jednotka:')

    def test_weight_label(self):
        field = self.form._fields['weight']
        self.assertEqual(field.label.text, 'Váha:')

    def test_weight_units_label(self):
        field = self.form._fields['weight_units']
        self.assertEqual(field.label.text, 'Váhová jednotka:')

    def test_color_label(self):
        field = self.form._fields['color']
        self.assertEqual(field.label.text, 'Barva:')

    def test_subheading_label(self):
        field = self.form._fields['subheading']
        self.assertEqual(field.label.text, 'Podnadpis *:')

    def test_description_label(self):
        field = self.form._fields['description']
        self.assertEqual(field.label.text, 'Popis *:')

    def test_brand_id_label(self):
        field = self.form._fields['brand_id']
        self.assertEqual(field.label.text, 'Značka:')

    def test_product_image_label(self):
        field = self.form._fields['product_image']
        self.assertEqual(field.label.text, 'Foto *:')

    def test_additional_images_label(self):
        field = self.form._fields['additional_images']
        self.assertEqual(field.label.text, 'Další fotky:')

    def test_add_product_submit_label(self):
        field = self.form._fields['add_product_submit']
        self.assertEqual(field.label.text, 'Přidat produkt')

    def test_edit_product_submit_label(self):
        field = self.form._fields['edit_product_submit']
        self.assertEqual(field.label.text, 'Upravit produkt')
