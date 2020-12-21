from select import *
from socket import *
import re
class Handle:
    def __init__(self,connfd,html=""):
        self.connfd=connfd
        self.html=html
    def chuli(self,info):
        if info=="/":
            filename=self.html+"/index.html"
        else:
            filename=self.html+info
        try:
            file=open(filename,"rb")
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"  # 空行
            with open(self.html + "/404.html") as f:
                response += f.read()
            response = response.encode()
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"  # 空行
            response = response.encode() + file.read()
        finally:
            self.connfd.send(response)
    def requset(self):
        data=self.connfd.recv(1024*10).decode()
        pattern=r"[A-Z]+\s+(?P<info>/\S*)"
        result=re.match(pattern,data)
        if result:
            info=result.group("info")
            print("请求内容",info)
            self.chuli(info)

class Webserver:
    def __init__(self,host="0.0.0.0",port=0,html=""):
        self.host=host
        self.port=port
        self.html=html
        self.address=(self.host,self.port)
        self.sock=self.createsock()
        self.rlist=[]
        self.wlist=[]
        self.xlist=[]
    def createsock(self):
        sock=socket()
        sock.bind(self.address)
        sock.setblocking(False)
        return sock
    def connect(self):
        connfd,addr=self.sock.accept()
        print("connect from ",addr)
        connfd.setblocking(False)
        self.rlist.append(connfd)
    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock)
        while True:
            rs,ws,xs=select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    self.handle=Handle(r,self.html)
                    self.handle.requset()
                    self.rlist.remove(r)
                    r.close()




if __name__ == '__main__':
    server=Webserver(host="0.0.0.0",port=8855,html="./static")
    server.start()