import unittest
from fastapi.testclient import TestClient
from solution.main import app

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_post_endpoint(self):
        response = self.client.post("/solution")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json(), {"Hello": "World"})

if __name__ == '__main__':
    unittest.main()