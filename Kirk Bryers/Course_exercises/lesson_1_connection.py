from netmiko import ConnectHandler
from getpass import getpass

# import time

# Create a simple connection:
# password = getpass()
# time.sleep(4)
# net_connect = ConnectHandler(
#    device_type="linux",
#    host="10.9.18.11",
#    username="sbheemanathini",
#    password=password,
#    session_log="session.out",
# )
# With device_type="invalid", netmiko dumps the support device types

# Create a dictionary:
my_device = {
    "device_type":"invalid",
    "host": "10.9.18.11",
    "username": "sbheemanathini",
    "password": getpass(),
}

# Without Context Manager and graceful disconnect:
# net_connect = ConnectHandler(**my_device)
# print(net_connect.find_prompt())
# output = net_connect.send_command("date")
# print(output)
# net_connect.disconnect()

# Context manager explicitly disconnects the session:
with ConnectHandler(**my_device) as net_connect:
    print(net_connect.find_prompt())
    print(net_connect.send_command("date"))
