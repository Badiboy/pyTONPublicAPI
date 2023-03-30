[![PyPi Package Version](https://img.shields.io/pypi/v/pyTONPublicAPI.svg)](https://pypi.python.org/pypi/pyTONPublicAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTONPublicAPI.svg)](https://pypi.python.org/pypi/pyTONPublicAPI)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTONPublicAPI.svg)](https://pypi.org/project/pyTONPublicAPI/)

# <p align="center">pyTONPublicAPI</p>
Python implementation of TON Public API for The Open Network (TON).

# Supported API servers
* [TON.sh](https://ton.sh/api/) - full
* [TON Center](https://toncenter.com/api/v2/) - partial, will be extended
* [TON Center Testnet](https://testnet.toncenter.com/api/v2/) - partial, will be extended
* [TON API](https://tonapi.io/) - partial, will be extended
* [TON API Testnet](https://testnet.tonapi.io/) - partial, will be extended
* [TON CAT](https://ton.cat/) - partial, will be extended

# Installation
Installation using pip (a Python package manager):
```
$ pip install pyTONPublicAPI
```

# Usage
Everything is as simple as the API itself.
1. Create pyTONPublicAPI instance
2. Access API methods in pythonic notation (getAddressInformation -> get_address_information)
```
from pyTONPublicAPI import pyTONPublicAPI
client = pyTONPublicAPI()
print(client.get_address_balance(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))
```
If you want to work with a single address - you can pre-set it on init and avoid in functions.
```
from pyTONPublicAPI import pyTONPublicAPI
client = pyTONPublicAPI(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N")
print(client.get_address_balance())
print(client.get_transactions())
```
You can also check tests.py.

# Exceptions
Exceptions are rised using pyTONException class.


# API servers
By default all calls are sent to TON.sh server. To select API server you should:
1. Create server object
2. Pass it to pyTONPublicAPI constructor via api_server parameter
```
from pyTONPublicAPI import pyTONPublicAPI, pyTONAPIServerTonCenter
api_server=pyTONAPIServerTonCenter()
client = pyTONPublicAPI(api_server=api_server)
```

## Ton.sh
Site: https://ton.sh/api/

Class: **pyTONAPIServerTonSh**

Additional constructor paramters:
* blockchain_id - Identifier of target blockchain ID, either "mainnet" or "test". Default is "None", so default begaviour is up to API server.

## Ton Center
Site: https://toncenter.com/api/v2/

Class: **pyTONAPIServerTonCenter**

Additional constructor paramters:
* api_key - Authentication key. Using API without API key is limited to 1 request per second. Default is "None", so API is used without API key.

## Ton Center Testnet
Site: https://testnet.toncenter.com/api/v2/

Class: **pyTONAPIServerTonCenterTest**

Additional constructor paramters:
* api_key - Authentication key. Using API without API key is limited to 1 request per second. Default is "None", so API is used without API key.

## TON API
Site: https://tonapi.io/

Class: **pyTONAPIServerTonAPI**

Additional constructor paramters:
* api_key - Authentication key. Using API without API key is limited to 1 request per second. Default is "None", so API is used without API key.

## TON API Testnet
Site: https://testnet.tonapi.io/

Class: **pyTONAPIServerTonAPITest**

Additional constructor paramters:
* api_key - Authentication key. Using API without API key is limited to 1 request per second. Default is "None", so API is used without API key.

## TON CAT
Site: https://ton.cat/

Class: **pyTONAPIServerCAT**

# Notes
1. API servers support different subset of commands. Check correspondent API specification before use.   
2. API servers have different reply formats! Currently it's up to you to deal with it. May be once there will be a reply parser for unification.
