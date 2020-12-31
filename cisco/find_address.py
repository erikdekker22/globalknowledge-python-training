import re

def filter_internet_address(filename):
    ip_pattern = re.compile('((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
    with open(filename, 'r') as arp_file:
        for line in arp_file:
            match = re.search(ip_pattern, line)
            if match:
                print(match.group())

def filter_mac_address(filename):
    mac_pattern = re.compile('([0-9a-fA-F]){4}\.([0-9a-fA-F]){4}\.([0-9a-fA-F]){4}')
    with open(filename, 'r') as arp_file:
        for line in arp_file:
            match = re.search(mac_pattern, line)
            if match:
                print(match.group())

def main():
    filename = "arp_list.txt"
    filter_internet_address(filename)
    filter_mac_address(filename)

if __name__ == "__main__":
    main()