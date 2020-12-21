
from socket import *
from select import *
file=open("1.txt",)
udp_sock=socket(AF_INET,SOCK_DGRAM)

tcp_sock=socket()
tcp_sock.bind(("0.0.0.0",1125))
tcp_sock.listen(5)
tcp_sock.setblocking(False)
p = poll()
p.register(tcp_sock, POLLIN)
map = {tcp_sock.fileno(): tcp_sock}
while True:
    events = p.poll() #events[(fuio,event)]
    for f,v in events:
        if map[f]==tcp_sock:
            connfd, addr = tcp_sock.accept()
            print("connect from",addr)
            connfd.setblocking(False)
            p.register(connfd,POLLIN)
            map[connfd.fileno()]=connfd
        else:
            data=map[f].recv(1024)
            if not data:
                p.unregister(f)
                map[f].close()
                del map[f]
                continue
            print(data.decode())
            map[f].send("ok".encode())





