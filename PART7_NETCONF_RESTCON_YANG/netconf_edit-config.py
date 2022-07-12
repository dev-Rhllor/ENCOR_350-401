from ncclient import manager
from ncclient.xml_ import to_ele
from inventory import sandbox
from NetconfFilters import (
    netconf_ietf_interfaces_config,
    netconf_ietf_interfaces_delete
)

def main():

    with manager.connect(**sandbox, hostkey_verify=False) as m:

        # Creating a loopback using a template and config RPC
        with m.locked("candidate"):
            interface_config = netconf_ietf_interfaces_config.format(name='Loopback1',
                                                                     description='Loopback1 netconf',
                                                                     type= 'ianaift:softwareLoopback',
                                                                     ip_address='1.1.1.1',
                                                                     mask='255.255.255.255')
            change_reply = m.edit_config(interface_config, target="candidate")
            if change_reply.ok:
                m.commit()
                print("Change done")

        # Rollback
        with m.locked("candidate"):
            interface_config = netconf_ietf_interfaces_delete.format(name='Loopback1')
            change_reply = m.edit_config(interface_config, target="candidate")
            if change_reply.ok:
                m.commit()
                print("Rollback done")


        # Save the config using custom craft rpc
        save_body = """<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>"""
        rpc_replay = m.dispatch(to_ele(save_body))
        if rpc_replay.ok:
            print("Save running-config successful")


if __name__ == '__main__':
    main()