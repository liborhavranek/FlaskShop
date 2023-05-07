""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest
from datetime import datetime
from werkzeug.security import generate_password_hash
from myshop import create_app, db
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.customer_model import Customer
from myshop.models.product_model import Product
from myshop.products import allowed_file
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
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "image.jpg"
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
        self.create_product()
        response = self.client.get('/products/product-preview/1')
        self.assertTrue(response, 'product_page.html')

    def test_product_page_preview_returns_correct_status_code(self):
        self.create_product()
        response = self.client.get('/products/product-preview/1')
        self.assertEqual(response.status_code, 200)

    def test_allowed_file_returns_true_for_allowed_extensions(self):
        filename = "example.jpg"
        result = allowed_file(filename)
        self.assertTrue(result)

    def test_allowed_file_returns_false_for_not_allowed_extensions(self):
        filename = "example.exe"
        result = allowed_file(filename)
        self.assertFalse(result)

    def test_allowed_file_returns_false_for_missing_extension(self):
        filename = "example"
        result = allowed_file(filename)
        self.assertFalse(result)

    def test_allowed_file_returns_false_for_empty_filename(self):
        filename = ""
        result = allowed_file(filename)
        self.assertFalse(result)

    def test_product_already_registered(self):
        """
        Test that form validation fails and a flash message is shown when adding a product that already exists
        """
        self.login_user()
        with self.app.test_request_context():
            # Create a product in the database
            new_product = Product(product_name='New Product', price=10.0, description='This is a new product',
                                  subheading='This is a new product Iphone')
            db.session.add(new_product)
            db.session.commit()

        data = {
            'product_name': 'New Product',
            'price': 20.0,
            'description': 'This is a new product',
            'subheading': 'This is a new product Iphone'
        }
        response = self.client.post('/products/create-product', data=data, follow_redirects=True)
        self.assertIn(b'Tento produkt je u\xc5\xbe zaregistrov\xc3\xa1n v na\xc5\xa1\xc3\xad datab\xc3\xa1zi.',
                      response.data)

    def test_create_product_return_correct_message(self):
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "image.jpg"
        }
        response = self.client.post('/products/create-product', data=self.data, follow_redirects=True)
        self.assertIn(bytes("Produkt byl přidán.", "utf-8"), response.data)

    def test_create_product_with_image_is_saved_in_db(self):
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": 'image.jpg'
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)

        product = Product.query.filter_by(product_name='Iphonek').first()

        self.assertEqual(product.product_image, 'image.jpg')

    def test_check_product_taken(self):
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": 'image.jpg'
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)
        response = self.client.post('products/check-product', data={'product_name': 'Iphonek'})
        self.assertEqual(response.data, b'taken')

    def test_check_product_aviable(self):
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": 'image.jpg'
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)
        response = self.client.post('products/check-product', data={'product_name': 'Iphon'})
        self.assertEqual(response.data, b'available')

    def test_product_list_page_have_set_correct_template(self):
        response = self.client.get('/products/products-list')
        self.assertTrue(response, 'product_list.html')

    def test_product_list_page_returns_correct_status_code(self):
        self.create_product()
        response = self.client.get('/products/products-list')
        self.assertEqual(response.status_code, 200)


class TestEditProduct(TestMixin, unittest.TestCase):

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
        self.login_user()

        brand_data = {
            "brand_name": "Apple",
        }
        self.client.post('/products/create-brand', data=brand_data, follow_redirects=True)

        category_data = {
            "category_name": "Mobil",
        }
        self.client.post('/products/create-category', data=category_data, follow_redirects=True)

        self.data = {
            "product_name": "Iphonek",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "image.jpg"
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)

    def test_edit_product_have_correct_template(self):
        self.create_product()
        response = self.client.get('/products/edit-product/1')
        self.assertTrue(response, 'edit_product.html')

    def test_edit_product_have_correct_response(self):
        self.create_product()
        response = self.client.get('/products/edit-product/1')
        self.assertEqual(response.status_code, 200)

    def test_edit_product_edit_product_name(self):
        self.create_product()
        edit_data = {'product_name': 'Iphone 13 pro',
                     'subheading': 'Nový iPhone 13 best Iphone in the world'}
        response = self.client.post('/products/edit-product/1', data=edit_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check that the product name has been updated in the database
        product = Product.query.get(1)
        self.assertEqual(product.product_name, 'Iphone 13 pro')

    def test_edit_product_edit_can_have_the_same_name(self):
        self.create_product()
        edit_data = {'product_name': 'Iphonek',
                     'subheading': 'Nový iPhone 13 best Iphone in the world edit'}
        response = self.client.post('/products/edit-product/1', data=edit_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check that the product name has been updated in the database
        product = Product.query.get(1)
        self.assertEqual(product.product_name, 'Iphonek')

    def test_edit_product_flash_message_when_product_is_edited(self):
        self.create_product()
        edit_data = {'product_name': 'Iphonek',
                     'subheading': 'Nový iPhone 13 best Iphone in the world edit'}
        response = self.client.post('/products/edit-product/1', data=edit_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check that the product name has been updated in the database
        product = Product.query.get(1)
        self.assertIn(bytes("Produkt byl aktualizován.", "utf-8"), response.data)

    def test_edit_product_cant_be_changed_to_name_of_another_product(self):
        self.create_product()
        self.data = {
            "product_name": "Iphonek2",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "image.jpg"
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)
        edit_data = {'product_name': 'Iphonek2',
                     'subheading': 'Nový iPhone 13 best Iphone in the world edit'}
        response = self.client.post('/products/edit-product/1', data=edit_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check that the product name has been updated in the database
        product = Product.query.get(1)
        self.assertEqual(product.product_name, 'Iphonek')

    def test_edit_product_flash_message_when_try_add_the_same_name(self):
        self.create_product()
        self.data = {
            "product_name": "Iphonek2",
            "price": 999,
            "discount": 10,
            "stock": 50,
            "size": 5,
            "size_units": "in",
            "weight": 1,
            "weight_units": "kg",
            "color": "cerna",
            "subheading": "Nový iPhone 12 best Iphone in the world",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit augue vitae enim "
                           "bibendum euismod. Fusce feugiat velit elit, a finibus metus dapibus id. Nunc bibendum ac "
                           "libero sit amet convallis. Nullam semper viverra turpis, in tincidunt enim varius a.",
            "brand_id": 1,
            "category_id": 1,
            "product_image": "image.jpg"
        }
        self.client.post('/products/create-product', data=self.data, follow_redirects=True)
        edit_data = {'product_name': 'Iphonek2',
                     'subheading': 'Nový iPhone 13 best Iphone in the world edit'}
        response = self.client.post('/products/edit-product/1', data=edit_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check that the product name has been updated in the database
        product = Product.query.get(1)
        self.assertIn(bytes("Produkt s tímto názvem již existuje.", "utf-8"), response.data)

