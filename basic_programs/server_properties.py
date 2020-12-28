
def main():
    server_name = input("Please specify the server name here: ").strip()
    server_ip_adres = input("Please specify the server IP adres here: ").strip()
    server_mask = input("Please specify the netmask here: ").strip()

    print("-----------")
    print(server_name.strip(), ",", server_ip_adres, ",", server_mask)
    print("===========")

    print("Server name: " + server_name + "\n" + "IP: " + server_ip_adres + "\n" "Netmask: " + server_mask)

main()