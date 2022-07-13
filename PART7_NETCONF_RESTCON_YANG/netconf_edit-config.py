from ncclient import manager
from ncclient.xml_ import to_ele
from inventory import sandbox
from NetconfFilters import (
    netconf_ietf_interfaces_config,
    netconf_ietf_interfaces_delete
)

def send_config(rpc,device):
    with manager.connect(**device, hostkey_verify=False) as m:
        m.lock('running')
        try:
            assert(':candidate' in m.server_capabilities)
            m.discard_changes()        
            with m.locked('candidate'):
                m.edit_config(rpc, target='candidate')
                m.commit()
                print('Change done')
        except AssertionError:
            print('No candidate datastore in the device')
        except Exception as e:
            print(f'Failed with error {e}')
        finally:
            m.unlock('running')

def save_config(device):
    # Save the config using custom craft rpc
    save_body = """<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>"""
    with manager.connect(**device, hostkey_verify=False) as m:
        try:
            m.dispatch(to_ele(save_body))
            print('Save running-config successful')
        except Exception as e:
                print(f'Failed with error {e}')

def main():

    # Format the RPC with the values
    interface_config = netconf_ietf_interfaces_config.format(name='Loopback1',
                                                             description='Dev-Rhllor created this loopback using NETCONF',
                                                             type= 'ianaift:softwareLoopback',
                                                             ip_address='1.1.1.1',
                                                             mask='255.255.255.255')

    # print(str(interface_config))
    send_config(interface_config,sandbox)      
    interface_delete = netconf_ietf_interfaces_delete.format(name='Loopback1')
    # print(str(interface_config_delete))
    send_config(interface_delete,sandbox) 
    save_config(sandbox)   

if __name__ == '__main__':
    main()