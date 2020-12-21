from multiprocessing import  Process
from socket import *
from time import ctime,sleep
file=open("1.txt","a+")
ADDR=("127.0.0.1",8888)
tcp_socket=socket()
tcp_socket.connect(ADDR)
while True:
    a=input(">>")
    if not a:
        break
    tcp_socket.send(a.encode())
    data=tcp_socket.recv(1024)
    print(data.decode())
tcp_socket.close()