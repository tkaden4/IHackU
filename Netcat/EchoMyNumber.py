import os
import sys
import socket
import random
from threading import Thread

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    return True
    
class MyServer:
    sock = None
    clientHandler = None
    stopSock = False
    def __init__(self, clientHandler):
        self.clientHandler = clientHandler
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def listen(self, host: str, port: int):
        self.sock.bind((host, port))
        self.sock.settimeout(1)
        self.sock.listen(5)
        stopSock = False
        try:
            while not stopSock:
                try:
                    (clientsocket, address) = self.sock.accept()
                    t = Thread(target=self.clientHandler, args=(clientsocket, address))
                    t.start()
                except socket.timeout as e1:
                    pass
         
        except KeyboardInterrupt as e1:
            stopSock = True
            
        self.sock.close()

NUM_OF_PROBLEMS_TO_GET_RIGHT = 100

# main
def evaluateClient(sock, addr):
    print("Client {0} trying to connect".format(addr))
    #sock.settimeout(5)
    BUFFER_SIZE = 2048
    MAX_INPUT_SIZE = 40;
    
    returnData = "*******  Echo My Number *******"
    returnData += "\r\nI will give you a number, and you will send the number back to me."
    returnData += "\r\nPress enter to continue.\r\n\r\n"
    sock.send(bytearray(returnData, "UTF-8"))
    
    lastAnswerWrong = False;
    correctAnswersCount = 0
    for i in range(200000):
        try:
            if (lastAnswerWrong):
                sock.send(bytearray("That's Not The Number I Gave You." +
                                    "\r\nThe number was: " +
                                    str(echoNumber) + "\r\n", "UTF-8"))
                break;
            
            chunks = ""
            while True:
                chunk = sock.recv(BUFFER_SIZE)
                chunks += chunk.decode("utf-8")
                if (len(chunk) < BUFFER_SIZE or len(chunks) > MAX_INPUT_SIZE): break;
            
            if (len(chunks) > MAX_INPUT_SIZE):
                sock.send(bytearray("Too much data sent.", "UTF-8"))
                break;
                
            if (i != 0):
                try:
                    if (not is_int(chunks) or int(chunks) != echoNumber):
                        lastAnswerWrong = True
                    else:
                        correctAnswersCount += 1
                        
                except ValueError:
                    lastAnswerWrong = True
            
            if (not lastAnswerWrong):
                if (correctAnswersCount >= NUM_OF_PROBLEMS_TO_GET_RIGHT):
                    break
                    
                echoNumber = random.randint(0, 9)
                sock.send(bytearray(str(echoNumber) + "\r\n", "UTF-8"))
            
        except socket.timeout as e1:
            pass
    
    if (correctAnswersCount >= NUM_OF_PROBLEMS_TO_GET_RIGHT):
        sock.send(bytearray("You Win! FLAG_{GRAY_PASSWORD_123_HATS}\r\n", "UTF-8"))
    
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Closed");

serverA = MyServer(evaluateClient)
port = 2506
print("My Port Is: " + str(port))
# serverA.listen("192.168.240.35", port)
serverA.listen("169.254.155.222", port)
