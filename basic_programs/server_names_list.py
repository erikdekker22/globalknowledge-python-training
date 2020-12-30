def add_some(servers):
    servers.append('Helsinki')
    servers.insert(servers.index('Paris'), 'Tokyo')
    return servers

def get_five_letter_servers(servers):
    five_letter_names = []  # fixture
    for server in servers:
        if len(server) == 5:
            five_letter_names.append(server)
    return five_letter_names


def print_reverse(a_list):
    new_list = []
    for server in a_list:
        new_list.insert(0, server)
    return new_list

def main():
    servers = ['Amsterdam', 'Tokyo', 'Paris', 'Brussel']
    temp_list = add_some(servers)
    print(temp_list)

    filtered = get_five_letter_servers(temp_list)
    print(filtered)

    reversed_list = print_reverse(temp_list)
    print(reversed_list)


if __name__ == "__main__":
    main()