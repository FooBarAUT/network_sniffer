from getmac import get_mac_address
import socket


def get_mac_from_ip(ip):
    mac = get_mac_address(ip=ip)
    return mac


def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
    except Exception:
        hostname = ["None"]

    return hostname
