import unittest
from unittest.mock import patch, MagicMock
import requests
from status_script import fetch_url_status  # Imports my function

class TestFetchURLStatus(unittest.TestCase):

    @patch('status_script.requests.get')  # Patch the requests.get inside my module
    def test_fetch_url_status_success(self, mock_get):
        """Test fetch_url_status function with a 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200  # Simulate a successful response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = fetch_url_status("https://example.com")
        self.assertEqual(result, 200)  # Tests function logic

    @patch('status_script.requests.get')  # Patch requests.get
    def test_fetch_url_status_not_found(self, mock_get):
        """Test fetch_url_status function with a 404 Not Found response."""
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a 404 response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = fetch_url_status("https://google.com")
        self.assertEqual(result, 404)  # Tests function logic

    @patch('status_script.requests.get')  # Patch requests.get
    def test_fetch_url_status_connection_error(self, mock_get):
        """Test fetch_url_status function when there's a connection error."""
        mock_get.side_effect = requests.exceptions.ConnectionError  # Simulate connection error
        
        result = fetch_url_status("invalid-url")
        self.assertEqual(result, "Connection Error")  # Test function logic

    @patch('status_script.requests.get')  # Patch the requests.get
    def test_fetch_url_status_timeout(self, mock_get):
        """Test fetch_url_status function when there's a timeout."""
        mock_get.side_effect = requests.exceptions.Timeout  # Simulate timeout error
        
        result = fetch_url_status("https://example.com")
        self.assertEqual(result, "Timeout Error")  # Test function logic

    @patch('status_script.requests.get')  # Patch the requests.get
    def test_fetch_url_status_general_error(self, mock_get):
        """Test fetch_url_status function when there's a general request error."""
        mock_get.side_effect = requests.exceptions.RequestException  # Simulate a general request error
        
        result = fetch_url_status("https://example.com")
        self.assertEqual(result, "General Error")  # Tests function logic

if __name__ == "__main__":
    unittest.main()
