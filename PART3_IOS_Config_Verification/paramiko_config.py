import paramiko
import time
from inventory import gns3_ios_router


def main():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=gns3_ios_router['host'],
                username=gns3_ios_router['username'],
                password=gns3_ios_router['password'],
                port=gns3_ios_router['port'],
                look_for_keys=False,
                allow_agent=False)

    with open('cisco_config.txt') as file:
        config_set = file.read().splitlines()

    interactive_shell = ssh.invoke_shell()
    interactive_shell.send("config terminal \n")
    time.sleep(2)
    for config_line in config_set:
        print(f"sending {config_line}")
        command = config_line + '\n'
        interactive_shell.send(command)
        output = interactive_shell.recv(65535)
        print(output)
        time.sleep(2)
    
    ssh.close()


if __name__ == "__main__":
    main()
