from api import pyTONPublicAPI, pyTONException

client = pyTONPublicAPI(address = "EQA70Y6kLmQ_5tFEEqlLGrXIf7fCNiJrXTInX5Hy8viZPR9H")

print(client.get_address_information())
print(client.get_address_information(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))

print(client.get_transactions())
print(client.get_transactions(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"))
print(client.get_transactions(address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N", limit = 1))
