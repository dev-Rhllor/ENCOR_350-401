import paramiko
import re
# from inventory import gns3_ios_router
from inventory import sandbox


def main():
    command = 'show ip interface brief \n'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=sandbox['host'],
                username=sandbox['username'],
                password=sandbox['password'],
                port=sandbox['port'],
                look_for_keys=False,
                allow_agent=False)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    print(" ".join(output))

    regex = re.compile('(?P<interface>\S+) +(?P<ip>\S+) +\S+ +\S+ +\S+')
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
