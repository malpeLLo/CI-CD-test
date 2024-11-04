import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reverse_text(self):
        response = self.app.post('/reverse', json={'text': 'Привет, мир!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['reversed_text'], '!рим ,тевирП')

if __name__ == '__main__':
    unittest.main()