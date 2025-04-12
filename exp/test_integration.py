import unittest
from app import app
from io import BytesIO

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_encrypt_page_loads(self):
        response = self.client.get('/encrypt')
        self.assertEqual(response.status_code, 200)

    def test_decrypt_page_loads(self):
        response = self.client.get('/decrypt')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()