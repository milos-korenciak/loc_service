import unittest
import requests
import datetime
import logging

logging.basicConfig()
L = logging.getLogger()
URL = "http://localhost:8088/v1/now"
MAX_DELAY_SEC = 1.1
L.setLevel(0)


class TestCaseNowEndpoint(unittest.TestCase):
    def test_server_runnig(self):
        """Test if now endpoint is running on localhost:8088/v1/now correctly"""
        response = requests.get(URL)
        self.assertEqual(200, response.status_code, "The server is not running correctly!")  # add assertion here
        output = response.json()
        L.debug("I have got output: %s", output)
        timestamp = datetime.datetime.fromisoformat('2008-09-03T20:56:35.450686Z')
        L.debug("I have got output: %s", timestamp)
        timestamp = datetime.datetime.fromisoformat(output["now"])
        L.debug("timestamp: %s", timestamp)
        now = datetime.datetime.utcnow().replace(tzinfo=datetime.UTC)
        # test time discrepancy under
        self.assertAlmostEqual(now, timestamp, delta=datetime.timedelta(seconds=MAX_DELAY_SEC),
                               msg="Bad now time in webservice! Something misconfigured!")


if __name__ == '__main__':
    unittest.main()
