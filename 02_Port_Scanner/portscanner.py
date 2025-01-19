import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[- 0 Scanning Target] ' + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)


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


targets = input('[+] Enter Target/s to Scan (split multiple targets with ,): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
