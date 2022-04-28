from napalm import get_network_driver
# from inventory import gns3_junos_vsrx
from inventory import gns3_ios_router
from pprint import pprint 


def main():
    driver = get_network_driver("ios") # "junos" for Juniper, "ios" for cisco 
    device = driver(hostname=gns3_ios_router['host'],
                    username=gns3_ios_router['username'],
                    password=gns3_ios_router['password'],
                    optional_args={'port': gns3_ios_router['port']})

    device.open()
    interfaces = device.get_interfaces_ip()
    pprint(interfaces)


if __name__ == "__main__":
    main()
