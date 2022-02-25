#!/usr/bin/env python

"To make program compatible with python2 and python3"
from __future__ import print_function, unicode_literals

# import sys
# print(sys.argv)

# Connect Handler
from netmiko import Netmiko
from getpass import getpass
password = getpass()
import logging
logging.basicConfig(filename='test.log',level=logging.logging.DEBUG)
logger=logging.getLogger("netmiko")

#net_conn = Netmiko(host="1:1:1:1", username="admin",
#                   password=getpass(),device_type="fortinet")



my_device = {
    'host':'1:1:1:1',
    'username':'admin',
    'password':password,
    'secret': password,
    'device_type':'fortinet'
    'global_delay_factor': 2
}

net_conn = Netmiko(**my_device)
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())

net_conn.enable()
print(net_conn.find_prompt())

output = net_conn.send_command("show arp")
print(output)
net_conn.disconnect()

cfg_commands = ['get sys status','get sys ha status']
output=net_conn.send_config_set((cfg_commands))

output = net_conn.commit()
print(output)

output = net_conn.exit_config_mode()
print(output)

output=net_conn.send_config_from_file("file.txt")

print()
print('-'*80)
print(output)
print('-'*80)
print()

output = net_conn.write_channel("show ip arp\n")
# add time.sleep()
output = net_conn.read_channel()

#ssh -L 33333:172.17.32.11:3389 -l sbheemanathini 10.9.18.11

import jinja2

bgp_vars ={
    "local_as": 10,
    "peer1_ip": "10.255.255.2",
    "peer1_as": 20,
    "advertised_route1": "10.10.200.0/24",
}

bgp_template = '''
feature bgp 
router bgp {{local_as}}
    address-family ipv4 unicast
        network {{advertised_route1}}
    neighbor {{peer1_ip}} remote-as {{peer1_as}}
        update-source loopback1
        ebgp-multihop 2
        address-family ipv4 unicast

'''

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))
















