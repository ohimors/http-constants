from unittest import TestCase

from http_constants.status import HttpStatus


class TestHttpStatus(TestCase):

    def test_generic(self):

        for item in HttpStatus:
            print(item)
