import sys
(str_ipaddr,str_cidr) = sys.argv[1].split("/")
octet = str_ipaddr.split(".")
cidr = int(str_cidr)
netmask = [0,0,0,0]
for net in range(cidr):
    netmask[(net//8)] = netmask[(net//8) + (1 << (7 - net % 8))
network = []
for netID in range(4):
    network.append(int(octet[netID]) & netmask[netID])
broadcast = list(network)
broadcast_range = 32-cidr
for bcast in range(broadcast_range):
    broadcast[3-(bcast//8)] = broadcast[3-(bcast//8)] + (1 << (bcast%8))
print("Network Information : " + str_ipaddr + "/" + str_cidr)
print("Netmask: %s % ".".join(map(str,netmask)))
print("Network: %s % ".".join(map(str,network)))
print("Broadcast: %s % ".".join(map(str,broadcast)))
