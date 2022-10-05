import json
from pprint import pprint
from netmiko import ConnectHandler
from inventory import gns3_ios_router
from inventory import gns3_junos_vsrx


def main():
    ios_command = 'show ip interface brief'
    device_connection = ConnectHandler(**gns3_ios_router)
    interfaces = device_connection.send_command(ios_command)
    print(interfaces)

    interfaces_parsed = device_connection.send_command(ios_command, use_textfsm=True)
    pprint(interfaces_parsed)


    junos_command = 'show interface terse | display json'
    device_connection = ConnectHandler(**gns3_junos_vsrx)
    interfaces = device_connection.send_command(junos_command)
    print(interfaces)
    pprint(json.loads(interfaces))


if __name__ == "__main__":
    main()
