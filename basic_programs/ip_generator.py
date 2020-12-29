import sys

def ask_number(minimum=0, max_tries=3):
    count = 0
    ip_address_amount = int(input("Please specify a value above the minimum (0)."))
    while (ip_address_amount <= 0) or (ip_address_amount > 255):
        if count < 3:
            print(count)
            print("Im sorry but this value is too small. Or above 255 \n")
            ip_start_value = int(input("Please specify again a value above the minimum (0)."))
            count += 1
        else:
            print("Maximum retires! Zero is used as your value now!")
            return 0
    else:
        return ip_address_amount

def generate_ip_addresses(ip_amount, start_octet, end_octet, base="192.168.178"):
    if ip_amount == 0:
        print("What are you doing? You did not ask for any IP addresses!")
        sys.exit(0)
    else:
        for i in range(ip_amount):
            if (i + start_octet) <= end_octet:
                print(str(base) + "." + str(i + start_octet))
            else:
                print("I\'m sorry, but there are not enough IP addresses.")
                break

def main():
    print("Hoeveel ip-adressen moeten er worden gemaakt?")
    ip_count = ask_number()

    print("Wat is het start-octet?")
    ip_start = ask_number(minimum=1, max_tries=2)
    print("Wat is het end-octet?")
    ip_end = ask_number()

    generate_ip_addresses(ip_count, ip_start, ip_end)

if __name__ == "__main__":
    main()