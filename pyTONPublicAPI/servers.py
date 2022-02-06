from enum import Enum
from abc import ABC


# noinspection PyPep8Naming
class pyTONAPIServerTypes(Enum):
    TonSh = 1
    TonCenter = 2


# noinspection PyPep8Naming
class pyTONAPIServer(ABC):
    def __init__(self, server_type, api_url):
        self.server_type = server_type
        self.api_url = api_url

    def add_parameters(self, params):
        pass


# noinspection PyPep8Naming
class pyTONAPIServerTonSh(pyTONAPIServer):
    def __init__(self, blockchain_id = None):
        super().__init__(pyTONAPIServerTypes.TonSh, "https://api.ton.sh/")
        self.blockchain_id = blockchain_id

    def add_parameters(self, params):
        if self.blockchain_id:
            params["blockchain_id"] = self.blockchain_id


# noinspection PyPep8Naming
class pyTONAPIServerTonCenter(pyTONAPIServer):
    def __init__(self, api_key = None):
        super().__init__(pyTONAPIServerTypes.TonCenter, "https://toncenter.com/api/v2/")
        self.api_key = api_key

    def add_parameters(self, params):
        if self.api_key:
            params["api_key"] = self.api_key


# noinspection PyPep8Naming
class pyTONAPIServerTonCenterTest(pyTONAPIServerTonCenter):
    def __init__(self, api_key = None):
        super().__init__(api_key = api_key)
        self.api_url = "https://testnet.toncenter.com/api/v2/"
