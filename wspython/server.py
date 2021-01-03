import socket
import threading

#define server host and port
host,port ='127.0.0.1',5555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

#List for client-ids and their nickname
clients,nickname=[],[]

#send message to all connected clients
def brodcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

#handling incomming message from clients
def handle(client):
    while True:
        try:
            #broadcast message
            message=client.recv(1024).decode('ascii')
            brodcast(message)
        except:
            #Remove and close clients
            index=client.index(client)
            clients.remove(index)
            client.close()
            userLeft=nickname[index]
            brodcast(f'{userLeft} left the chat!')
            nickname.remove(userLeft)
            break

#Reciving Function

def receive():
    while True:
        #Accept Connection
        client,address=server.accept()
        print(f'User connected from {address}')

        #Get and store the name of user
        client.send('Your Name'.encode('ascii'))
        username=client.recv(1024).decode('ascii')
        nickname.append(username)
        clients.append(client)

        #print and brodcast username to all users
        print(f'user  {username}')
        brodcast(f"user joined {username}")
        client.send('Connected to server'.encode('ascii'))

        #start handling thread For Client
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()
    
receive()



    
