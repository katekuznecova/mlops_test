import unittest
import requests


data_input = {
    "data": "[0, 3, 2, 4, 5, 6, 233, 2, 5, 33, 123133, 23, 33]"
}


class TestCase(unittest.TestCase):
    def test_prediction(self):
        response = requests.get("http://localhost:5000/", json=data_input)
        response_data = response.json()
        self.assertEqual(response_data["prediction"], 15.739)

    def test_response_code(self):
        response = requests.get("http://localhost:5000/", json=data_input)
        response_data = response.json()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()