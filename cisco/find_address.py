import re

def filter_internet_address(filename):
    pattern = re.compile('((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
    with open(filename, 'r') as arp_file:
        for line in arp_file:
            match = re.search(pattern, line)
            if match:
                print(match.group())


def main():
    filename = "arp_list.txt"
    filter_internet_address(filename)

if __name__ == "__main__":
    main()