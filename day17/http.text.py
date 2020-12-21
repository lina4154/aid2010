"""
获取http 请求和相应
"""
from socket import *

def handle(connfd):
    data = connfd.recv(1024 * 10)
    print(data.decode())
    # 换行\r\n
    file=open("kb.jpg","rb")
    response="HTTP/1.1 200 OK\r\n"
    response+="Content-Type: image/jpg\r\n"
    response+="\r\n"
    response=response.encode()+file.read()
    connfd.setblocking(response)
    # file = open("kb.jpg", "rb")
    # response = "HTTP/1.1 200 OK\r\n"
    # response += "Content-Type: image/jpg\r\n"
    # response += "\r\n"
    # response = response.encode() + file.read()
    # connfd.send(response)
def main():
    s=socket()
    s.bind(("0.0.0.0",8800))
    s.listen(5)

    connfd,addr=s.accept()
    print("connect from",addr)
    handle(connfd)
    connfd.close()
    s.close()
if __name__ == '__main__':
    main()

#换行\r\n

###网页上输入127.0.0.0:8888