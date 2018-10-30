import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("107.170.192.50", 2506))

print(sock.recv(1024).decode("UTF-8"))
sock.send(bytearray(" ", "UTF-8"))

data = ""
while True:
    data = sock.recv(1024);
    print(str(data))
    
    if (len(data) < 1):
        break
    else:
        sock.send(data)
