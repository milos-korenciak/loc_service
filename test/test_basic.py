import unittest
import requests


URL = "http://localhost:8088/"


class BaseTestCase(unittest.TestCase):
    def test_server_runnig(self):
        """Test if the server is running on localhost:8088"""
        response = requests.get(URL)
        self.assertEqual(200, response.status_code, "The server is not running correctly!")  # add assertion here


if __name__ == '__main__':
    unittest.main()
