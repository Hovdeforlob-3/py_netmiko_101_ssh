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
print(net_conn.find_prompt())


# moves to conf t (configure terminal) mode
net_conn.config_mode()
# printer hvilken mode det er i
print(net_conn.find_prompt())


def exit_to_user_mode():
    mode_state = net_conn.find_prompt()
    if mode_state.__contains__("config"):
        net_conn.exit_config_mode()
        net_conn.exit_enable_mode()

    elif mode_state.__contains__("#"):
        net_conn.exit_enable_mode()


def set_hostname(name):
    net_conn.send_command("hostname " + name, expect_string=r"#", delay_factor=2)


# R_py#copy run start
# Destination filename [startup-config]?
# Building configuration...
# [OK]
# R_py#
def copy_run_start():
    exit_to_user_mode()
    net_conn.enable()

    output = net_conn.send_command_timing("copy run start")
    print(output)
    if "startup-config" in output:
        output += net_conn.send_command_timing("\n")
        print("from if \n", output)


def config_set_test():
    exit_to_user_mode()
    net_conn.enable()

    cfg_commands = ["int g0/0", "ip add 10.0.1.1 255.255.255.0", "no shutdown"]
    output20 = net_conn.send_config_set(cfg_commands)
    print(output20)


def config_from_file():
    exit_to_user_mode()
    net_conn.enable()

    output = net_conn.send_config_from_file("Test.txt")
    print(output)


config_from_file()

# print("Exiting ...")
# exit_to_user_mode()

# set_hostname("R_py")
# print(net_conn.find_prompt())
# copy_run_start()
# print(net_conn.find_prompt())

# config_set_test()
# print(net_conn.find_prompt())
# output = net_conn.send_command("sh ip int brief")
# print(output)

net_conn.disconnect()
