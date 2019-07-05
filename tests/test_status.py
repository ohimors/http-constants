import random
from unittest import TestCase

from http_constants.status import HttpStatus


class TestHttpStatus(TestCase):

    def test_enum_max_size(self):
        self.assertTrue(len(HttpStatus) is 62)

    def test_get_value(self):
        status = random.choice(list(HttpStatus))
        self.assertEqual(status.get_value(), status.value[0])

    def test_get_reason_phrase(self):
        status = random.choice(list(HttpStatus))
        self.assertEqual(status.get_reason_phrase(), status.value[1])

    def test_series(self):
        status = random.choice(list(HttpStatus))
        series = status.series()
        first_digit = int(str(status.value[0])[:1])
        self.assertEqual(series.value, first_digit)


