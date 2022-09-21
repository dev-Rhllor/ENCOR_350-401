from pprint import pprint
from netmiko import ConnectHandler
from inventory import gns3_ios_router
# from inventory import gns3_junos_vsrx


def main():
    cisco_command = 'show interface'
    # junos_command = 'show interface'
    device_connection = ConnectHandler(**gns3_ios_router)
    device_interface = device_connection.send_command(cisco_command)
    print(device_interface)

    device_interface_parsed = device_connection.send_command(cisco_command, use_textfsm=True)
    pprint(device_interface_parsed)


if __name__ == "__main__":
    main()
