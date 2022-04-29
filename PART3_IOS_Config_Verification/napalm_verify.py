from napalm import get_network_driver
from inventory import gns3_ios_router


def main():
    driver = get_network_driver("ios")
    with driver(hostname=gns3_ios_router['host'], 
                username=gns3_ios_router['username'],
                password=gns3_ios_router['password'],
                optional_args={'port': gns3_ios_router['port']}) as device:
        result = device.compliance_report('cisco_verification.yaml')
        print(result)

if __name__ == "__main__":
    main()
