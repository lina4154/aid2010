from multiprocessing import  Process
from socket import *
from time import ctime,sleep
file=open("1.txt","a+")
ADDR=("0.0.0.0",1125)
tcp_socket=socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)
# tcp_socket.setblocking(False)
tcp_socket.settimeout(5)
while True:
    print("等待连接")
    try:
        connfd,addr=tcp_socket.accept()
        print("connfd from:",addr)
    except BlockingIOError as e:
        sleep(2)
        msg="%s %s\n"%(ctime(),e)
        file.write(msg)
    except timeout as e:
        msg = "%s %s\n" % (ctime(), e)
        file.write(msg)
    else:
        data = connfd.recv(1024)
        print(data.decode())


