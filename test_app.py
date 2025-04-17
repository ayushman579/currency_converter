import unittest
from unittest.mock import patch
import requests
import app  # This is the Streamlit app you wrote


class TestCurrencyConverter(unittest.TestCase):

    @patch("app.requests.get")
    def test_get_exchange_rate_success(self, mock_get):
        # Mock a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": "success",
            "conversion_rate": 0.85
        }

        # Test the conversion logic
        result = app.get_exchange_rate("USD", "EUR", 100)
        self.assertEqual(result, 85.0)

    @patch("app.requests.get")
    def test_get_exchange_rate_failure(self, mock_get):
        # Mock a failed API response
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {
            "result": "error",
            "error": "Invalid API request"
        }

        # Test failure case
        result = app.get_exchange_rate("USD", "EUR", 100)
        self.assertIsNone(result)

    @patch("app.requests.get")
    def test_get_exchange_rate_api_error(self, mock_get):
        # Simulate an exception thrown during the API call
        mock_get.side_effect = requests.exceptions.RequestException("API request failed")

        result = app.get_exchange_rate("USD", "EUR", 100)
        self.assertIsNone(result)


@patch("app.requests.get")
def test_get_exchange_rate_success(self, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "result": "success",
        "conversion_rate": 0.85
    }

    # Assuming 100 USD -> EUR at rate 0.85 = 85.0
    result = app.get_exchange_rate("USD", "EUR", 100)

    # ✅ Assert the expected result
    self.assertEqual(result, 85.0)


if __name__ == "__main__":
    unittest.main()
