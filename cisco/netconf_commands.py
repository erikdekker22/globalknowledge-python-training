import xmltodict, json, os
from ncclient import manager
from netconf_credentials import device


def get_device_configuration(device, data_store="running"):
    with manager.connect(host=device['host'],
                         port=device['port'],
                         username=device['username'],
                         password=device['password'],
                         hostkey_verify=False) as m:
        reply = m.get_config(data_store)
        return reply.xml


def write_to_file(filename, result):
    filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data/netconf_data", filename)
    with open(filename, 'w+') as router_name_file:
        router_name_file.write(result)


def dict_to_pretty_xml(dictionary):
    ''' converteer de dictionary naar xml met xmltodict.unparse().'''
    return xmltodict.unparse(dictionary, pretty=True)


def dict_to_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


def main():
    xml_data = get_device_configuration(device, 'running')
    write_to_file(filename='device_config.xml', result=xml_data)

    data = xmltodict.parse(xml_data)
    print()
    print("Here begins normal data")
    print(data)

    pretty_xml = dict_to_pretty_xml(data)
    print()
    print("Here begin pretty xml data")
    print(pretty_xml)
    write_to_file(filename='pretty_device_config.xml', result=pretty_xml)

    pretty_json = dict_to_json(data)
    print()
    print("Here begin pretty JSON data")
    print(pretty_json)
    write_to_file(filename='pretty_device_config.json', result=pretty_json)


if __name__ == "__main__":
    main()