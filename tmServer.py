import pathlib
import MySocket
import time
from uuid import uuid1
from threading import Thread,Semaphore
class Model:
    def __init__(self,path):
        self.manager=dict()
        self.users=dict()
        self.loggedInUsers=dict()
        self.populateDatastructure(path)
    def populateDatastructure(self,path):
        for file in path.iterdir():
            semaphore=Semaphore(5)
            self.manager[file.name]=(file.name,file.stat().st_size,semaphore)
        with open("users.cfg","r")as usersFile:
            while True:
                user=usersFile.readline()
                if len(user)==0: break
                userName,password=eval(user)
                self.users[userName]=eval(user)
    def getFileByName(self,fileName):
        file=self.manager[fileName]        
        return file
    def checkUserByName(self,userName):
        userName=userName
        if userName in self.users:return True
        return False
    def checkUserPassword(self,userName,password):
        dsUser=self.users[userName]
        dsPassword=dsUser[1]
        if dsPassword==password: return True
        return False
    def removeUserId(self,userId):
        self.loggedInUsers.pop(userId)
    def generateUserId(self,user):
        id=str(uuid1())
        self.loggedInUsers[id]=user
        return id
    def isIdRegistered(self,userId):
        if userId in self.loggedInUsers:return True
        return False  
    def isFileExist(self,fileName):
        return fileName in self.manager
    def getFilesList(self):
        list=[]
        for file in self.manager:
            list.append(self.manager[file])
        return list


class RequestModifier:
    def __init__(self,function):
        self.function=function  
    def isUserRegistered(socket,model):
        userLength=int(socket.recieveAndDecode(1024))
        user=eval(socket.recieveAndDecode(userLength))
        userName,password=user
        if not(model.checkUserByName(userName)):
                response=("Incorrect Username",)
                responseLength=len(str(response))
                socket.sendString(str(responseLength).ljust(1024))
                socket.sendString(str(response))
        elif not(model.checkUserPassword(userName,password)):
                response=("Incorrect Password",)
                responseLength=len(str(response))
                socket.sendString(str(responseLength).ljust(1024))
                socket.sendString(str(response))
        else:
            id=model.generateUserId(user)
            response=("Correct",id)
            responseLength=len(str(response))
            socket.sendString(str(responseLength).ljust(1024))
            socket.sendString(str(response))
    def __call__(self,socket,model):
            RequestModifier.isUserRegistered(socket,model);
            self.function(socket,model)


class MyThread(Thread):
    def __init__(self,socket,model):
        self.model=model
        self.socket=socket
        Thread.__init__(self)
        self.start()
    def run(self):
        acceptRquests(self.socket,self.model)


def download(socket,dsFile,semaphore):
    fileName,fileSize=dsFile
    socket.sendString(str(fileSize).ljust(1024))
    for entry in path.glob(fileName):
        ff=entry
    with open(ff,"rb")as file:
        bytesSent=0
        while True:
            if fileSize-bytesSent<=4096:
                socket.sendBytes(file.read(fileSize-bytesSent))
                break;
            bytesSent+=4096
            socket.clientSocket.sendall(file.read(4096))
    semaphore.release()
   



def verifyUserId(function):
    def checkId(socket,model):
        lengthOfId=int(socket.recieveAndDecode(1024))
        userId=socket.recieveAndDecode(lengthOfId)
        if model.isIdRegistered(userId)==True:
            response="Id verified"
            responseLength=len(response)
            socket.sendString(str(responseLength).ljust(1024))
            socket.sendString(response)
            function(socket,model)
        else:
            response="exit"
            responseLength=len(response)
            socket.sendString(str(responseLength).ljust(1024))
            socket.sendString(response)
    return checkId

@verifyUserId
def displayFiles(socket,model):
    files=model.getFilesList()
    for file in files:
        fileNameAndSize=(file[0],file[1])
        socket.sendString(str(len(str(fileNameAndSize))).ljust(1024))
        socket.sendString(str(fileNameAndSize))
    socket.sendString("4".ljust(1024))
    socket.sendString("Over")
@verifyUserId
def isFileExist(socket,model):
    fileNameLength=int(socket.recieveAndDecode(1024))
    fileName=socket.recieveAndDecode(fileNameLength)
    responseLength=len(str(model.isFileExist(fileName)))
    socket.sendString(str(responseLength).ljust(1024))
    socket.sendString(str(model.isFileExist(fileName)))
    if model.isFileExist(fileName)==True: 
        file=model.getFileByName(fileName)
        semaphore=file[2]
        fileNameAndSize=(file[0],file[1])
        semaphore.acquire()
        download(socket,fileNameAndSize,semaphore)


def logoutUser(socket,model):
    lengthOfId=int(socket.recieveAndDecode(1024))
    userId=socket.recieveAndDecode(lengthOfId)
    model.removeUserId(userId)


@RequestModifier
def acceptRquests(socket,model):
    while True:
        requestLength=int(socket.recieveAndDecode(1024))
        request=socket.recieveAndDecode(requestLength)
        if request=="dir":displayFiles(socket,model)
        if request=="Download File": isFileExist(socket,model)
        if request=="quit": 
            logoutUser(socket,model)
            socket.close()
            break 
        if request=="exit": break
    socket.close()


        
path=pathlib.Path(str(pathlib.Path.cwd())+"//store")
model=Model(path)   
while True:  
    socket=MySocket.MySocket()
    t=MyThread(socket,model)
    
    
    

