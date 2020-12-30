import netmiko, os

def execute_command(command):
    # Below is not ideal, but for testing purposes fine.
    net_connect = netmiko.ConnectHandler(
                      device_type='cisco_ios',
                      host='ios-xe-mgmt.cisco.com',
                      username='developer',
                      password='C1sco12345',
                      port=8181,
                      secret='')
    output = net_connect.send_command(command)
    return output

def write_to_file(filename, result):
    filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", filename)
    with open(filename, 'w+') as router_name_file:
        router_name_file.write(result)

def get_interfaces():
    command = 'show ip int brief'
    filename = 'interfaces.txt'
    result = execute_command(command)
    write_to_file(filename, result)

def get_arp_list():
    command = 'show arp'
    filename = 'arp.txt'
    result = execute_command(command)
    write_to_file(filename, result)

def main():
    get_interfaces()
    get_arp_list()

if __name__ == "__main__":
    main()