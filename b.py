from multiprocessing import Process
from socket import *
ADDR=("127.0.0.1",1125)
tcp_sock=socket()
tcp_sock.connect(ADDR)
while True:
    a=input(">>")
    if not a:
        break
    tcp_sock.send(a.encode())
    # data=tcp_sock.recv(1024)
tcp_sock.close()