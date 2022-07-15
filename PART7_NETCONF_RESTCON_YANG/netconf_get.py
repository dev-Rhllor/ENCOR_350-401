from pprint import pprint
from ncclient import manager
import xmltodict
from inventory import sandbox


def main():

    with manager.connect(**sandbox, hostkey_verify=False) as m:

        # Send a get-config to retrieve ieft-interfaces standard yang model.
        netconf_ietf_interfaces = """
        <interfaces xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
            <interface>
                <name>GigabitEthernet2</name>
            </interface>
        </interfaces>
        """
        interfaces_ietf = m.get_config(source="running",
                                       filter=("subtree", netconf_ietf_interfaces))
        interfaces_ietf_dict = xmltodict.parse(interfaces_ietf.data_xml)
        interface_description = interfaces_ietf_dict['data']['interfaces']['interface']['description']
        print(f"Interface description for GigabitEthernet2 is {interface_description}")
        
        # Send a get to retrieve ieft-interfaces oper-status from interface standard yang model.
             
        ## using subtree filter
        netconf_ietf_interfaces_status = """
        <interfaces-state xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
        </interfaces-state>
        """
        interfaces_ietf_status = m.get(("subtree", netconf_ietf_interfaces_status))
        interfaces_ietf_status_dict = xmltodict.parse(interfaces_ietf_status.data_xml)
        interfaces_ietf_status = interfaces_ietf_status_dict['data']['interfaces-state']['interface']['oper-status']
        print(f"Interface operation status for GigabitEthernet2 is {interfaces_ietf_status}")

        ## using xpath filter
        assert ":xpath" in m.server_capabilities
        netconf_xpath_selection = "//interfaces-state/interface[name='GigabitEthernet2']"
        netconf_xpath = m.get(filter=('xpath',netconf_xpath_selection))
        netconf_xpath_dict = xmltodict.parse(netconf_xpath.data_xml)
        netconf_xpath_ietf_status = netconf_xpath_dict['data']['interfaces-state']['interface']['oper-status']
        print(f"Interface operation status for GigabitEthernet2 is {netconf_xpath_ietf_status}")

        # Send a get to retrieve IOS-XE Memory Statistics from the Native yang model.
        netconf_native_memory_statistics = """
        <memory-statistics xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-memory-oper'>
        </memory-statistics>
        """
        native_memory_statistics = m.get(filter=("subtree", netconf_native_memory_statistics))
        native_memory_statistics_dict = xmltodict.parse(native_memory_statistics.data_xml)
        pprint(native_memory_statistics_dict['data']['memory-statistics']['memory-statistic'])


if __name__ == '__main__':
    main()