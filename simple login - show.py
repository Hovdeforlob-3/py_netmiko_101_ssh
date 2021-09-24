from netmiko import Netmiko

my_device = {
    "host": "192.168.1.1",
    "username": "py",
    "password": "cisco",
    "secret": "class",
    "device_type": "cisco_ios"
}
net_conn = Netmiko(**my_device)
net_conn.enable()


def sh_arp():
    output = net_conn.send_command("show arp")
    print(output)


def sh_interface_b():
    output = net_conn.send_command("show ip int brief")
    print(output)


sh_interface_b()

net_conn.disconnect()
