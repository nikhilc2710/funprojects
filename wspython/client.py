import socket
import threading

#asking user for name
username=input("Enter Your Name")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5555))

def receive():
    while True:
        try:
            #Recive message form server
            #send username to server
            message=client.recv(1024).decode('ascii')
            if message=="Your Name":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            #close connection in case Error
            print("Error Occured")
            client.close()
            break


#send message to server
def write():
    while True:
        message=f'{username}: {input("")}'
        client.send(message.encode('ascii'))

#start Threads for recive and write

reciverThread=threading.Thread(target=receive)
reciverThread.start()

writeThread=threading.Thread(target=write)
writeThread.start()
