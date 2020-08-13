import sys
(str_ipaddr, str_cidr) = sys.argv[1].split("/")
octet = str_ipaddr.split(".") #No way to avoid having to split string?
cidr = int(str_cidr)          #Convert the cidr to INT
netmask = [0,0,0,0]
for net in range(cidr):
    netmask[(net//8)] = netmask[(net//8)] + (1 << (7 - net % 8)) # switch octets every 8 loops, calculates network mask
network = []
for netID in range(4):
    network.append(int(octet[netID]) & netmask[netID])
broadcast = list(network)
broadcast_range = 32-cidr
for bcast in range(broadcast_range):
    broadcast[3-(bcast//8)] = broadcast[3 - (bcast//8)] + (1 << (bcast%8)) # // performs integer division, takes floor
print("\nNetwork Information : " + str_ipaddr + "/" + str_cidr)
print("-------------------")
print("Netmask: %s" % ".".join(map(str,netmask)))
print("Network: %s" % ".".join(map(str,network)))
print("Broadcast: %s" % ".".join(map(str,broadcast)))
