def print_indexed_names(servers):
    for counter, item in enumerate(servers):
        print(counter, item[0])

def ask_index(max_index):
    index_value = int(input("Please specify an index number: "))
    while (index_value >= max_index) or (index_value <= 0 - max_index):
        print("You entered an incorrect value!")
        index_value = int(input("Please specify an index number: "))
    else:
        return index_value


def print_properties(index, servers):
    return servers[index]

def main():
    servers = [ ["Amsterdam", '192.168.178.3', '255.255.255.0'],
                ["Tokyo", '192.168.178.8', '255.255.255.0'],
                ["Paris",  '192.168.178.12', '255.255.255.0'],
                ["Helsinki",  '192.168.178.145', '255.255.255.0'],
                ["Brussel",  '192.168.178.12', '255.255.255.0']]

    print_indexed_names(servers)
    max_index = len(servers) - 1
    index = ask_index(max_index)
    specified_server = print_properties(index, servers)
    print(specified_server)

if __name__ == "__main__":
    main()