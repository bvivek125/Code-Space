from netmiko import ConnectHandler
from getpass import getpass
import logging
import time
import os 

# For automated tests, set an env variable with password, if that fails, use getpass():
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# logging.basicConfig(filename='test_1.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

# my_device = {
#     "device_type":"linux",
#     "host": "10.9.18.11",
#     "username": "sbheemanathini",
#     "password": password,
#     "fast_cli": False,
# }
# Delay factor & max-loops to slow the send commands:
# with ConnectHandler(**my_device) as net_connect:
#     output = net_connect.send_command("arp -a",delay_factor=5, max_loops=1000)
#     print(output)

# my_device = {
#     "device_type":"linux",
#     "host": "10.9.18.11",
#     "username": "sbheemanathini",
#     "password": password,
#     "fast_cli": False,
#     # Doubles ALL the delays
#     "global_delay_factor": 2,
# }
# with ConnectHandler(**my_device) as net_connect:
#     output = net_connect.send_command("arp -a")
#     print(output)

my_device = {
    "device_type":"linux",
    "host": "10.9.18.11",
    "username": "sbheemanathini",
    "password": password,
    "session_log":"sudo.out",
    "fast_cli": False,
}
# Using expect_string works for multiline prompting with regex
# with ConnectHandler(**my_device) as net_connect:
#     output = net_connect.send_command("sudo su",expect_string=r"password",strip_prompt=False,strip_command=False)
#     output += net_connect.send_command(password,expect_string=r"sbheemanathini",strip_prompt=False,strip_command=False)
#     # output += net_connect.send_command("\n", delay_factor=5, max_loops=1000, expect_string=r"~\$",strip_prompt=False,strip_command=False)
#     print(output)

# send_command_timing eliminates the need of expect_string
with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command_timing("sudo su",strip_prompt=False,strip_command=False)
    output += net_connect.send_command_timing(password,strip_prompt=False,strip_command=False)
    print(output)

