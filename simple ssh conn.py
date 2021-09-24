from netmiko import Netmiko

my_device = {
    "host": "192.168.1.1",
    "username": "py",
    "password": "cisco",
    "device_type": "cisco_ios"
}

net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())