try:
    from pyTONPublicAPI import pyTONPublicAPI
except:
    from api import pyTONPublicAPI

client = pyTONPublicAPI(address = "EQA70Y6kLmQ_5tFEEqlLGrXIf7fCNiJrXTInX5Hy8viZPR9H")

print(client.get_address_information())
print(client.get_address_information(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))

print(client.get_transactions())
print(client.get_transactions(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))
print(client.get_transactions(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N", limit = 1))

print(client.get_address_balance())
print(client.get_address_balance(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))

print(client.get_address_state())
print(client.get_address_state(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))

uaddress1 = client.unpack_address()
uaddress2 = client.unpack_address(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N")
print(uaddress1)
print(uaddress2)

print(client.pack_address(address = uaddress1))
print(client.pack_address(address = uaddress2))

print(client.get_block_information(100))

print(client.get_server_time())

print(client.get_coin_price())
