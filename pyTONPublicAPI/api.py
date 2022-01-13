import json

import requests


# noinspection PyPep8Naming
class pyTONException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)


# noinspection PyPep8Naming
class pyTONPublicAPI:
    """TON Public API Client"""
    api_url = "https://api.ton.sh/"

    def __init__(self, blockchain_id = "mainnet", address = None):
        """
        Create the pyTONPublicAPI instance.

        :param blockchain_id: Identifier of target blockchain ID, either "mainnet" or "test"
        :param address: (Optional) 	Identifier of target account in TON to use in all queries
        """
        self.blockchain_id = blockchain_id
        self.address = address

    def __request(self, method, **kwargs):
        if kwargs:
            data = dict(kwargs)
            if not data.get("address"):
                data["address"] = self.address
        else:
            data = {"address": self.address}
        if not data.get("address"):
            raise pyTONException(-1, "No address given")
        resp = requests.get(url=self.api_url + method, data=data).json()
        if not resp.get('ok'):
            raise pyTONException(resp.get('code'), resp.get('description'))
        else:
            return resp

    def get_address_information(self, address = None):
        """
        getAddressInformation
        Use this method to get balance (in nanotons) and state of a given address.
        :param address: Identifier of target account in TON
        :return:
        """
        method = "getAddressInformation"
        params = {}
        if params:
            return self.__request(method, address = address, **params).get("result")
        else:
            return self.__request(method, address = address).get("result")

    def get_transactions(self, address = None, limit = None, lt = None, hash = None):
        """
        getTransactions
        Use this method to get balance (in nanotons) and state of a given address.
        :param address: Identifier of target account in TON
        :param limit: Limits the number of transactions to be retrieved. Values between 1—10 are accepted. Defaults to 10.
        :param lt: Logical time of transaction to start with, must be sent with hash
        :param hash: Hash of transaction to start with, must be sent with lt
        :return:
        """
        method = "getTransactions"
        params = {}
        if limit:
            params["limit"] = limit
        if lt:
            params["lt"] = lt
        if hash:
            params["hash"] = hash
        if params:
            return self.__request(method, address = address, **params).get("result")
        else:
            return self.__request(method, address = address).get("result")
