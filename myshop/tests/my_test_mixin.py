import os
import time
import unittest

from bs4 import BeautifulSoup

from myshop import create_app


class TestMixin:
    def start_test(self):
        self.start_time = time.monotonic()
        print(
            "\033[91mStarting test......................................................................\033[0m"
        )
        os.environ.pop("FLASK_ENV", None)

        if self._outcome.success:
            print(
                f"\nRunning test: {self.test_name} - "
                f"{self._testMethodName} - \033[32mPASSED\033[0m"
            )

        else:
            print(
                f"\nRunning test: {self.test_name} - "
                f"{self._testMethodName} - \033[31mFAILED\033[0m"
            )

        if self._outcome.success:
            print("\033[32m" + f"{self._testMethodName} - passed." + "\033[0m")
            print("\033[32m" + f"{self._testMethodName} - completed.\n\n" + "\033[0m")

        else:
            print("\033[31m" + f"{self._testMethodName} - failed." + "\033[0m")
            print("\033[31m" + f"{self._testMethodName} - completed.\n\n" + "\033[0m")

    def setUp(self):
        super().setUp()
        self.start_test()

    def subTest(self, **params):
        self.start_test()
        return super().subTest(**params)


class TestAllTemplates(TestMixin, unittest.TestCase):
    """Test tags and things what will have almost all templates"""

    path = None

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

    def test_response_status(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_template_have_doctype(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertTrue(b"<!DOCTYPE html>" in response.data)

    def test_template_have_utf(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_template_have_correct_title(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertTrue(b"<title>Flask shop</title>" in response.data)

    def test_template_have_closed_body_tag(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertTrue(b"<body>" in response.data)
        self.assertTrue(b"</body>" in response.data)

    def test_template_have_close_head_tag(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertTrue(b"<head>" in response.data)
        self.assertTrue(b"</head>" in response.data)

    def test_template_have_close_html_tag(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(b'<html lang="en">', response.data)
        self.assertTrue(b"</html>" in response.data)

    def test_template_have_set_index_css(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<link rel="stylesheet" type="text/css" href="/static/Gen/index.css',
            response.data,
        )

    def test_template_have_set_product_css(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<link rel="stylesheet" type="text/css" href="/static/Gen/product.css',
            response.data,
        )

    def test_template_have_set_register_css(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<link rel="stylesheet" type="text/css" href="/static/Gen/register.css',
            response.data,
        )

    def test_template_have_bootstrap(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"',
            response.data,
        )

    def test_template_have_bootstrap_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"',
            response.data,
        )

    def test_template_have_jquery_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(
            b'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>',
            response.data,
        )

    def test_template_have_myscript_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(b"myscripts.js", response.data)

    def test_template_have_registration_form_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(b"registration_form.js", response.data)

    def test_template_have_product_scripts(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        self.assertIn(b"product.js", response.data)

    def test_template_have_top_nav_bar(self):
        if self.path is None:
            self.skipTest("Skipping test because path is not defined")
        response = self.client.get(self.path, follow_redirects=True)
        soup = BeautifulSoup(response.data, "html.parser")
        navbar = soup.find("nav", class_="navbar")
        self.assertIsNotNone(navbar)
