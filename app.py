from src import macadress
from src import ping
import sys

modeChoice = int(
    input("\nChoose:\n1 - full (1-254) or\n2 - partial mode (custom range)\n\n|> "))
safeChoice = input(
    "Activate safe-mode or flood network?\n\nyes - safe-mode\nno - no timeout between pings\n\n|> ")

if(safeChoice.lower() == 'yes'):
    safe = True
elif(safeChoice.lower() == 'no'):
    safe = False
else:
    print("\nInvalid input, defaulting to safe-mode ...\n")
    safe = True

if (modeChoice == 1):
    results = ping.get_confirmed_adresses(1, 254, safe)
elif (modeChoice == 2):
    start = int(input("\nEnter the first adress to scan: "))
    end = int(input("Enter the last adress: "))
    results = ping.get_confirmed_adresses(start, end, safe)
else:
    sys.exit(
        "\nInvalid choice!\nPlease choose either 1 (full) or 2 (partial mode).\n")

for ip in results:
    mac = macadress.get_mac_from_ip(ip)
    hostname = macadress.get_hostname(ip)

    print("\n{}\nHostname: '{}'\nMAC-adress: {}"
          .format(ip, hostname[0], mac))
