import requests
from enum import Enum
from abc import ABC


# noinspection PyPep8Naming
class pyTONAPIServerTypes(Enum):
    TonCenter = 2
    TonAPI = 3
    TonCAT = 4


# noinspection PyPep8Naming
class pyTONAPIServer(ABC):
    def __init__(self, server_type, api_url):
        self.server_type = server_type
        self.api_url = api_url
        self.parameters_subst = {}

    def add_headers(self, headers):
        pass

    def add_parameters(self, params):
        for source_name, dest_name in self.parameters_subst.items():
            if source_name in params:
                params[dest_name] = params[source_name]
                del params[source_name]

    def request_get(self, method = None, headers=None, params=None, timeout=None):
        result = requests.get(url=self.api_url + method, headers=headers, params=params, timeout=timeout)
        return result.json()


# noinspection PyPep8Naming
class pyTONAPIServerTonCenter(pyTONAPIServer):
    def __init__(self, api_key = None):
        super().__init__(pyTONAPIServerTypes.TonCenter, "https://toncenter.com/api/v2/")
        self.api_key = api_key

    def add_parameters(self, params):
        super().add_parameters(params)
        if self.api_key:
            params["api_key"] = self.api_key


# noinspection PyPep8Naming
class pyTONAPIServerTonCenterTest(pyTONAPIServerTonCenter):
    def __init__(self, api_key = None):
        super().__init__(api_key = api_key)
        self.api_url = "https://testnet.toncenter.com/api/v2/"


# noinspection PyPep8Naming
class pyTONAPIServerTonAPI(pyTONAPIServer):
    def __init__(self, api_key = None):
        self.api_key = api_key
        super().__init__(pyTONAPIServerTypes.TonAPI, "https://tonapi.io/v2/")
        self.parameters_subst["address"] = "account"

    def add_headers(self, headers):
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key


# noinspection PyPep8Naming
class pyTONAPIServerTonAPITest(pyTONAPIServerTonAPI):
    def __init__(self, api_key = None):
        super().__init__(api_key = api_key)
        self.api_url = "https://testnet.tonapi.io/v1/"


# noinspection PyPep8Naming
class pyTONAPIServerCAT(pyTONAPIServer):
    def __init__(self):
        super().__init__(pyTONAPIServerTypes.TonCAT, "https://api.ton.cat/v2/contracts/")

    def request_get(self, method = None, headers=None, params=None, timeout=None):
        method = method.replace("%address%", params["address"])
        params.pop("address")
        return requests.get(url=self.api_url + method, headers=headers, params=params, timeout=timeout).json()
