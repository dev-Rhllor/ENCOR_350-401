netconf_ietf_interfaces = """
<interfaces xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
      <interface>
          <name>GigabitEthernet2</name>
      </interface>
</interfaces>
"""

netconf_ietf_interfaces_status = """
<interfaces-state xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
  <interface>
    <name>GigabitEthernet2</name>
  </interface>
</interfaces-state>
"""

# IOSXE Requires a default Namespace in the Config tag #
netconf_ietf_interfaces_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
    <interface>
      <name>{name}</name>
      <description>{description}</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
        {type}
      </type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>{ip_address}</ip>
          <netmask>{mask}</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""
netconf_ietf_interfaces_delete = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>{name}</name>
        </interface>
    </interfaces>
</config>"""

netconf_native_memory_statistics = """
<memory-statistics xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-memory-oper'>
</memory-statistics>
"""