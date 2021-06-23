from iridium_client import IridiumClient

iridium = IridiumClient("localhost", 14007)  # IP or URL and Port

# ---------- Below Is An Example With All Of The Methods ----------
# If you want to view the output of any method add this argument: "print_info=True". See examples below:

iridium.reset(print_info=True)  # Re-synchronize Your Wallet.
iridium.reset(view_secret_key="EXAMPLE_SECRET_VIEW_KEY", print_info=True)  # Override Your 'viewSecretKey'.

iridium.save(print_info=True)  # Save Your Wallet.

iridium.get_view_key(print_info=True)  # returns the view key

iridium.get_spend_keys(address="YOUR_IRIDIUM_ADDRESS", print_info=True)  # returns your spend keys

iridium.get_status(print_info=True)  # returns information about the current RPC Wallet state

iridium.get_addresses(print_info=True)  # returns a list (array) of your RPC Wallet's addresses
