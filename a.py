from socket import *
from threading import Thread

class Handle:
    def handle(self,connfd):
        while True:
            data=connfd.recv(1024)
            if not data:
                connfd.close()
                break
            print(data.decode())
            connfd.send("一定要幸福一辈子".encode())
class ServerThread:
    def __init__(self,host="",port=0,):
        self.host=host
        self.port=port
        self.adress=(host,port)
        self.sock=self.creatsochet()
        self.a=Handle()
    def creatsochet(self):
        tcp_socket=socket()
        tcp_socket.bind(self.adress)
        return tcp_socket
    def connect(self):
        self.sock.listen(5)
        while True:
            connfd,addr=self.sock.accept()
            t=Thread(target=self.a.handle,args=(connfd,),daemon=True)
            t.start()

if __name__ == '__main__':
    thread=ServerThread(host="0.0.0.0",port=8888)
    thread.connect()






































