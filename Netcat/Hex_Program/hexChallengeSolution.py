import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("107.170.192.50", 2210))
sock.settimeout(1)

for i in range(100):
    raw = ""
    
    try:
        iLoopMax = 20
        while iLoopMax > 0:
            sleep(0.3)
            raw += sock.recv(1024).decode("UTF-8")
            iLoopMax -= 1
            if (raw.find("Answer") != -1): break
    except Exception as e:
        pass

    if (iLoopMax <= 0 or len(raw.split("\r\n")) < 3):
        print("Done?")
        break
    
    values = [x.split(' ')[-1] for x in raw.split('\r\n')[-3:-1]]

    solution = 0
    if raw.find("Please add") != -1:
        solution = hex(int(values[0], 16) + int(values[1], 16))[2:]
    else:
        solution = hex(int(values[0], 16) - int(values[1], 16))[2:]

    solution = solution[0:len(solution)].upper()
    sock.send(bytearray(solution + "\n", "UTF-8"))
    print(solution)

print(raw)
