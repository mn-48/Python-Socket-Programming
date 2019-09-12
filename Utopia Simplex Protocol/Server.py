import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    #abc = input()
    #clientsocket.send(bytes(abc,"utf-8"))
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()