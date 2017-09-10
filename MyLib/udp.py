from socket import (socket, AF_INET, SOCK_DGRAM, SOL_SOCKET,SO_REUSEADDR, IPPROTO_IP, IP_ADD_MEMBERSHIP, IP_MULTICAST_IF, inet_aton)
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

    def recv(self, repeat=False):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            sock.bind(('0.0.0.0', self.groupport))
            sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, inet_aton(self.groupaddr) + inet_aton(self.ip))

            while True:
                data = sock.recv(self.bufsize).decode('utf8')
                self.on_data(data)
                if repeat is False:
                    break

    def send(self, msg):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.setsockopt(IPPROTO_IP, IP_MULTICAST_IF, inet_aton(get_ip()))
            sock.sendto(msg.encode('utf8'), (self.groupaddr, self.groupport))
        return

    def on_data(self, data):
        print(data)


class UniUDP:
    def __init__(self, addr, port, bufsize=4096):
        self.addr = addr
        self.port = port
        self.bufsize = bufsize
        self.ip = get_ip()

    def send(self, addr=self.addr, port=self.port):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.sendto(msg.encode('utf8'), (addr, port))
        return

    def recv(self, addr=self.addr, port=self.port, repeat=False):
        with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
            sock.bind((addr, port))
            while True:
                data = sock.recv(bufsize).decode('utf8')
                self.on_data(data)
                if repeat is False:
                    break

    def on_data(self, data):
        print(data)



