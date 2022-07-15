import requests
import json
from pprint import pprint
from inventory import sandbox

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()


def main():

      headers = {'Content-Type': 'application/yang-data+json',
                 'Accept': 'application/yang-data+json'}    
      base_url = f"https://{sandbox['host']}:443/restconf/data"   

      # Send a get to retrieve ieft-interfaces standard yang model.
      resource = '/ietf-interfaces:interfaces/interface=GigabitEthernet2'
      response = requests.get(url=f'{base_url}{resource}',
                              auth=(sandbox['username'],
                                    sandbox['password']),
                              headers=headers,
                              verify=False)
      interfaces_ietf_dict = json.loads(response.content)
      interface_description= interfaces_ietf_dict['ietf-interfaces:interface']['description']
      print(f"Interface description for GigabitEthernet2 is {interface_description}")
      

      # Send a get to retrieve ieft-interfaces oper-status from interface standard yang model.
      resource = '/ietf-interfaces:interfaces-state/interface=GigabitEthernet2'
      response = requests.get(url=f'{base_url}{resource}',
                              auth=(sandbox['username'],
                                    sandbox['password']),
                              headers=headers,
                              verify=False)
      interfaces_ietf_status_dict = json.loads(response.content)
      interfaces_ietf_status = interfaces_ietf_status_dict['ietf-interfaces:interface']['oper-status']
      print(f"Interface operation status for GigabitEthernet2 is {interfaces_ietf_status}")
      
      # Send a get to retrieve IOS-XE Memory Statistics from the Native yang model.
      resource = '/Cisco-IOS-XE-memory-oper:memory-statistics/memory-statistic/'
      response = requests.get(url=f'{base_url}{resource}',
                              auth=(sandbox['username'],
                                    sandbox['password']),
                              headers=headers,
                              verify=False)
      memory_statistics_dict = json.loads(response.content)
      pprint(memory_statistics_dict['Cisco-IOS-XE-memory-oper:memory-statistic'])



if __name__ == '__main__':
    main()
