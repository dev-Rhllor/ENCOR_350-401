from netmiko import ConnectHandler
from inventory import gns3_ios_router


def main():
    device_connection = ConnectHandler(**gns3_ios_router)

    # Using the "send config from file function"
    # device_connection.send_config_from_file('cisco_config.txt')

    # Using the "send config set" function
    with open('cisco_config.txt', encoding="utf-8") as file:
        config_set = file.read().splitlines()
    output = device_connection.send_config_set(config_set)
    if "%" in output:
        print(f"problem in config_set sent \n {output}")
    device_ip_parsed = device_connection.send_command("show ip interface brief", use_textfsm=True)
    print(device_ip_parsed)


if __name__ == "__main__":
    main()
