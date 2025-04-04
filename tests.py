import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
import csv
from status_script import fetch_url_status  # Importing my function

csv_filename = "Task 2 - Intern.csv"

class TestCSVScript(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="URL\nhttps://example.com\nhttps://google.com\ninvalid-url\n")
    @patch("requests.get")
    def test_fetch_url_status(self, mock_get, mock_file):
        """Test fetch_url_status function with different URL scenarios."""

        # Mock different responses
        mock_response_1 = MagicMock(status_code=200)
        mock_response_2 = MagicMock(status_code=404)

        # Simulate exceptions
        mock_get.side_effect = [mock_response_1, mock_response_2, requests.exceptions.ConnectionError]

        # Expected outputs
        expected_results = {
            "https://example.com": 200,
            "https://google.com": 404,
            "invalid-url": "Connection Error"
        }

        # Validate function behavior
        for url, expected_status in expected_results.items():
            with self.subTest(url=url):
                self.assertEqual(fetch_url_status(url), expected_status)

        # Ensure three requests were attempted
        self.assertEqual(mock_get.call_count, 3)

if __name__ == "__main__":
    unittest.main()
