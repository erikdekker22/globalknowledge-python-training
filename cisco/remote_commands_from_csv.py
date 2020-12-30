import netmiko, os, csv

def connect_host():

    with open('devices.csv', 'r') as txt_devices:
        devices = csv.DictReader(txt_devices, delimiter=',')
        for device in devices:
            net_connect = netmiko.ConnectHandler(
                              device_type=device['device_type'],
                              host=device['host'],
                              username=device['username'],
                              password=device['password'],
                              port=device['port'],
                              secret=device['secret'])
            execute_commands(device['host'],net_connect)


def write_to_file(filename, result):
    filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", filename)
    with open(filename, 'w+') as router_name_file:
        router_name_file.write(result)

def execute_commands(hostname,net_connect):
    with open ("commands.txt", 'r') as commands:
        for command in commands:
            if not os.path.exists:
                os.mkdir(os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", hostname))
                filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", hostname, command.rstrip() + '.txt')
                print('Created the following: ' + filename)
                output = net_connect.send_command(command)
                write_to_file(filename, output)
            else:
                filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", hostname, command.rstrip() + '.txt')
                print('Created the following: ' + filename)
                output = net_connect.send_command(command)
                write_to_file(filename, output)

def main():
    connect_host()

if __name__ == "__main__":
    main()