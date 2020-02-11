from datetime import datetime
from src import macadress
from src import ping

start = int(input("Enter the first adress to scan: "))
end = int(input("Enter the last adress: "))

starttime = datetime.now()

results = ping.get_confirmed_adresses(start, end)

for ip in results:
    mac = macadress.get_mac_from_ip(ip)
    hostname = macadress.get_hostname(ip)

    print("\n{} has hostname {} and MAC adress {}.\n"
          .format(ip, hostname[0], mac))

endtime = datetime.now()

print("\nGot result in: " + str(endtime - starttime) + "\n")
