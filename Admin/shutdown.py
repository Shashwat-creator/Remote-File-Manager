import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(("localhost",5500))
request="xipo8770"
socket.sendall(bytes(str(len(request)).ljust(1024),encoding="utf-8"))
socket.sendall(bytes(request,encoding="utf-8"))