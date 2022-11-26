import requests
from .servers import pyTONAPIServerTonSh


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
    """

    def __init__(self, blockchain_id = "mainnet", address = None, print_errors = False, api_server = None, timeout = None):
        """
        Create the pyTONPublicAPI instance.

        :param blockchain_id: Identifier of target blockchain ID, either "mainnet" or "test"
        :param address: (Optional) Identifier of target account in TON to use in all queries
        :param print_errors: (Optional) Print dumps on request errors
        """
        self.blockchain_id = blockchain_id
        self.address = address
        self.print_errors = print_errors
        self.api_server = api_server if api_server else pyTONAPIServerTonSh()
        self.timeout = timeout

    def __request(self, method, use_address = True, **kwargs):
        if kwargs:
            data = dict(kwargs)
        else:
            data = {}
        if use_address and not data.get("address"):
            data["address"] = self.address
        if use_address and not data.get("address"):
            raise pyTONException(-1, "No address given")
        self.api_server.add_parameters(data)
        try:
            resp = requests.get(url=self.api_server.api_url + method, params=data, timeout=self.timeout).json()
        except ValueError as e:
            message = "Response decode failed: {}".format(e)
            if self.print_errors:
                print(message)
            raise pyTONException(-2, message)
        except requests.ReadTimeout as e:
            message = "Read timed out"
            if self.print_errors:
                print(message)
            raise pyTONException(-3, message)
        except Exception as e:
            message = "Request unknown exception: {}, {}".format(type(e).__name__, e)
            if self.print_errors:
                print(message)
            raise pyTONException(-98, message)
        if not resp:
            message = "None request response"
            if self.print_errors:
                print(message)
            raise pyTONException(-99, message)
        elif not resp.get("ok"):
            if ("error_code" in resp):
                if self.print_errors:
                    print("Response: {}".format(resp))
                code = resp.get("error_code")
                if isinstance(code, str) and code.isdigit():
                    code = int(code)
                raise pyTONException(code, "Error code returned")
            elif ("code" in resp):
                if self.print_errors:
                    print("Response: {}".format(resp))
                code = resp.get("code")
                if isinstance(code, str) and code.isdigit():
                    code = int(code)
                description = resp.get("description")
                if not description:
                    description = resp.get("error")
                if not description:
                    description = resp.get("message")
                raise pyTONException(code, description)
            else:
                if self.print_errors:
                    print("Response: {}".format(resp))
                raise pyTONException(-5, "Unknown response structure, enable 'print_errors' to see response")
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

    def get_transactions(self, address = None, limit = None, lt = None, hash = None, to_lt = None, archival = None):
        """
        getTransactions
        Use this method to get balance (in nanotons) and state of a given address.
        :param address: Identifier of target account in TON
        :param limit: (Optional) Limits the number of transactions to be retrieved. Values between 1—10 are accepted. Defaults to 10.
        :param lt: (Optional) Logical time of transaction to start with, must be sent with hash
        :param hash: (Optional) Hash of transaction to start with, must be sent with lt
        :param to_lt: (Optional, not all servers supports) Logical time of transaction to finish with (to get tx from lt to to_lt).
        :param archival: (Optional, not all servers supports) By default getTransaction request is processed by any available liteserver. If archival=true only liteservers with full history are used.
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
        if to_lt is not None:
            params["to_lt"] = to_lt
        if archival is not None:
            params["archival"] = archival
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
        Use this method to convert an address from human-readable to raw format.
        :param address: Identifier of target account in TON in human-readable format. Example : EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N
        :return: Identifier in raw format
        """
        method = "unpackAddress"
        return self.__request(method, address = address).get("result")

    def pack_address(self, address):
        """
        packAddress
        Use this method to convert an address from raw to human-readable format.
        :param address: Identifier of target account in TON in raw format. Example : 0:83DFD552E63729B472FCBCC8C45EBCC6691702558B68EC7527E1BA403A0F31A8
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

    def get_extended_address_information(self, address = None):
        """
        getExtendedAddressInformation
        Similar to previous one but tries to parse additional information for known contract types. This method is based on tonlib's function getAccountState. For detecting wallets we recommend to use getWalletInformation.
        :param address: Identifier of target account in TON
        :return:
        """
        method = "getExtendedAddressInformation"
        return self.__request(method, address = address).get("result")

    def get_wallet_information(self, address = None):
        """
        getWalletInformation
        Retrieve wallet information. This method parses contract state and currently supports more wallet types than getExtendedAddressInformation: simple wallet, standart wallet, v3 wallet, v4 wallet.
        :param address: Identifier of target account in TON
        :return:
        """
        method = "getWalletInformation"
        return self.__request(method, address = address).get("result")

    def detect_address(self, address = None):
        """
        detectAddress
        Get all possible address forms.
        :param address: Identifier of target TON account in any form.
        :return:
        """
        method = "detectAddress"
        return self.__request(method, address = address).get("result")

    def get_masterchain_info(self):
        """
        getMasterchainInfo
        Get up-to-date masterchain state.
        :return:
        """
        method = "getMasterchainInfo"
        return self.__request(method).get("result")

    def get_consensus_block(self):
        """
        getConsensusBlock
        Get consensus block and its update timestamp.
        :return:
        """
        method = "getConsensusBlock"
        return self.__request(method).get("result")

    def lookup_block(self, workchain, shard, seqno = None, lt = None, unixtime = None):
        """
        lookupBlock
        Look up block by either seqno, lt or unixtime.
        :param workchain: Workchain id to look up block in
        :param shard: Shard id to look up block in
        :param seqno: (Optional, one of) Block's height
        :param lt: (Optional, one of) Block's logical time
        :param unixtime: (Optional, one of) Block's unixtime
        :return:
        """
        method = "lookupBlock"
        params = {
            "workchain": workchain,
            "shard": shard,
        }
        if seqno is not None:
            params["seqno"] = seqno
        if lt is not None:
            params["lt"] = lt
        if unixtime is not None:
            params["unixtime"] = unixtime
        if params:
            return self.__request(method, **params).get("result")

    def shards(self, seqno):
        """
        shards
        Get shards information.
        :param seqno: Masterchain seqno to fetch shards of.
        :return:
        """
        method = "shards"
        params = {
            "seqno": seqno,
        }
        if params:
            return self.__request(method, **params).get("result")

    def get_block_transactions(self, workchain, shard, seqno, root_hash = None, file_hash = None, after_lt = None, after_hash = None, count = None):
        """
        getBlockTransactions
        Get transactions of the given block.param workchain: Workchain id to look up block in
        :param workchain:
        :param shard:
        :param seqno:
        :param root_hash: (Optional)
        :param file_hash: (Optional)
        :param after_lt: (Optional)
        :param after_hash: (Optional)
        :param count: (Optional)
        :return:
        """
        method = "getBlockTransactions"
        params = {
            "workchain": workchain,
            "shard": shard,
            "seqno": seqno,
        }
        if root_hash is not None:
            params["root_hash"] = root_hash
        if file_hash is not None:
            params["file_hash"] = file_hash
        if after_lt is not None:
            params["after_lt"] = after_lt
        if after_hash is not None:
            params["after_hash"] = after_hash
        if count is not None:
            params["count"] = count
        if params:
            return self.__request(method, **params).get("result")

    def get_block_header(self, workchain, shard, seqno, root_hash = None, file_hash = None):
        """
        getBlockHeader
        Get metadata of a given block.
        :param workchain:
        :param shard:
        :param seqno:
        :param root_hash: (Optional)
        :param file_hash: (Optional)
        :return:
        """
        method = "getBlockHeader"
        params = {
            "workchain": workchain,
            "shard": shard,
            "seqno": seqno,
        }
        if root_hash is not None:
            params["root_hash"] = root_hash
        if file_hash is not None:
            params["file_hash"] = file_hash
        if params:
            return self.__request(method, **params).get("result")

    def try_locate_tx(self, source, destination, created_lt):
        """
        tryLocateTx
        Locate outcoming transaction of destination address by incoming message.
        :param source:
        :param destination:
        :param created_lt:
        :return:
        """
        method = "tryLocateTx"
        params = {
            "source": source,
            "destination": destination,
            "created_lt": created_lt,
        }
        if params:
            return self.__request(method, **params).get("result")

    def try_locate_result_tx(self, source, destination, created_lt):
        """
        tryLocateResultTx
        Same as try_locate_tx. Locate outcoming transaction of destination address by incoming message
        :param source:
        :param destination:
        :param created_lt:
        :return:
        """
        method = "tryLocateResultTx"
        params = {
            "source": source,
            "destination": destination,
            "created_lt": created_lt,
        }
        if params:
            return self.__request(method, **params).get("result")

    def try_locate_source_tx(self, source, destination, created_lt):
        """
        tryLocateSourceTx
        Locate incoming transaction of source address by outcoming message.
        :param source:
        :param destination:
        :param created_lt:
        :return:
        """
        method = "tryLocateSourceTx"
        params = {
            "source": source,
            "destination": destination,
            "created_lt": created_lt,
        }
        if params:
            return self.__request(method, **params).get("result")
