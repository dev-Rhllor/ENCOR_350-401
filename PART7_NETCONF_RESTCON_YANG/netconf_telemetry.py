from ncclient import manager
import xmltodict
from lxml.etree import fromstring
from inventory import sandbox

# This generates a dynamic telemetry subscription, when the session is over,
# the subscription is erased from the device.
# Another approach is to configure the telemetry subscription in the device
# and then configure a collector using telegraf to receive the telemetry.

def main():

    with manager.connect(**sandbox, hostkey_verify=False) as m:

        rpc = """
            <establish-subscription xmlns='urn:ietf:params:xml:ns:yang:ietf-event-notifications'
                                    xmlns:yp='urn:ietf:params:xml:ns:yang:ietf-yang-push'>
                <stream>yp:yang-push</stream>
                <yp:xpath-filter>/memory-ios-xe-oper:memory-statistics/memory-statistic</yp:xpath-filter>
                <yp:period>500</yp:period>
            </establish-subscription>
        """
        m.dispatch(fromstring(rpc))

        while True:
            sub_data = m.take_notification()
            python_sub_data = xmltodict.parse(sub_data.notification_xml)
            print(
                f"Sub ID: {python_sub_data['notification']['push-update']['subscription-id']}")
            print(
                f"Name:\
                    {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['name']}")
            print(
                f"Total RAM:\
                    {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['total-memory']}")
            print(
                f"Used RAM:\
                    {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['used-memory']}")
            print(
                f"Free RAM:\
                    {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['free-memory']}")

if __name__ == '__main__':
    main()
    