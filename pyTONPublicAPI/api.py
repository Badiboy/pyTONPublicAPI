import requests


# noinspection PyPep8Naming
class pyTONException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)


# noinspection PyPep8Naming
class pyTONPublicAPI:
    """
    TON Public API Client
    https://ton.sh/api
    """
    api_url = "https://api.ton.sh/"

    def __init__(self, blockchain_id = "mainnet", address = None, print_errors = False):
        """
        Create the pyTONPublicAPI instance.

        :param blockchain_id: Identifier of target blockchain ID, either "mainnet" or "test"
        :param address: (Optional) Identifier of target account in TON to use in all queries
        :param print_errors: (Optional) Print dumps on request errors
        """
        self.blockchain_id = blockchain_id
        self.address = address
        self.print_errors = print_errors

    def __request(self, method, use_address = True, **kwargs):
        if kwargs:
            data = dict(kwargs)
            if use_address and not data.get("address"):
                data["address"] = self.address
        else:
            if use_address:
                data = {"address": self.address}
            else:
                data = {}
        if use_address and not data.get("address"):
            raise pyTONException(-1, "No address given")
        resp = requests.get(url=self.api_url + method, data=data).json()
        if not resp:
            if self.print_errors:
                print("None request response")
            raise pyTONException(-2, "None request response")
        elif not resp.get("ok"):
            if ("DOCTYPE" in resp):
                if self.print_errors:
                    print("Response: {}".format(resp))
                raise pyTONException(-3, "Response in HTML")
            elif ("error_code" in resp):
                if self.print_errors:
                    print("Response: {}".format(resp))
                raise pyTONException(resp.get("error_code"), "Error code")
            elif ("code" in resp):
                if self.print_errors:
                    print("Response: {}".format(resp))
                raise pyTONException(resp.get("code"), resp.get("description"))
            else:
                if self.print_errors:
                    print("Response: {}".format(resp))
                raise pyTONException(-4, "Unknown response format, enable 'print_errors' to see response")
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
        return self.__request(method, address = address).get("result")

    def get_transactions(self, address = None, limit = None, lt = None, hash = None):
        """
        getTransactions
        Use this method to get balance (in nanotons) and state of a given address.
        :param address: Identifier of target account in TON
        :param limit: (Optional) Limits the number of transactions to be retrieved. Values between 1—10 are accepted. Defaults to 10.
        :param lt: (Optional) Logical time of transaction to start with, must be sent with hash
        :param hash: (Optional) Hash of transaction to start with, must be sent with lt
        :return:
        """
        method = "getTransactions"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if lt is not None:
            params["lt"] = lt
        if hash is not None:
            params["hash"] = hash
        if params:
            return self.__request(method, address = address, **params).get("result")
        else:
            return self.__request(method, address = address).get("result")

    def get_address_balance(self, address = None):
        """
        getAddressBalance
        Use this method to get balance (in nanotons) of a given address.
        :param address: Identifier of target account in TON
        :return: balance
        """
        method = "getAddressBalance"
        return self.__request(method, address = address).get("result")

    def get_address_state(self, address = None):
        """
        getAddressState
        Use this method to get state of a given address. State can be either unitialized, active or frozen.
        :param address: Identifier of target account in TON
        :return: state
        """
        method = "getAddressState"
        return self.__request(method, address = address).get("result")

    def unpack_address(self, address = None):
        """
        unpackAddress
        Use this method to get state of a given address. State can be either unitialized, active or frozen.
        :param address: Identifier of target account in TON in human-readable format
        :return: Identifier in raw format
        """
        method = "unpackAddress"
        return self.__request(method, address = address).get("result")

    def pack_address(self, address):
        """
        packAddress
        Use this method to convert an address from raw to human-readable format.
        :param address: Identifier of target account in TON in raw format
        :return: Identifier in human-readable format
        """
        method = "packAddress"
        return self.__request(method, address = address).get("result")

    def get_block_information(self, seqno, workchain_id = None):
        """
        getBlockInformation
        Use this method to get basic information about the block.
        :param seqno: Block height
        :param workchain_id: (Optional) Identifier of target workchain in TON. Defaults to 0.
        :return: Identifier in human-readable format
        """
        method = "getBlockInformation"
        params = {"seqno": seqno}
        if workchain_id is not None:
            params["workchain_id"] = workchain_id
        return self.__request(method, use_address = False, **params).get("result")

    def get_server_time(self):
        """
        getServerTime
        Get TON node time (not TON.sh server time).
        :return:
        """
        method = "getServerTime"
        return self.__request(method, use_address = False).get("result")

    def get_coin_price(self):
        """
        getCoinPrice
        Returns TONCOIN price in USDT, pulled from Uniswap.
        :return:
        """
        method = "getCoinPrice"
        return self.__request(method, use_address = False).get("result")
