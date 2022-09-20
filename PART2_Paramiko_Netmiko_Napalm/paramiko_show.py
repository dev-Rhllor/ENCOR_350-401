import re
import paramiko
from inventory import gns3_ios_router

def main():
    command = 'show ip interface brief \n'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=gns3_ios_router['host'],
                username=gns3_ios_router['username'],
                password=gns3_ios_router['password'],
                port=gns3_ios_router['port'],
                look_for_keys=False,
                allow_agent=False)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    print(" ".join(output))

    regex = re.compile(r'(?P<interface>\S+) +(?P<ip>\S+) +\S+ +\S+ +\S+')
    result = []

    for line in output:
        match = regex.search(line)
        if match:
            result.append(match.groupdict())

    print(result)
    ssh.close()
    del ssh, stdin, stdout, stderr


if __name__ == "__main__":
    main()
