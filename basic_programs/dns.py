import json

def user_interact():
    dns = {}
    hostname = ''
    while 'q' != hostname:
        hostname = ask_user_hostname()
        if ('q' != hostname) and (hostname not in dns):
            ip = ask_user_ip()
            print_dns(hostname, ip)
            dns = add_to_dns(dns,hostname, ip)
        elif hostname in dns:
            decide = input("Do you want to overwrite the value of key: [y or n]")
            if decide == 'y':
                ip = ask_user_ip()
                print_dns(hostname, ip)
                dns[hostname] = ip
            else:
                hostname = ''
        else:
            print("You entered q to quit")
            break
    else:
        print("OK, You decided to quit.")
    return dns

def ask_user_hostname():
    hostname = input("Please enter the hostname here: [press q to quit]").lower()
    return hostname

def ask_user_ip():
    ip = input("Please enter the IP address here: ").lower()
    return ip

def print_dns(hostname, ip):
    print("You just entered:")
    print('  - Hostname: ', hostname)
    print('  -       IP: ',ip)

def add_to_dns(dns,hostname, ip):
    dns[hostname] = ip
    return dns

def save_to_json(dictionary):
    with open('data.json', 'w') as fp:
        json.dump(dictionary, fp, indent=4, sort_keys=True)

def read_json_file():
    with open ('data.json', 'r') as fp:
        pretty_print = json.load(fp)
        return pretty_print

def main():
    dns = user_interact()
    print(dns)
    save_to_json(dns)
    json_output = read_json_file()
    print(json_output)


if __name__ == "__main__":
    main()