"""
IO多路复用演示
"""
from socket import *
from select import *
file=open("1.txt",)
udp_sock=socket(AF_INET,SOCK_DGRAM)
tcp_sock=socket()
tcp_sock.bind(("0.0.0.0",1125))
tcp_sock.listen(5)
print("监听开始")
rs,ws,xs=select([tcp_sock],[udp_sock],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)
