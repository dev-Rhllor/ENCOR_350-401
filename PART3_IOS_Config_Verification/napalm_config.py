from napalm import get_network_driver
from inventory import gns3_ios_router


def main():
    driver = get_network_driver("ios")
    device = driver(hostname=gns3_ios_router['host'],
                    username=gns3_ios_router['username'],
                    password=gns3_ios_router['password'],
                    optional_args={'port': gns3_ios_router['port']})
    device.open()
    device.load_merge_candidate(filename='cisco_config.txt')
    print(device.compare_config())
    device.commit_config()
    interfaces = device.get_interfaces_ip()
    print(interfaces)
    device.close()


if __name__ == "__main__":
    main()
