from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint 
import os

# For automated tests, set an env variable with password, if that fails, use getpass():
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


# Connect to multiple device using a for-loop:
hitl = {
    "device_type": "linux",
    "host": "10.9.18.11",
    "username": "sbheemanathini",
    "password": password,
}

# Use textfsm to parse the output into structured data
# Netmiko will refer to the ntc-templates for commands
# net_connect = ConnectHandler(**hitl)
# output = net_connect.send_command("arp -a", use_textfsm=True)
# pprint(output)
# net_connect.disconnect()

# Use textfsm template to parse the output into structured data
# for device in (hitl,):
#     net_connect = ConnectHandler(**device)
#     output = net_connect.send_command("date", use_textfsm=True, textfsm_template="my_template.tpl")
#     pprint(output)
#     net_connect.disconnect()

# Netmiko will refer to the genie available parsers
# net_connect = ConnectHandler(**hitl)
# output = net_connect.send_command("arp -a", use_genie=True)
# pprint(output)
# net_connect.disconnect()


# Netmiko will refer to the ttp template [reverse jinja2 template] for available parsers
net_connect = ConnectHandler(**hitl)
output = net_connect.send_command("arp -a", use_ttp=True, ttp_template="my_template.ttp")
pprint(output)
net_connect.disconnect()