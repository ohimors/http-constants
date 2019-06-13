import string
from enum import Enum


class HttpStatus(Enum):
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
    FAILED_DEPENDENCY = (424
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    BANDWIDTH_LIMIT_EXCEEDED = 509
    NOT_EXTENDED = 510
    NETWORK_AUTHENTICATION_REQUIRED = 511

    _value = None
    _reason_phrase = None

    def __init__(self, value: int, reason_phrase: string):
        self._value = value
        self._reason_phrase = reason_phrase

    def get_value(self):
        return self._value

    def get_reason_phrase(self):
        return self._reason_phrase

    class Series(Enum):
        INFORMATIONAL = 1
        SUCCESSFUL = 2
        REDIRECTION = 3
        CLIENT_ERROR = 4
        SERVER_ERROR = 5

        _value = None

        def __init__(self, value: int):
            self._value = value

        def get_value(self):
            return self._value

        @classmethod
        def value_of(cls, http_status):
            """
            Return the enum constant of this type with the corresponding series.
            :parameter: status a standard HTTP status enum value
            :return: the enum constant of this type with the corresponding series
            :raises: ValueError if this enum has no corresponding constant
            """
            return cls.value_of(http_status.value)

        @classmethod
        def value_of(cls, status_code: int):
            series = cls.resolve(status_code)
            if not series:
                raise ValueError(f"No matching constant for [{status_code}]")
            return series

        @classmethod
        def resolve(cls, status_code: int):
            series_code = status_code / 100;
            for series in cls:
                if series.value == series_code:
                    return series
            return None
