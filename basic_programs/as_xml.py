def indent(content, spaces=2):
    '''implementeer'''
    returnvalue = spaces * ' ' + content
    return returnvalue


def as_xml(content, tag_name):
    returnvalue = '<' + tag_name + '>' +content + '</' + tag_name + '>'
    return returnvalue


def main():
    name = "Paris"
    ip = "10.0.0.135"
    xml_name = as_xml(name, "name")
    xml_ip = as_xml(ip, "ip4")

    print(indent(xml_name))
    print(indent(xml_ip, 4))


if __name__ == "__main__":
    main()