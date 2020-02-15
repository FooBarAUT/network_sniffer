from src import macadress
from src import ping
import sys

choice = int(
    input("\nChoose:\n1 - full (1-254) or\n2 - partial mode (custom range)\n\n|> "))

if (choice == 1):
    results = ping.get_confirmed_adresses(1, 254)
elif (choice == 2):
    start = int(input("\nEnter the first adress to scan: "))
    end = int(input("Enter the last adress: "))
    results = ping.get_confirmed_adresses(start, end)
else:
    sys.exit("\nInvalid choice!\n(Is it really that hard to hit 1 or 2?\n")

for ip in results:
    mac = macadress.get_mac_from_ip(ip)
    hostname = macadress.get_hostname(ip)

    print("\n{}\nHostname: '{}'\nMAC-adress: {}"
          .format(ip, hostname[0], mac))
