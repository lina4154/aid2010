
from socket import *
from select import *

udp_sock=socket(AF_INET,SOCK_DGRAM)

tcp_sock=socket()
tcp_sock.bind(("0.0.0.0",1125))
tcp_sock.listen(5)
tcp_sock.setblocking(False)
ep = epoll()
ep.register(tcp_sock, EPOLLIN)
map = {tcp_sock.fileno(): tcp_sock}
while True:
    events = ep.poll() #events[(fuio,event)]
    for f,v in events:
        if map[f]==tcp_sock:
            connfd, addr = tcp_sock.accept()
            print("connect from",addr)
            connfd.setblocking(False)
            ep.register(connfd,EPOLLIN)
            map[connfd.fileno()]=connfd
        elif v==EPOLLIN:
            data=map[f].recv(1024)
            if not data:
                ep.unregister(f)
                map[f].close()
                del map[f]
                continue
            print(data.decode())
            ep.unregister(f)
            ep.register(f,EPOLLOUT)
        elif v==EPOLLOUT:
            map[f].send("ok".encode())
            ep.unregister(f)
            ep.register(f, EPOLLIN)











