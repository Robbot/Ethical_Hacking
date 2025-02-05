Arp spoofing is using scapy module, 
which documentation can be found here

https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb

For proper running it needs two parameters 
- packets destination
- packets router

ie. "python arpspoofer.py 192.168.1.1 192.168.1.2"

In the router (most likely Kali) add forwarding
- echo 1 >> /proc/sysnet/ipv4/ip_forward
