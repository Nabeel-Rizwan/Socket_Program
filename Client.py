import socket                                           # import Socket python library

def Client():                                           # Client function
    host='localhost'                                    # host is localhost
    port=6000
    socket_client=socket.socket()   
    socket_client.connect((host,port))                  # Connect to Server

    message=input(" -> ")                               # Take input from client

    while message != 'bye':                             # While the message from client is not bye, Repeat the loop
        socket_client.send(message.encode())            # Encode and send the message from client to server
        data=socket_client.recv(1024).decode()          # Receive the message from Client side and decode
        print(data)                                     # print the message from Server
        message=input(" -> ")                           # Take input message from client then repeat loop to send message
    socket_client.close()                               # if message is bye then close client socket

Client()                                                # Call Client function

