from MyClient import MyClient
import time
import pathlib
def isFileExist(fileName):
    client.sendString(str(len(fileName)).ljust(1024))
    client.sendString(fileName)
    responseLength=int(client.recieveAndDecode(1024))
    response=client.recieveAndDecode(responseLength)
    return eval(response)
def download(saveFileName):
    print("Waiting for download to start.....")
    fileSize=int(client.recieveAndDecode(1024))
    print("Download starts")
    with open(saveFileName,"wb")as file:
        bytesSent=0
        while True:
            if fileSize-bytesSent<=4096:
                file.write(client.recieve(fileSize-bytesSent))
                break
            bytesSent+=4096
            file.write(client.recieve(4096))
    
    print("Downloaded")
def showFiles():
            while True:
                responseLength=int(client.recieve(1024))
                response=client.recieveAndDecode(responseLength)
                if response=="Over":
                    break
                else :
                    file=eval(response)
                    fileName=file[0]
                    fileSize=file[1]
                    print(f"{fileName},size: {fileSize}")
def saveFile(fileName):
            if isFileExist(fileName):
                saveFileName=input("tmclient-> SaveAs?")
                download(saveFileName)
            else : print(f"Invalid file name {fileName}")
client=MyClient()
userName=input("Username: ")
password=input("Password: ")
request=str((userName,password))
requestLength=len(request)
client.sendString(str(requestLength).ljust(1024))
client.sendString(request)
responseLength=int(client.recieveAndDecode(1024))
response=eval(client.recieveAndDecode(responseLength))
if response[0]=="Correct": 
    id=response[1]   
    while True:
        command=str(input("tmclient->"))  
        if command=="quit":
            client.sendString(str(len(command)).ljust(1024)) 
            client.sendString(command)
            lengthOfId=len(str(id))
            print(id,str(id))
            client.sendString(str(lengthOfId).ljust(1024))
            client.sendString(str(id))
            break  
        if command=="dir":
            client.sendString(str(3).ljust(1024)) 
            client.sendString(command)
            lengthOfId=len(str(id))
            client.sendString(str(lengthOfId).ljust(1024))
            client.sendString(str(id))
            responseLength=int(client.recieveAndDecode(1024))
            response=client.recieveAndDecode(responseLength)
            if response=="exit": 
                client.sendString(str(4).ljust(1024)) 
                client.sendString(response)
                break
            showFiles()
        if command[0:4]=="get ":
            fileName=command[4:]
            request="Download File"
            client.sendString(str(len(request)).ljust(1024))
            client.sendString(request)
            lengthOfId=len(id)
            client.sendString(str(lengthOfId).ljust(1024))
            client.sendString(id)
            responseLength=int(client.recieveAndDecode(1024))
            response=client.recieveAndDecode(responseLength)
            if response=="exit": break
            saveFile(fileName)
else : print(response[0])
client.close()
            
            