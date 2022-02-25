from netmiko import ConnectHandler
from getpass import getpass
import os
import yaml

# Enable logging to understand the underling paramiko ssh handler connections:
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
        #print(device_dict)
    return device_dict


if __name__ == "__main__":
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

device_dict = load_devices()
jumphost = device_dict["jumphost"]

cfg_changes = ["who"]

for device in (jumphost,):
    device["password"] = password
    device["secret"] = password
    net_connect = ConnectHandler(**device)
    output=net_connect.enable(cmd='sudo su',pattern='password')
    output+= net_connect.send_config_set(cfg_changes)
    print(output)
    net_connect.disconnect()