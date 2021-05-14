import socket
class MyClient:
    def __init__(self):
       self.clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       self.clientSocket.connect(("localhost",5500))
    def recieve(self,size):
        buffer=b''
        while len(buffer)<size:
            buffer+=self.clientSocket.recv(size-len(buffer))
        return buffer
    def recieveAndDecode(self,size):
        buffer=b''
        while len(buffer)<size:
            buffer+=self.clientSocket.recv(size-len(buffer))
        return buffer.decode("utf-8").strip()
    def sendString(self,string):
        self.clientSocket.sendall(bytes(string,"utf-8"))
    def sendBytes(self,dataBytes):
        self.clientSocket.sendall(bytes)
    def close(self):
        self.clientSocket.close()