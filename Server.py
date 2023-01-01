import socket                                     # import socket python library

def Server():                                     # Server function
    host='localhost'                              # host is localhost
    port=6000                                     # port will be 6000, can be changed
    socket_server=socket.socket()
    socket_server.bind((host,port))               # Bind host and port
    socket_server.listen(2)                       # listen to 2 connections maximum
    conn,add=socket_server.accept()               # accept connection

    print("ADDRESS -> "+ str(add))                # print address at which connection is established

    while True:
        data=conn.recv(1024).decode()             # receive data and decode from client
        print(data)                               # print the data received from client
        data=input(" -> ")                        # take the input from server
        conn.send(data.encode())                  # encode and send data to client from server
    conn.close()

Server()                                          # Call Server function
