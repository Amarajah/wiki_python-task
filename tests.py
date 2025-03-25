import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
import csv

csv_filename = "Task 2 - Intern.csv"

class TestCSVScript(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="URL\nhttps://example.com\nhttps://google.com\ninvalid-url\n")
    @patch("requests.get")
    def test_csv_processing(self, mock_get, mock_file):
        """Test script handles various URL responses correctly."""

        # Mock different responses
        mock_response_1 = MagicMock(status_code=200)
        mock_response_2 = MagicMock(status_code=404)

        # Simulate an exception for a broken link
        mock_get.side_effect = [mock_response_1, mock_response_2, requests.exceptions.RequestException]

        # Process the CSV
        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            urls = [row[0].strip() for row in reader]
            status_codes = []

            for url in urls:
                try:
                    response = requests.get(url)
                    status_codes.append(response.status_code)
                except requests.exceptions.RequestException:
                    status_codes.append("Error")

        # Expected output
        expected_urls = ["https://example.com", "https://google.com", "invalid-url"]
        expected_statuses = [200, 404, "Error"]

        self.assertEqual(urls, expected_urls)
        self.assertEqual(status_codes, expected_statuses)
        self.assertEqual(mock_get.call_count, 3)  # Ensure three requests were attempted


if __name__ == "__main__":
    unittest.main()
