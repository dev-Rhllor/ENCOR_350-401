import json
import requests
from inventory import sandbox

requests.packages.urllib3.disable_warnings()

def main():

    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    base_url = f"https://{sandbox['host']}:443/restconf/data"

    # CONFIGURE LOOPBACK
    ## Format the RESTCONF template with the values
    parameters = json.dumps({
        "ietf-interfaces:interface": {
            "name": "Loopback1",
            "description": "Dev-Rhllor created this using RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
            "address": [
                {
                "ip": "1.1.1.1",
                "netmask": "255.255.255.255"
                }
            ]
            }
        }
    })
    resource = '/ietf-interfaces:interfaces'
    response = requests.post(url=f'{base_url}{resource}',
                             auth=(sandbox['username'],
                                   sandbox['password']),
                             headers=headers,
                             data=parameters,
                             verify=False)

    if response.ok is True:
        print('Change done')
    else:
        print(f'Failed with error {response.reason}')

    # REMOVE LOOPBACK
    resource = '/ietf-interfaces:interfaces/interface=Loopback1'
    response = requests.delete(url=f'{base_url}{resource}',
                               auth=(sandbox['username'],
                                     sandbox['password']),
                               headers=headers,
                               verify=False)
    if response.ok is True:
        print('Change done')
    else:
        print(f'Failed with error {response.reason}')

    # SAVE RUNNING CONFIGURATION
    url = f"https://{sandbox['host']}:443/restconf/operations/cisco-ia:save-config/"
    response = requests.post(url,
                  headers=headers,
                  auth=(sandbox['username'],
                        sandbox['password']),
                  data={},
                  verify=False)
    if response.ok is True:
        print('Save running-config successful')
    else:
        print(f'Failed with error {response.reason}')


if __name__ == '__main__':
    main()
