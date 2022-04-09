from napalm import get_network_driver

sandbox = {
    'host': '10.10.20.48',
    'device_type': 'cisco_ios',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22
}

gns3_ios_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.140',
    'username': 'devnet',
    'password': 'devnet',
    'port': 22
}

gns3_junos_vsrx = {
    'device_type': 'juniper_junos',
    'host': '192.168.122.150',
    'username': 'devnet',
    'password': 'Devnet',
    'port': 22
}

driver = get_network_driver("junos")
device = driver(hostname=gns3_junos_vsrx['host'],
                username=gns3_junos_vsrx['username'],
                password=gns3_junos_vsrx['password'],
                optional_args={'port': gns3_junos_vsrx['port']})

device.open()
interfaces = device.get_interfaces()
print(interfaces)
