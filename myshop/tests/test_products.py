""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest
from datetime import datetime

from werkzeug.security import generate_password_hash

from myshop import create_app, db
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.customer_model import Customer
from myshop.tests.my_test_mixin import TestMixin


class TestAddBrand(TestMixin, unittest.TestCase):

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
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def test_view_have_set_correct_template(self):
        response = self.client.get('/products')
        self.assertTrue(response, 'products.html')

    def test_products_route_returns_correct_status_code(self):
        response = self.client.get('/products', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_create_brand_return_correct_status_code(self):
        response = self.client.get('/products/create-brand', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_create_brand_return_correct_template(self):
        response = self.client.get('/products/create-brand')
        self.assertTrue(response, 'add_brand.html')

    def test_products_create_brand_return_correct_message_when_brand_created(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Značka byla vytvořena.", "utf-8"), response.data)

    def test_product_create_brand_cant_save_in_db_the_same_brand_again(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=data, follow_redirects=True)

        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Tato značka je už zaregistrována v naší databázi.", "utf-8"), response.data)

    def test_product_create_brand_cant_be_less_than_two_char(self):
        self.login_user()
        data = {
            "brand_name": "A",
        }
        response = self.client.post('/products/create-brand', data=data, follow_redirects=True)
        self.assertIn(bytes("Značka musí mít alespoň dva znaky.", "utf-8"), response.data)

    def test_check_brand_aviable(self):
        self.login_user()
        response = self.client.post('products/check-brand', data={'brand_name': 'Samsung'})
        self.assertEqual(response.data, b'available')

    def test_check_brand_taken(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=data, follow_redirects=True)
        response = self.client.post('products/check-brand', data={'brand_name': 'Apple'})
        self.assertEqual(response.data, b'taken')


if __name__ == '__main__':
    unittest.main()


class TestEditBrand(TestMixin, unittest.TestCase):

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
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def create_brand(self):
        self.data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=self.data, follow_redirects=True)

    def test_products_edit_brand_return_correct_status_code(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=data, follow_redirects=True)
        response = self.client.get('/products/edit-brand/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_edit_brand_return_correct_template(self):
        self.login_user()
        data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=data, follow_redirects=True)
        response = self.client.get('/products/edit-brand/1', follow_redirects=True)
        self.assertTrue(response, 'edit_brand.html')

    def test_check_brand_aviable(self):
        self.login_user()
        response = self.client.post('products/check-brand', data={'brand_name': 'Samsung'})
        self.assertEqual(response.data, b'available')

    def test_check_brand_taken(self):
        self.login_user()
        self.create_brand()
        self.client.post('/products/edit-brand/1', data=self.data, follow_redirects=True)
        response = self.client.post('products/check-brand', data={'brand_name': 'Apple'})
        self.assertEqual(response.data, b'taken')

    def test_products_edit_brand_return_correct_message_when_the_same_brand_try_add_in_db(self):
        self.login_user()
        self.create_brand()
        response = self.client.post('/products/edit-brand/1', data=self.data, follow_redirects=True)
        self.assertIn(bytes("Tato značka je už zaregistrována v naší databázi.", "utf-8"), response.data)

    def test_products_edit_brand_return_correct_message_when_brand_is_edited(self):
        self.login_user()
        self.create_brand()
        response = self.client.post('/products/edit-brand/1', data={'brand_name': 'Samsung'}, follow_redirects=True)
        self.assertIn(bytes("Značka byla aktualizována.", "utf-8"), response.data)

    def test_product_edit_brand_cant_be_less_than_two_char(self):
        self.login_user()
        self.create_brand()
        response = self.client.post('/products/edit-brand/1', data={'brand_name': 'A'}, follow_redirects=True)
        self.assertIn(bytes("Značka musí mít alespoň dva znaky.", "utf-8"), response.data)

    def test_products_edit_brand_have_brand_edited_true_when_brand_is_edited(self):
        self.login_user()
        self.create_brand()
        self.client.post('/products/edit-brand/1', data={'brand_name': 'Samsung'}, follow_redirects=True)
        brand = Brand.query.filter_by(brand_name='Samsung').first()
        self.assertTrue(brand.edited)

    def test_products_edit_brand_have_date_edited_when_brand_is_edited(self):
        self.login_user()
        self.create_brand()
        self.client.post('/products/edit-brand/1', data={'brand_name': 'Samsung'}, follow_redirects=True)
        brand = Brand.query.filter_by(brand_name='Samsung').first()
        self.assertTrue(isinstance(brand.date_edited, datetime))

    def test_products_brand_can_be_deleted(self):
        self.login_user()
        self.create_brand()
        self.client.post('/products/delete-brand/1')
        deleted_brand = Brand.query.filter_by(id=1).first()
        self.assertIsNone(deleted_brand)


class TestAddCategory(TestMixin, unittest.TestCase):

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
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def create_category(self):
        self.login_user()
        self.data = {
            "category_name": "Mobilní telefony",
        }

    def test_create_category_have_set_correct_template(self):
        response = self.client.get('/products/create-category')
        self.assertTrue(response, 'add_category.html')

    def test_products_route_returns_correct_status_code(self):
        response = self.client.get('/products/create-category', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_create_category_return_correct_message_when_category_created(self):
        self.create_category()
        response = self.client.post('/products/create-category', data=self.data, follow_redirects=True)
        self.assertIn(bytes("Kategorie byla vytvořena.", "utf-8"), response.data)

    def test_product_create_category_cant_save_in_db_the_same_category_again(self):
        self.create_category()

        self.client.post('/products/create-category', data=self.data, follow_redirects=True)
        response = self.client.post('/products/create-category', data=self.data, follow_redirects=True)

        self.assertIn(bytes("Tato kategorie je už zaregistrována v naší databázi.", "utf-8"), response.data)

    def test_product_create_category_cant_be_less_than_two_char(self):
        self.login_user()
        data = {
            "category_name": "A",
        }
        response = self.client.post('/products/create-category', data=data, follow_redirects=True)
        self.assertIn(bytes("Kategorie musí mít alespoň dva znaky.", "utf-8"), response.data)


class TestEditCategory(TestMixin, unittest.TestCase):

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
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def create_category(self):
        self.data = {
            "category_name": "Mobilní telefony",
        }
        self.client.post('/products/create-category', data=self.data, follow_redirects=True)

    def test_products_edit_category_return_correct_status_code(self):
        self.login_user()
        data = {
            "category_name": "Mobilní telefony",
        }
        self.client.post('/products/create-category', data=data, follow_redirects=True)
        response = self.client.get('/products/edit-category/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_products_edit_brand_return_correct_template(self):
        self.login_user()
        data = {
            "category_name": "Mobilní telefony",
        }
        self.client.post('/products/create-category', data=data, follow_redirects=True)
        response = self.client.get('/products/edit-category/1', follow_redirects=True)
        self.assertTrue(response, 'edit_category.html')

    def test_products_edit_category_have_category_edited_true_when_category_is_edited(self):
        self.login_user()
        self.create_category()
        self.client.post('/products/edit-category/1', data={'category_name': 'Nnotebooky'}, follow_redirects=True)
        category = Category.query.filter_by(id=1).first()
        self.assertTrue(category.edited)

    def test_products_edit_brand_have_date_edited_when_brand_is_edited(self):
        self.login_user()
        self.create_category()
        self.client.post('/products/edit-category/1', data={'category_name': 'Nnotebooky'}, follow_redirects=True)
        category = Category.query.filter_by(id=1).first()
        self.assertTrue(isinstance(category.date_edited, datetime))

    def test_check_category_aviable(self):
        self.login_user()
        response = self.client.post('products/check-category', data={'category_name': 'Notebooky'})
        self.assertEqual(response.data, b'available')

    def test_check_category_taken(self):
        self.login_user()
        self.create_category()
        self.client.post('/products/edit-category/1', data=self.data, follow_redirects=True)
        response = self.client.post('products/check-category', data={'category_name': 'Mobilní telefony'})
        self.assertEqual(response.data, b'taken')

    def test_products_category_can_be_deleted(self):
        self.login_user()
        self.create_category()
        self.client.post('/products/delete-category/1')
        deleted_category = Category.query.filter_by(id=1).first()
        self.assertIsNone(deleted_category)


class TestAddProduct(TestMixin, unittest.TestCase):

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
        super().setUp()

    def login_user(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        self.client.post('/auth/login', data=data, follow_redirects=True)

    def create_product(self):
        self.data = {
            "product_name": "Iphone",
            "price": 999.99,
            "discount": 10,
            "stock": 50,
            "size": 5.0,
            "size_units": "in",
            "weight": 0.5,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 2
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)

    def test_create_product_have_set_correct_template(self):
        response = self.client.get('/products/create-product')
        self.assertTrue(response, 'add_product.html')

    def test_products_route_returns_correct_status_code(self):
        response = self.client.get('/products/create-product', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_product_return_correct_message_when_short_name(self):
        self.login_user()
        data = {
            "product_name": "I",
            "price": 999.99,
            "discount": 10,
            "stock": 50,
            "size": 5.0,
            "size_units": "in",
            "weight": 0.5,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 2
        }
        response = self.client.post('/products/create-product', data=data, follow_redirects=True)
        self.assertIn(bytes("Produkt musí mít alespoň dva znaky.", "utf-8"), response.data)

    def test_create_product_return_correct_message_when_price_is_zero(self):
        self.login_user()
        data = {
            "product_name": "Iphone",
            "price": 0,
            "discount": 10,
            "stock": 50,
            "size": 5.0,
            "size_units": "in",
            "weight": 0.5,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 2
        }
        response = self.client.post('/products/create-product', data=data, follow_redirects=True)
        self.assertIn(bytes("Cena produktu nemůže být nulová.", "utf-8"), response.data)

    def test_create_product_return_correct_message_when_description_is_short(self):
        self.login_user()
        data = {
            "product_name": "Iphone",
            "price": 20,
            "discount": 10,
            "stock": 50,
            "size": 5.0,
            "size_units": "in",
            "weight": 0.5,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum",
            "brand_id": 1,
            "category_id": 2
        }
        response = self.client.post('/products/create-product', data=data, follow_redirects=True)
        self.assertIn(bytes("Popis musí mít alespoň padesát znaků.", "utf-8"), response.data)

    def test_create_product_return_correct_message_when_subheading_is_short(self):
        self.login_user()
        data = {
            "product_name": "Iphone",
            "price": 20,
            "discount": 10,
            "stock": 50,
            "size": 5.0,
            "size_units": "in",
            "weight": 0.5,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 2
        }
        response = self.client.post('/products/create-product', data=data, follow_redirects=True)
        self.assertIn(bytes("Podnadpis musí mít alespoň dvacet znaků.", "utf-8"), response.data)

    def test_product_page_preview_have_set_correct_template(self):
        self.login_user()
        self.create_product()
        response = self.client.get('/products/product-preview/1')
        self.assertTrue(response, 'product_page.html')

    def test_product_page_preview_returns_correct_status_code(self):
        self.login_user()
        self.create_product()
        response = self.client.get('/products/product-preview/1')
        self.assertEqual(response.status_code, 200)

# TODO Thinking how write test for url redirect and write tests for create product message
# TODO add test for message when product ahve the same name
