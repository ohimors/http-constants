# Http Constants

A set of constants for HTTP statuses and headers.

## Installation

You can install Http Constants from [PyPI](https://pypi.org/project/http-constants/):

    pip install http-constants

The library is supported on Python 3.7+.

## Usage

### Headers

```py
from http_constants.headers import HttpHeaders

>>> HttpHeaders.ACCEPT
'Accept'

>>> HttpHeaders.CONTENT_TYPE_VALUES.json
'application/json'
```

### Statuses

```py
from http_constants.status import HttpStatus

>>> HttpStatus.SERVICE_UNAVAILABLE
<HttpStatus.SERVICE_UNAVAILABLE: (503, 'Service Unavailable')>

>>> HttpStatus.SERVICE_UNAVAILABLE.value
503

>>> int(HttpStatus.SERVICE_UNAVAILABLE)
503

>>> HttpStatus.SERVICE_UNAVAILABLE.reason_phrase
'Service Unavailable'

>>> str(HttpStatus.SERVICE_UNAVAILABLE)
'503 SERVICE_UNAVAILABLE'
```
