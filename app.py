from datetime import datetime
from src import macadress
from src import ping

start = int(input("Enter the first adress to scan: "))
end = int(input("Enter the last adress: "))

starttime = datetime.now()

result = ping.get_confirmed_adresses(start, end)

endtime = datetime.now()

print(result)
print("\nGot result in: " + str(endtime - starttime) + "\n")
