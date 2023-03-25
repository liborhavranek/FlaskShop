""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from myshop import create_app


class TestCreateApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True

    def test_view_have_set_correct_template(self):
        with self.app.test_client() as client:
            response = client.get('/auth')
            self.assertTrue(response, 'auth.html')

    def test_auth_route_returns_auth_template(self):
        with self.app.test_client() as client:
            response = client.get('/auth', follow_redirects=True)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'text/html; charset=utf-8')
            self.assertTrue(b'<!DOCTYPE html>' in response.data)
            self.assertTrue(b'<title>Flask shop</title>' in response.data)
            self.assertTrue(b'</head>' in response.data)
            self.assertTrue(b'<body>' in response.data)
            self.assertTrue(b'</body>' in response.data)
            self.assertTrue(b'</html>' in response.data)



if __name__ == '__main__':
    unittest.main()
