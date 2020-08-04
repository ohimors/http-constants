import random
from unittest import TestCase

from http_constants.status import HttpStatus


class TestHttpStatus(TestCase):

    def test_enum_max_size(self):
        # MOVED_TEMPORARILY is treated as alias of FOUND
        self.assertTrue(len(HttpStatus) == 61)

    def test_get_value(self):
        status = random.choice(list(HttpStatus))
        self.assertEqual(status.get_value(), status.value)
        self.assertEqual(status.get_value(), int(status))

    def test_get_reason_phrase(self):
        status = random.choice(list(HttpStatus))
        self.assertEqual(status.get_reason_phrase(), status.reason_phrase)

    def test_series(self):
        status = random.choice(list(HttpStatus))
        series = status.series()
        first_digit = int(str(int(status))[:1])
        self.assertEqual(series.value, first_digit)

    def test_is_1xx_informational(self):
        self.assertTrue(HttpStatus.CONTINUE.is_1xx_informational())

    def test_is_2xx_successful(self):
        self.assertTrue(HttpStatus.OK.is_2xx_successful())

    def test_is_3xx_redirection(self):
        self.assertTrue(HttpStatus.PERMANENT_REDIRECT.is_3xx_redirection())

    def test_is_4xx_client_error(self):
        self.assertTrue(HttpStatus.FORBIDDEN.is_4xx_client_error())

    def test_is_5xx_server_error(self):
        self.assertTrue(HttpStatus.SERVICE_UNAVAILABLE.is_5xx_server_error())

    def test_is_error(self):
        self.assertTrue(HttpStatus.SERVICE_UNAVAILABLE.is_error())
        self.assertTrue(HttpStatus.BAD_REQUEST.is_error())
        self.assertFalse(HttpStatus.OK.is_error())

    def test_value_of(self):
        status = random.choice(list(HttpStatus))
        status_from_value = HttpStatus.value_of(status.get_value())
        self.assertEqual(status_from_value, status)
