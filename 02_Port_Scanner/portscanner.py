import socket
from IPy import IP


def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' is Open')
    except:
        print('[-] Port' + str(port) + ' is Closed')


ipaddress = input('[+] Enter Target to Scan: ')

for port in range(75, 85):
    scan_port(ipaddress, port)
