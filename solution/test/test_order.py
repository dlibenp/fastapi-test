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
            json={
                "orders": [
                    {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f3", "item": "New Order 1", "quantity": 2, "price": 2.5, "status": "completed", "created_at": "2023-10-07T19:41:12.294211"},
                    {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f4", "item": "New Order 2", "quantity": 4, "price": 1.5, "status": "pending", "created_at": "2023-10-07T19:41:12.294211"},
                    {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f5", "item": "New Order 3", "quantity": 2, "price": 0.5, "status": "canceled", "created_at": "2023-10-07T19:41:12.294211"},
                    {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f6", "item": "New Order 4", "quantity": 3, "price": 3.5, "status": "completed", "created_at": "2023-10-07T19:41:12.294211"}
                ]
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 15.5)
        print(response.json())


if __name__ == '__main__':
    unittest.main()
