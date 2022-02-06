try:
    from pyTONPublicAPI import pyTONPublicAPI, pyTONException, pyTONAPIServerTonCenter
except:
    from api import pyTONPublicAPI, pyTONException
    from servers import pyTONAPIServerTonCenter

ton_address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"

def run_and_print(f):
    try:
        res = f()
        print(res)
        return res
    except pyTONException as pe:
        if pe.code in [-2, 500]:
            print("API call failed")
        else:
            raise pe
    except Exception as e:
        raise e
    return None

def test_no_address(api_server = None):
    client = pyTONPublicAPI(print_errors=True, api_server=api_server)
    run_and_print(lambda: client.get_address_information(address=ton_address))
    run_and_print(lambda: client.get_transactions(address=ton_address))
    run_and_print(lambda: client.get_transactions(address=ton_address, limit=1))
    run_and_print(lambda: client.get_address_balance(address=ton_address))
    run_and_print(lambda: client.get_address_state(address=ton_address))
    uaddress = run_and_print(lambda: client.unpack_address(address=ton_address))
    run_and_print(lambda: client.pack_address(address=uaddress))

def test_with_address(api_server = None):
    client = pyTONPublicAPI(address=ton_address, print_errors=True, api_server=api_server)
    run_and_print(lambda: client.get_address_information())
    run_and_print(lambda: client.get_transactions())
    run_and_print(lambda: client.get_address_balance())
    run_and_print(lambda: client.get_address_state())
    uaddress = run_and_print(lambda: client.unpack_address())
    run_and_print(lambda: client.pack_address(address=uaddress))

def test_general_functions(api_server = None):
    client = pyTONPublicAPI(print_errors=True, api_server=api_server)
    run_and_print(lambda: client.get_block_information(100))
    run_and_print(lambda: client.get_server_time())
    run_and_print(lambda: client.get_coin_price())

test_no_address()
test_with_address()
test_general_functions()

test_no_address(api_server=pyTONAPIServerTonCenter())
test_with_address(api_server=pyTONAPIServerTonCenter())
