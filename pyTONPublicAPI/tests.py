try:
    from pyTONPublicAPI import pyTONPublicAPI
except:
    from api import pyTONPublicAPI

ton_address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"

def test_no_address():
    client = pyTONPublicAPI(print_errors=True)
    print(client.get_address_information(address=ton_address))
    print(client.get_transactions(address=ton_address))
    print(client.get_transactions(address=ton_address, limit=1))
    print(client.get_address_balance(address=ton_address))
    print(client.get_address_state(address=ton_address))
    uaddress = client.unpack_address(address=ton_address)
    print(uaddress)
    print(client.pack_address(address=uaddress))

def test_with_address():
    client = pyTONPublicAPI(address=ton_address, print_errors=True)
    print(client.get_address_information())
    print(client.get_transactions())
    print(client.get_address_balance())
    print(client.get_address_state())
    uaddress = client.unpack_address()
    print(uaddress)
    print(client.pack_address(address=uaddress))

def test_general_functions():
    client = pyTONPublicAPI(print_errors=True)
    print(client.get_block_information(100))
    print(client.get_server_time())
    print(client.get_coin_price())

test_no_address()
test_with_address()
test_general_functions()
