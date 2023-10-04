import unittest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.getcwd())
from main import app


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_post_endpoint(self):
        response = self.client.post(
            "/solution?criterion=completed",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=[
                {"id": 1, "item": "New Order 1", "quantity": 2, "price": 2.5, "status": "completed"},
                {"id": 2, "item": "New Order 2", "quantity": 4, "price": 1.5, "status": "pending"},
                {"id": 3, "item": "New Order 3", "quantity": 2, "price": 0.5, "status": "canceled"},
                {"id": 4, "item": "New Order 4", "quantity": 3, "price": 3.5, "status": "completed"}
            ],
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 15.5)


if __name__ == '__main__':
    unittest.main()
