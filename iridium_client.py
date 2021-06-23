import requests


class IridiumClient:

    def __init__(self, host="localhost", port=14007):
        self.host = host
        self.port = port
        self.endpoint = f"http://{self.host}:{self.port}/json_rpc"
        print(self.endpoint)

    def reset(self, view_secret_key=None, print_info=False):
        if view_secret_key is None:
            query = {
                "params": {},
                "jsonrpc": "2.0",
                "id": "iridium-python-api",
                "method": "reset",
            }
            response = requests.post(self.endpoint, json=query)
            data = response.json()

        else:
            query = {
                "params": {
                    "viewSecretKey": view_secret_key,
                },
                "jsonrpc": "2.0",
                "id": "iridium-python-api",
                "method": "reset",
            }
            response = requests.post(self.endpoint, json=query)
            data = response.json()

        if print_info:
            print(f"{'-' * 20}reset{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            if view_secret_key is None:
                print("Message: Re-synchronized Wallet.")
            else:
                print("Message: Your 'viewSecretKey' has been overridden.")
            print(data)

        return data

    def save(self, print_info=False):
        query = {
            "params": {},
            "jsonrpc": "2.0",
            "id": "iridium-python-api",
            "method": "save",
        }
        response = requests.post(self.endpoint, json=query)
        data = response.json()

        if print_info:
            print(f"{'-' * 20}save{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            print(f"Message: Wallet Changes Saved.")
            print(data)

        return data

    def get_view_key(self, print_info=False):
        query = {
            "params": {},
            "jsonrpc": "2.0",
            "id": "iridium-python-api",
            "method": "getViewKey",
        }
        response = requests.post(self.endpoint, json=query)
        data = response.json()

        if print_info:
            print(f"{'-' * 20}getViewKey{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            print(data)

        return data

    def get_spend_keys(self, address, print_info=False):
        query = {
            "params": {
                "address": address
            },
            "jsonrpc": "2.0",
            "id": "iridium-python-api",
            "method": "getSpendKeys",
        }
        response = requests.post(self.endpoint, json=query)
        data = response.json()

        if print_info:
            print(f"{'-' * 20}getSpendKeys{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            print(data)

        return data

    def get_status(self, print_info=False):
        query = {
            "params": {},
            "jsonrpc": "2.0",
            "id": "iridium-python-api",
            "method": "getStatus",
        }
        response = requests.post(self.endpoint, json=query)
        data = response.json()

        if print_info:
            print(f"{'-' * 20}getStatus{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            print(data)

        return data

    def get_addresses(self, print_info=False):
        query = {
            "params": {},
            "jsonrpc": "2.0",
            "id": "iridium-python-api",
            "method": "getAddresses",
        }
        response = requests.post(self.endpoint, json=query)
        data = response.json()

        if print_info:
            print(f"{'-' * 20}getAddresses{'-' * 20}")
            print(f"Status Code: {response.status_code}")
            print(data)

        return data
