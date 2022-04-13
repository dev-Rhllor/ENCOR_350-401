from napalm import get_network_driver
from inventory import gns3_junos_vsrx
# from inventory import gns3_ios_router


def main():
    driver = get_network_driver("junos")
    device = driver(hostname=gns3_junos_vsrx['host'],
                    username=gns3_junos_vsrx['username'],
                    password=gns3_junos_vsrx['password'],
                    optional_args={'port': gns3_junos_vsrx['port']})

    device.open()
    interfaces = device.get_interfaces()
    print(interfaces)


if __name__ == "__main__":
    main()
