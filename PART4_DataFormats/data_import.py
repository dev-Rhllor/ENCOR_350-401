import json
import yaml
import xmltodict

def json_importer():
    with open('./PART4_DataFormats/inventory.json') as file:
        inventory = json.load(file)
        return inventory

def yaml_importer():
    with open('./PART4_DataFormats/inventory.yaml') as file:
        inventory = yaml.load(file, Loader=yaml.FullLoader)
        return inventory

def xml_importer():
    with open('./PART4_DataFormats/inventory.xml') as file:
        xml_inventory = file.read()
        inventory = xmltodict.parse(xml_inventory)
        return inventory


def main():
    inventory_from_json = json_importer()
    inventory_from_yaml = yaml_importer()
    inventory_from_xml = xml_importer()
    print(inventory_from_json['devices']['sandbox']['local'])
    print(inventory_from_yaml['devices']['sandbox']['local'])
    print(inventory_from_xml['devices']['sandbox']['local'])
    print(inventory_from_xml['devices']['sandbox']['@id'])

    # Importing from json from strings

    sandbox = """
    {
        "local": false,
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "device_type": "cisco_ios",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22
    }
    """
    print(json.load(sandbox.read()))


if __name__ == "__main__":
    main()




