import ipaddress
import sys

def main():
    for arg in sys.argv[1:]:
        addr = ipaddress.ip_interface(arg)
        print("IP Address: ", addr)
        print("Network: ", addr.network)
        print("Network Mask: ",addr.netmask)
        print("Broadcast Address: ",addr.broadcast_address)
