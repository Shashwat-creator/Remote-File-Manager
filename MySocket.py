import socket
class MySocket:
    serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(("localhost",5500))
    serverSocket.listen()
    
    def __init__(self):
        print("Server is ready to accept at port 5500")
        self.clientSocket,self.clientSocketName=MySocket.serverSocket.accept()
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
        self.clientSocket.sendall(dataBytes)
    def close(self):
        self.clientSocket.close()