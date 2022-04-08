from napalm import get_network_driver

sandbox = {
    'host': '10.10.20.48',
    'device_type': 'cisco_ios',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22
}

driver = get_network_driver("ios")
device = driver(hostname=sandbox['host'],
                username=sandbox['username'],
                password=sandbox['password'],
                optional_args={'port': sandbox['port']})

device.open()
interfaces = device.get_interfaces()
