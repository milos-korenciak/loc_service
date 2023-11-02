import unittest
import requests
import logging
import time


logging.basicConfig()
L = logging.getLogger()
# example point in time - may be incorrect?
URL = "http://localhost:8088/v1/VIP/1"
MAX_RESPONSE_SEC = 5
L.setLevel(0)


class TestCaseVipCoordinates(unittest.TestCase):
    def test_vip_in_time(self):
        """Test if VIP endpoint is running on localhost:8088/v1/VIP/
        {point-in-time:int} correctly in given time (= 200 OR 500)."""
        response = requests.get(URL)
        start_time = time.time()
        self.assertIn(response.status_code, (200, 500),
                      "The server is not running correctly!")
        output = response.json()
        """ We should get something like this:
        {
        "source": "vip-db",
        "gpsCoords": {
                "lat": value,
                "long": value
            }}"""
        # TODO: JSONValidator schema over the output

        end_time = time.time()
        self.assertGreater(MAX_RESPONSE_SEC, end_time - start_time,
                           "We are running too long!")


if __name__ == '__main__':
    unittest.main()
