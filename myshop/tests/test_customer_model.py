import unittest

from sqlalchemy.exc import IntegrityError
from flask_login import FlaskLoginClient, login_user, current_user

from myshop import create_app, db
from myshop.models import Customer


class TestCostumerAddModel(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()
        app_context = app.app_context()
        app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_costumer(self):
        self.customer = Customer(username='test_user', email='test@example.com', phone_code='+1', phone='123456789',
                                 password='password')
        db.session.add(self.customer)
        db.session.commit()

    def test_costumer_have_username(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.username, 'test_user')

    def test_costumer_have_email(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.email, 'test@example.com')

    def test_costumer_have_phone_code(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.phone_code, '+1')

    def test_costumer_have_phone(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.phone, '123456789')

    def test_costumer_have_password(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.password, 'password')

    def test_second_user_have_id_two(self):
        self.create_costumer()
        second_costumer = Customer(username='second_costumer', email='second_email@example.com', phone_code='+1',
                                   phone='987654321', password='password')
        db.session.add(second_costumer)
        db.session.commit()
        result = Customer.query.filter_by(username='second_costumer').first()
        self.assertEqual(result.id, 2)

    def test_in_db_cant_be_save_user_when_the_same_username(self):
        self.create_costumer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_user = Customer(username='test_user', email='test2@example.com', password='password')
            db.session.add(second_user)
            db.session.commit()

    def test_in_db_cant_be_save_user_when_the_same_email(self):
        self.create_costumer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_user = Customer(username='test_user', email='test@example.com', password='password')
            db.session.add(second_user)
            db.session.commit()

    def test_in_db_can_be_save_users_when_the_same_phonenumber(self):
        self.create_costumer()
        second_user = Customer(username='second_user', email='test2@example.com', password='password',
                               phone='123456789')
        db.session.add(second_user)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_password(self):
        self.create_costumer()
        second_user = Customer(username='second_user', email='test2@example.com', password='password',
                               phone='123456789')
        db.session.add(second_user)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    # TODO after set passwords add tests to match password


class TestCostumerChangeModel(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()
        app_context = app.app_context()
        app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_costumer(self):
        self.costumer = Customer(username='first_user', email='test@example.com', phone_code='+1', phone='123456789',
                                 password='password')
        db.session.add(self.costumer)
        db.session.commit()

    def create_second_costumers(self):
        self.second_user = Customer(username='second_user', email='test2@example.com', password='password',
                                    phone='987654321')
        db.session.add(self.second_user)
        db.session.commit()

    def test_update_username_when_username_is_not_used(self):
        self.create_costumer()
        self.create_second_costumers()
        self.second_user.username = "changed_username"
        db.session.commit()
        result = self.second_user.username
        self.assertEqual(result, 'changed_username')

    def test_update_username_when_username_is_used(self):
        self.create_costumer()
        self.create_second_costumers()
        with self.assertRaises(IntegrityError):
            self.second_user.username = "first_user"
            db.session.commit()

    def test_update_username_when_email_is_not_used(self):
        self.create_costumer()
        self.create_second_costumers()
        self.second_user.email = "changed@email.com"
        db.session.commit()
        result = self.second_user.email
        self.assertEqual(result, "changed@email.com")

    def test_update_username_when_email_is_used(self):
        self.create_costumer()
        self.create_second_costumers()
        with self.assertRaises(IntegrityError):
            self.second_user.email = "test@example.com"
            db.session.commit()

    def test_update_username_when_phone_is_not_used(self):
        self.create_costumer()
        self.create_second_costumers()
        self.second_user.phone = "111999111"
        db.session.commit()
        result = self.second_user.phone
        self.assertEqual(result, "111999111")

    def test_update_username_when_phone_used(self):
        self.create_costumer()
        self.create_second_costumers()
        self.second_user.phone = "123456789"
        db.session.commit()
        result = self.second_user.phone
        self.assertEqual(result, "123456789")

    # TODO IF if it will possible add tests for change password

    def test_delete_costumer(self):
        self.create_costumer()
        db.session.delete(self.costumer)
        db.session.commit()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertIsNone(result)
