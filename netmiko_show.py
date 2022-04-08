from netmiko import ConnectHandler
# import logging
# logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")


gns3_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.144',
    'username': 'devnet',
    'password': 'devnet',
    'secret': 'devnet',
    'port': 22
}

sandbox = {
    'host': '10.10.20.48',
    'device_type': 'cisco_ios',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22
}

sandbox_connection = ConnectHandler(**sandbox)
sandbox_ip = sandbox_connection.send_command('show ip interface brief')
print(sandbox_ip)
sandbox_ip_parsed = sandbox_connection.send_command('show ip interface brief', use_textfsm=True)
print(sandbox_ip_parsed)
