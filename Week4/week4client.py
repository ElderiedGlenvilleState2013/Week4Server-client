import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('127.0.0.1', 9600))




send_msg = input(" say anything: ")


c.sendall(send_msg.encode())
msg = c.recv(1024)
print('received from server: ', repr(msg))









#print(msg.decode("utf-8"))
c.close()


