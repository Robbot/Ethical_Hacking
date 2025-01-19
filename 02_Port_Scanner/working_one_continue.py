import socket
from IPy import IP


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open')
    except:
        print('[-] Port ' + str(port) + ' is Closed')


ipaddress = input('[+] Enter Target to Scan: ')
converted_ip = check_ip(ipaddress)

for port in range(75, 85):
    scan_port(converted_ip, port)
