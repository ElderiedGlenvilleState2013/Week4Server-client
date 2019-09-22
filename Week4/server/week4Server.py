import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9600))

s.listen()
print("server is listening")

#msg = s.recv(4024)

#print(socket.gethostname())



while True:
    clientsocket, address = s.accept()
    

    with clientsocket:
        print(f"got connection {address}")

        while True:
            d = clientsocket.recv(1024)
            if not d:
                break 
            elif d == b"Hello":
                clientsocket.sendall(b"Hi")
            else:
                clientsocket.sendall(b"Goodbye")


#closing connection

s.close()





    

   


