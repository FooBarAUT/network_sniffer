import platform
import os


def ping_ip(ip):
    if (platform.system() == "Windows"):
        pingcommand = "ping -n 1 -w 5 "
    else:
        pingcommand = "ping -c 1 -w 5 "

    response = os.system(pingcommand + ip)
    return response


def get_confirmed_adresses(start, end):
    confirmed_adresses = []

    for i in range(start, (end + 1)):
        ip = "192.168.0." + str(i)
        response = ping_ip(ip)

        if response == 0:
            confirmed_adresses.append(ip)
        else:
            pass

    return confirmed_adresses
