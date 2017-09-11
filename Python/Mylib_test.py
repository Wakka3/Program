import sys; sys.path.append("C:\GitHub\Program\MyLib")
import udp


groupaddr = "239.255.255.1"
groupport = 55555
multi = udp.MultiUDP(groupaddr, groupport)

multi.recv()


