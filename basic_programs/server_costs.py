

def main():
    vps_price = float(input("Type her your VPS price : "))
    amount_of_servers = int(input("Type her the amount of VPS servers you want : "))
    configure_time = float(input("How long does it take to configure a server (in minutes)? : "))

    server_price = vps_price * amount_of_servers
    configure_price = (configure_time * amount_of_servers) * (84.00 / 60)
    total_price = server_price + configure_price
    rounded_total_price = round(total_price,2)

    print("The total cost for " + str(amount_of_servers) + " is " + str(rounded_total_price) +  " euro.")

main()