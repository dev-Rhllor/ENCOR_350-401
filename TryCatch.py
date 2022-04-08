from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException
# import logging
# logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")


def main():
    sandbox_router = {
        'device_type': 'cisco_ios',
        'host': '192.168.122.144',
        'username': 'devnet',
        'password': 'devnet',
        'secret': 'devnet',
        'port': 22
    }
    try:
        sandbox_connection = ConnectHandler(**sandbox_router)
        sandbox_ip = sandbox_connection.send_command(
            'show ip interface brief')
        print(sandbox_ip)
        interface_configuration = ['interface gi0/1',
                                   'description configured using netmiko',
                                   'no switchport',
                                   'ip address 1.1.1.1 255.255.255.0']
        sandbox_connection.send_config_set(interface_configuration)
        sandbox_ip = sandbox_connection.send_command('show ip interface brief')
        print(sandbox_ip)
    except NetmikoTimeoutException as Err:
        if "TCP connection to device failed" in str(Err):
            print(Err)
        elif "Timed-out reading channel, data not available" in str(Err):
            sandbox_connection = ConnectHandler(**sandbox_router)
            sandbox_connection.enable()
            line_vty = sandbox_connection.send_command("show run | b line vty")
            print(Err)
            print("maybe is because is not entering in configuration mode")
            print(line_vty)


if __name__ == '__main__':
    main()
