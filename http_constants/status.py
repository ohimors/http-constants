import warnings
from enum import Enum, IntEnum
from typing import Optional


class Series(IntEnum):
    INFORMATIONAL = 1
    SUCCESSFUL = 2
    REDIRECTION = 3
    CLIENT_ERROR = 4
    SERVER_ERROR = 5

    @classmethod
    def from_status_code(cls, status_code: int) -> 'Series':
        """
        Return the corresponding series enum of this status_code.
        :param status_code:
        """
        series_code = int(status_code / 100)
        return cls(series_code)


class HttpStatus(int, Enum):
    _ignore_ = ['Series']

    CONTINUE = (100, "Continue")
    SWITCHING_PROTOCOLS = (101, "Switching Protocols")
    PROCESSING = (102, "Processing")
    CHECKPOINT = (103, "Checkpoint")

    OK = (200, "OK")
    CREATED = (201, "Created")
    ACCEPTED = (202, "Accepted")
    NON_AUTHORITATIVE_INFORMATION = (203, "Non-Authoritative Information")
    NO_CONTENT = (204, "No Content")
    RESET_CONTENT = (205, "Reset Content")
    PARTIAL_CONTENT = (206, "Partial Content")
    MULTI_STATUS = (207, "Multi-Status")
    ALREADY_REPORTED = (208, "Already Reported")
    IM_USED = (226, "IM Used")

    MULTIPLE_CHOICES = (300, "Multiple Choices")
    MOVED_PERMANENTLY = (301, "Moved Permanently")
    FOUND = (302, "Found")
    MOVED_TEMPORARILY = (302, "Moved Temporarily")
    SEE_OTHER = (303, "See Other")
    NOT_MODIFIED = (304, "Not Modified")
    USE_PROXY = (305, "Use Proxy")
    TEMPORARY_REDIRECT = (307, "Temporary Redirect")
    PERMANENT_REDIRECT = (308, "Permanent Redirect")

    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORIZED = (401, "Unauthorized")
    PAYMENT_REQUIRED = (402, "Payment Required")
    FORBIDDEN = (403, "Forbidden")
    NOT_FOUND = (404, "Not Found")
    METHOD_NOT_ALLOWED = (405, "Method Not Allowed")
    NOT_ACCEPTABLE = (406, "Not Acceptable")
    PROXY_AUTHENTICATION_REQUIRED = (407, "Proxy Authentication Required")
    REQUEST_TIMEOUT = (408, "Request Timeout")
    CONFLICT = (409, "Conflict")
    GONE = (410, "Gone")
    LENGTH_REQUIRED = (411, "Length Required")
    PRECONDITION_FAILED = (412, "Precondition Failed")
    PAYLOAD_TOO_LARGE = (413, "Payload too large")
    URI_TOO_LONG = (414, "URI Too Long")
    UNSUPPORTED_MEDIA_TYPE = (415, "Unsupported Media Type")
    REQUESTED_RANGE_NOT_SATISFIABLE = (416, "Requested range not satifiable")
    EXPECTATION_FAILED = (417, "Exception Failed")
    I_AM_A_TEAPOT = (418, "I'm a teapot")
    UNPROCESSABLE_ENTITY = (422, "Unprocessable entity")
    LOCKED = (423, "Locked")
    FAILED_DEPENDENCY = (424, "Failed Dependency")
    UPGRADE_REQUIRED = (426, "Upgrade Required")
    PRECONDITION_REQUIRED = (428, "Precondition Required")
    TOO_MANY_REQUESTS = (429, "Too Many Requests")
    REQUEST_HEADER_FIELDS_TOO_LARGE = (431, "Request Header Fields Too Large")
    UNAVAILABLE_FOR_LEGAL_REASONS = (451, "Unavailable For Legal Reasons")

    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")
    NOT_IMPLEMENTED = (501, "Not Implemented")
    BAD_GATEWAY = (502, "Bad Gateway")
    SERVICE_UNAVAILABLE = (503, "Service Unavailable")
    GATEWAY_TIMEOUT = (504, "Gateway Timeout")
    HTTP_VERSION_NOT_SUPPORTED = (505, "HTTP Version Not Supported")
    VARIANT_ALSO_NEGOTIATES = (506, "Variant Also Negotiates")
    INSUFFICIENT_STORAGE = (507, "Insufficient Storage")
    LOOP_DETECTED = (508, "Loop Detected")
    BANDWIDTH_LIMIT_EXCEEDED = (509, "Bandwidth Limit Exceeded")
    NOT_EXTENDED = (510, "Not Extended")
    NETWORK_AUTHENTICATION_REQUIRED = (511, "Network Authentication Required")

    def __new__(cls, value: int, reason_phrase: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.reason_phrase = reason_phrase
        return obj

    def get_value(self) -> int:
        """
        Return the integer value of this status code.
        """
        warnings.warn('Use int(this_enum), or this_enum.value instead', DeprecationWarning)
        return self.value

    def get_reason_phrase(self) -> str:
        """
        Return the reason phrase of this status code.
        """
        warnings.warn('Use this_enum.reason_phrase instead', DeprecationWarning)
        return self.reason_phrase

    def series(self) -> Series:
        """
        Return the HTTP status series of this status code.
        """
        return Series.from_status_code(self.value)

    def is_1xx_informational(self):
        return self.series() == Series.INFORMATIONAL

    def is_2xx_successful(self):
        return self.series() == Series.SUCCESSFUL

    def is_3xx_redirection(self):
        return self.series() == Series.REDIRECTION

    def is_4xx_client_error(self):
        return self.series() == Series.CLIENT_ERROR

    def is_5xx_server_error(self):
        return self.series() == Series.SERVER_ERROR

    def is_error(self):
        return self.is_4xx_client_error() or self.is_5xx_server_error()

    def __str__(self):
        return '{} {}'.format(self.value, self.name)

    @classmethod
    def value_of(cls, status_code: int) -> 'HttpStatus':
        """
        Return the enum constant of this type with the specified numeric value.
        :param status_code:
        :return: HttpStatus
        """
        warnings.warn("Use HttpStatus(status_code) instead", DeprecationWarning)
        return cls(status_code)

    @classmethod
    def resolve(cls, status_code: int) -> Optional['HttpStatus']:
        """
        Resolve the given status code to an {@code HttpStatus}, if possible.
        :param status_code:
        """
        warnings.warn("Use HttpStatus(status_code) and catch ValueError instead", DeprecationWarning)
        try:
            return cls(status_code)
        except ValueError:
            return None
