from netmiko import ConnectHandler
from inventory import gns3_ios_router
# from inventory import gns3_junos_vsrx


def main():
    cisco_command = 'show ip interface brief'
    # junos_command = 'show interface'
    device_connection = ConnectHandler(**gns3_ios_router)
    device_ip = device_connection.send_command(cisco_command)
    print(device_ip)

    device_ip_parsed = device_connection.send_command(cisco_command, use_textfsm=True)
    print(device_ip_parsed)


if __name__ == "__main__":
    main()
