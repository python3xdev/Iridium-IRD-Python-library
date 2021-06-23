# iridium-python-api

Python wrapper for the [Iridium Walletd JSON RPC API](https://wiki.ird.cash/iridium_walletd_rpc_call "Iridium Wiki").

Refer to the [python API documentation](https://wiki.ird.cash/python_api "Iridium Wiki Python API") for help with all of the methods.

## Usage

### Plain Python

* #### Creating an instance

Import the [IridiumClient](iridium_client.py) class and create a new instance of it:

```py
from iridium_client import IridiumClient
iridium = IridiumClient("localhost", 14007)
```

Or if your `iridium_walletd` is running on `localhost` with the default port of `14007`, there is no need to pass in any arguments, there are default values:

```py
from iridium_client import IridiumClient
iridium = IridiumClient()
```

------

