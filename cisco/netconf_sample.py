from ncclient import manager
import xmltodict
import csv

def connect_host():

    with open('devices.csv', 'r') as txt_devices:
        devices = csv.DictReader(txt_devices, delimiter=',')
        for device in devices:
           with manager.connect(
                              host=device['host'],
                              username=device['username'],
                              password=device['password'],
                              port=device['port'],
                              hostkey_verify=False) as m:
    netconf_reply = m.get()








def main():
    connect_host()


if __name__ == "__main__":
    main()