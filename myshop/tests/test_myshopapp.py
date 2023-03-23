import unittest
from myshop import create_app


class TestCreateApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_create_app_have_secret_key(self):
        # Test that the app has the expected configuration
        self.assertEqual(self.app.config['SECRET_KEY'], 'secret_key')

    def test_app_have_admin_blueprint(self):
        self.assertIn('admin', self.app.blueprints)

    def test_app_have_products_blueprint(self):
        self.assertIn('products', self.app.blueprints)

    def test_app_have_views_blueprint(self):
        self.assertIn('views', self.app.blueprints)

    def test_app_have_auth_blueprint(self):
        self.assertIn('auth', self.app.blueprints)

    def test_admin_blueprint_responds_to_correct_url(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_products_blueprint_responds_to_correct_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_views_blueprint_responds_to_correct_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auth_blueprint_responds_to_correct_url(self):
        response = self.client.get('/auth/')
        self.assertEqual(response.status_code, 200)

    def test_app_shutdown(self):
        # Test that the app can be shut down without errors
        with self.app.test_client() as client:
            response = client.get('/shutdown')
            self.assertEqual(response.status_code, 404)

# TODO write tests for bundless


if __name__ == '__main__':
    unittest.main()
