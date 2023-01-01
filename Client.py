import socket

def Client():
    host='localhost'
    port=6000
    socket_client=socket.socket()
    socket_client.connect((host,port))

    message=input(" -> ")

    while message != 'bye':
        socket_client.send(message.encode())
        data=socket_client.recv(1024).decode()
        print(data)
        message=input(" -> ")
    socket_client.close()

Client()

