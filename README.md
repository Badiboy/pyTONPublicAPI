[![PyPi Package Version](https://img.shields.io/pypi/v/pyTONPublicAPI.svg)](https://pypi.python.org/pypi/pyTONPublicAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTONPublicAPI.svg)](https://pypi.python.org/pypi/pyTONPublicAPI)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTONPublicAPI.svg)](https://pypi.org/project/pyTONPublicAPI/)

# <p align="center">pyTONPublicAPI</p>
Python implementation of TON Public API (https://ton.sh/api) for The Open Network (TON).

# Installation
Installation using pip (a Python package manager)*:
```
$ pip install pyTONPublicAPI
```

# Usage
Everything is as simple as the API itself.
1. Create pyTONPublicAPI instance
2. Access API methods in pythonic notation (getAddressInformation -> get_address_information)
```
from api import pyTONPublicAPI
client = pyTONPublicAPI()
print(client.get_address_balance(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))
```
If you want to work with a single address - you can pre-set it on init and avoid in functions.
```
from api import pyTONPublicAPI
client = pyTONPublicAPI(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N")
print(client.get_address_balance())
print(client.get_transactions())
```
You can also check tests.py.

# Exceptions
Exceptions are rised using pyTONException class.

