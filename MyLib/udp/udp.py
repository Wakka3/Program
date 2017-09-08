from socket import (socket, AF_INET, SOCK_DGRAM, SOL_SOCKET,SO_REUSEADDR, IPPROTO_IP, IP_ADD_MEMBERSHIP, inet_aton)
from contextlib import closing

def get_ip():
    with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
    return ip

class MultiUDP:
    def __init__(self, groupaddr, groupport, bufsize=4096):
        self.groupaddr = groupaddr
        self.groupport = groupport
        self.bufsize = 4096
        self.ip = get_ip()

    def multirecv(self, repeat=False):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            sock.bind(('0.0.0.0', port))
            sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, inet_aton(groupaddr) + inet_aton(get_ip()))

            while repeat is False:
                data = sock.recv(self.bufsize).decode('utf8')
                print(data)
        return data

    def multisend(self, msg):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.setsockopt(IPPROTO_IP, IP_MULTICAST_IF, inet_aton(get_ip()))
            sock.sendto(msg.encode('utf8'), (groupaddr, port))
        return

class UniUDP:
    def __init__(self):
        self.addr = groupaddr
        self.port = groupport
        self.bufsize = 4096
        self.ip = get_ip()

    def send(self):
        pass

    def recv(self):
        pass

