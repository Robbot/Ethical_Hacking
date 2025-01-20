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


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
            # decode and strip to avoid rubbish but banner would be enough to get response
        except:
            print('[+] Open port ' + str(port))
    except:
        # print('[-] Port ' + str(port) + ' is Closed')
        pass


if __name__ == "__main__":
    targets = input('[+] Enter Target/s to Scan (split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
