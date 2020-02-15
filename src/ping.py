from random import randint
import platform
import time
import os


def ping_ip(ip):
    if (platform.system() == "Windows"):
        pingcommand = "ping -n 1 -w 5 "
    else:
        pingcommand = "ping -c 1 -w 5 "

    response = os.system(pingcommand + ip)
    return response


def get_confirmed_adresses(start, end, safe):
    confirmed_adresses = []

    for i in range(start, (end + 1)):
        ip = "192.168.0." + str(i)
        if(safe):
            print("\nSleeping ...\n")
            time.sleep(randint(1, 5))
        response = ping_ip(ip)

        if response == 0:
            confirmed_adresses.append(ip)
        else:
            pass

    return confirmed_adresses
