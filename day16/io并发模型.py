"""
IO并发模型    tcp   一般和非阻塞一起用  一般都用读操作，写操作几乎不用
"""
from socket import *
from select import *
#设置监听套接字
tcp_sock=socket()
tcp_sock.bind(("0.0.0.0",1125))
tcp_sock.listen(5)
tcp_sock.setblocking(False)  #设置成非阻塞
#
rlist=[tcp_sock]
wlist=[]
xlist=[]
#循环的监控IO事件
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    #遍历就绪的IO 对象
    for r in rs:
        if r is tcp_sock:
            connfd,addr=tcp_sock.accept()
            print("connect from",addr)
            connfd.setblocking(False)  #设置非阻塞
            rlist.append(connfd)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)
    for w in wlist:
        w.send("ok".encode())
        wlist.remove(w)


