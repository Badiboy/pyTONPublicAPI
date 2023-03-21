import inspect
from time import sleep
try:
    from pyTONPublicAPI import pyTONPublicAPI, pyTONException, pyTONAPIServerTonSh, pyTONAPIServerTonCenter, pyTONAPIServerTonAPI
except:
    from api import pyTONPublicAPI, pyTONException
    from servers import pyTONAPIServerTonSh, pyTONAPIServerTonCenter, pyTONAPIServerTonAPI

ton_address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"

def run_and_print(f):
    try:
        sleep(1)
        print()
        print(inspect.getsourcelines(f)[0][0].strip())
        res = f()
        print(res)
        return res
    except pyTONException as pe:
        if pe.code in [-2, 404, 500, 504]:
            print("API call failed. Code: {}, Message: {}".format(pe.code, pe.message))
        else:
            raise pe
    except Exception as e:
        raise e
    return None

def test_no_address(api_server = None):
    client = pyTONPublicAPI(print_errors=True, api_server=api_server)
    run_and_print(lambda: client.get_address_information(address=ton_address))
    run_and_print(lambda: client.get_address_balance(address=ton_address))
    run_and_print(lambda: client.get_address_state(address=ton_address))
    run_and_print(lambda: client.get_transactions(address=ton_address))
    run_and_print(lambda: client.get_transactions(address=ton_address, limit=1))

def test_with_address(api_server = None):
    client = pyTONPublicAPI(address=ton_address, print_errors=True, api_server=api_server)
    run_and_print(lambda: client.get_address_information())
    run_and_print(lambda: client.get_address_balance())
    run_and_print(lambda: client.get_address_state())
    run_and_print(lambda: client.get_transactions())

def test_tonsh_functions(api_server = None):
    client = pyTONPublicAPI(print_errors=True, api_server=api_server)
    uaddress = run_and_print(lambda: client.unpack_address(address=ton_address))
    run_and_print(lambda: client.pack_address(address=uaddress))
    run_and_print(lambda: client.get_block_information(100))
    run_and_print(lambda: client.get_server_time())
    run_and_print(lambda: client.get_coin_price())

def test_toncenter_functions(api_server = None):
    client = pyTONPublicAPI(address=ton_address, print_errors=True, api_server=api_server)
    uaddress = run_and_print(lambda: client.unpack_address(address=ton_address))
    run_and_print(lambda: client.pack_address(address=uaddress))
    run_and_print(lambda: client.get_extended_address_information())
    run_and_print(lambda: client.detect_address())
    run_and_print(lambda: client.get_masterchain_info())
    run_and_print(lambda: client.get_consensus_block())
    run_and_print(lambda: client.lookup_block(1, 1, seqno = 1))
    run_and_print(lambda: client.shards(1))
    run_and_print(lambda: client.get_block_transactions(1, 1, 1))
    run_and_print(lambda: client.get_block_header(1, 1, 1))
    #Returns 503 error run_and_print(lambda: client.try_locate_tx(ton_address, ton_address, 1))
    #Returns 503 error run_and_print(lambda: client.try_locate_result_tx(ton_address, ton_address, 1))
    #Returns 503 error run_and_print(lambda: client.try_locate_source_tx(ton_address, ton_address, 1))

test_no_address(api_server=pyTONAPIServerTonSh())
test_with_address(api_server=pyTONAPIServerTonSh())

test_no_address(api_server=pyTONAPIServerTonCenter())
test_with_address(api_server=pyTONAPIServerTonCenter())

test_no_address(api_server=pyTONAPIServerTonAPI())
test_with_address(api_server=pyTONAPIServerTonAPI())

test_tonsh_functions(api_server=pyTONAPIServerTonSh())
test_toncenter_functions(api_server=pyTONAPIServerTonCenter())
