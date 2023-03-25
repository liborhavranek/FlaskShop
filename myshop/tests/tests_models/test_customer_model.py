import unittest

from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager
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

        self.login_manager = LoginManager()
        self.login_manager.init_app(app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_costumer(self):
        self.customer = Customer()
        self.customer.username = 'test_user'
        self.customer.email = 'test@example.com'
        self.customer.phone_code = '+1'
        self.customer.phone = '123456789'
        self.customer.password = 'password'

        self.customer.faktura_first_name = 'faktura_first_name'
        self.customer.faktura_last_name = 'faktura_last_name'
        self.customer.faktura_city = 'faktura_city'
        self.customer.faktura_street = 'faktura_street'
        self.customer.faktura_zipcode = '58'

        self.customer.dodej_first_name = 'dodej_first_name'
        self.customer.dodej_last_name = 'dodej_last_name'
        self.customer.dodej_company = 'dodej_company'
        self.customer.dodej_city = 'dodej_city'
        self.customer.dodej_street = 'dodej_street'
        self.customer.dodej_zipcode = '58'
        self.customer.dodej_info = 'dodej_info'
        self.customer.dodej_phone_code = '+1'
        self.customer.dodej_phone = '987654321'

        self.customer.firma_ico = '88888888'
        self.customer.firma_dic = '9999999999'
        self.customer.firma_bank_acc = '1234567890'
        self.customer.firma_bank_number = '0800'
        self.customer.firma_spec_symbol = '55555'
        db.session.add(self.customer)
        db.session.commit()

    def test_load_login_manager(self):
        customer = Customer()
        customer.username = "test_user"
        db.session.add(customer)
        db.session.commit()

        loaded_user = self.login_manager.user_loader(customer.id)

        self.assertEqual(loaded_user, customer.id)

    def test_load_user(self):
        self.create_costumer()
        db.session.add(self.customer)
        db.session.commit()
        costumer_id = self.customer.id

        loaded_user = Customer.query.get(costumer_id)

        self.assertEqual(loaded_user, self.customer)

    def test_load_user_id(self, id=1):
        self.create_costumer()
        db.session.add(self.customer)
        db.session.commit()

        loaded_user = Customer.query.get(id)

        self.assertEqual(loaded_user, self.customer)

    def test_load_user_with_valid_id(self):
        self.create_costumer()
        db.session.add(self.customer)
        db.session.commit()
        customer_id = self.customer.id

        loaded_customer = self.login_manager.user_loader(customer_id)

        self.assertEqual(loaded_customer, customer_id)

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

    def test_costumer_have_faktura_first_name(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.faktura_first_name, 'faktura_first_name')

    def test_costumer_have_faktura_last_name(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.faktura_last_name, 'faktura_last_name')

    def test_costumer_have_faktura_city(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.faktura_city, 'faktura_city')

    def test_costumer_have_faktura_street(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.faktura_street, 'faktura_street')

    def test_costumer_have_faktura_zipcode(self):
        self.create_costumer()
        result = Customer.query.filter_by(username='test_user').first()
        self.assertEqual(result.faktura_zipcode, '58')

    def test_second_user_have_id_two(self):
        self.create_costumer()
        second_customer = Customer()
        second_customer.username = 'second_costumer'
        second_customer.email = 'second_email@example.com'
        second_customer.phone_code = '+1'
        second_customer.phone = '987654321'
        second_customer.password = 'password'
        db.session.add(second_customer)
        db.session.commit()
        result = Customer.query.filter_by(username='second_costumer').first()
        self.assertEqual(result.id, 2)

    def test_in_db_cant_be_save_user_when_the_same_username(self):
        self.create_costumer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_customer = Customer()
            second_customer.username = 'test_user'
            second_customer.email = 'test2@example.com'
            second_customer.password = 'password'
            db.session.add(second_customer)
            db.session.commit()

    def test_in_db_cant_be_save_user_when_the_same_email(self):
        self.create_costumer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_customer = Customer()
            second_customer.username = 'test_user'
            second_customer.email = 'test@example.com'
            second_customer.password = 'password'
            db.session.add(second_customer)
            db.session.commit()

    def test_in_db_can_be_save_users_when_the_same_phonenumber(self):
        self.create_costumer()
        second_customer = Customer()
        second_customer.username = 'second_customer'
        second_customer.email = 'test2@example.com'
        second_customer.phone = '123456789'
        second_customer.password = 'password'
        db.session.add(second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_password(self):
        self.create_costumer()
        second_customer = Customer()
        second_customer.username = 'second_customer'
        second_customer.email = 'test2@example.com'
        second_customer.phone = '123456789'
        second_customer.password = 'password'
        db.session.add(second_customer)
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
        self.costumer = Customer()
        self.costumer.username = 'first_user'
        self.costumer.email = 'test@example.com'
        self.costumer.phone_code = '+1'
        self.costumer.phone = '123456789'
        self.costumer.password = 'password'
        db.session.add(self.costumer)
        db.session.commit()

    def create_second_costumers(self):
        self.second_user = Customer()
        self.second_user.username = 'second_user'
        self.second_user.email = 'test2@example.com'
        self.second_user.phone_code = '+1'
        self.second_user.phone = '987654321'
        self.costumer.password = 'password'
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
