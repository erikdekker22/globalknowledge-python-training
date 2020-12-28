
def main():
    server_name = input("Please specify the server name here: ")
    server_ip_adres = input("Please specify the server IP adres here: ")
    server_mask = input("Please specify the netmask here: ")

    print("-----------")
    print(server_name, ",", server_ip_adres, ",", server_mask)
    print("===========")

    print("Server name: " + server_name + "\n" + "IP: " + server_ip_adres + "\n" "Netmask: " + server_mask)

main()