from netmiko import Netmiko

net_conn = Netmiko(host="192.168.1.1", username="py",
                   password="cisco", device_type="cisco_ios")

print(net_conn.find_prompt())
