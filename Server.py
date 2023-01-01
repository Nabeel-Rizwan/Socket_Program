import socket

def Server():
    host='localhost'
    port=6000
    socket_server=socket.socket()
    socket_server.bind((host,port))
    socket_server.listen(2)
    conn,add=socket_server.accept()

    print("ADDRESS -> "+ str(add))

    while True:
        data=conn.recv(1024).decode()
        print(data)
        data=input(" -> ")
        conn.send(data.encode())
    conn.close()

Server()
