from netmiko import ConnectHandler
from getpass import getpass
import os

# import logging

# For automated tests, set an env variable with password, if that fails, use getpass():
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Enable logging to understand the underling paramiko ssh handler connections:
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")
# my_device = {
#    "device_type":"linux",
#    "host": "10.9.18.11",
#    "username": "sbheemanathini",
#    "password": password,
# }
# net_connect = ConnectHandler(**my_device)
# print(net_connect.find_prompt())
# net_connect.disconnect()

# Connect to multiple device using a for-loop:
hitl = {
    "device_type": "linux",
    "host": "10.9.18.11",
    "username": "sbheemanathini",
    "password": password,
}

# Use send_command() to send command string to the device:
# for device in (hitl,):
#     net_connect = ConnectHandler(**device)
#     output = net_connect.send_command("date", expect_string=r"\$")
#     print(output)
#     net_connect.disconnect()

# Use send_command_timing() delay based connection to the device:
for device in (hitl,):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command_timing("date")
    print(output)
    net_connect.disconnect()
