import socket
import random
from threading import Thread

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

NUM_OF_PROBLEMS_TO_GET_RIGHT = 200

# main
def evaluateClient(sock, addr):
    print("Client {0} trying to connect".format(addr))
    sock.settimeout(5000)
    bufferSize = 2048
    
    returnData = "Welcome To IHackUCTF"
    returnData += "\r\nIn the following responses, you will get a random addition problem."
    returnData += "\r\nYou will have to respond with the correct answer to the problem.";
    returnData += "\r\nPress enter to begin."
    returnData += "\r\n\r\n"
    sock.send(bytearray(returnData, "UTF-8"))
    
    lastAnswerWrong = False;
    expectedAnswer = 0;
    correctAnswersCount = 0
    for i in range(200000):
        try:
            if (lastAnswerWrong):
                sock.send(bytearray("That's Wrong!\r\nThe Correct Answer Was: " +
                                        str(expectedAnswer) + "\r\n", "UTF-8"))
                break;
            
            chunks = ""
            while True:
                chunk = sock.recv(bufferSize)
                chunks += chunk.decode("utf-8")
                if (len(chunk) < bufferSize): break;
            
            if (i != 0):
                try:
                    if (int(chunks) != expectedAnswer):
                        lastAnswerWrong = True
                    else:
                        correctAnswersCount += 1
                        
                except ValueError:
                    lastAnswerWrong = True
            
            if (not lastAnswerWrong):
                if (correctAnswersCount >= NUM_OF_PROBLEMS_TO_GET_RIGHT):
                    break
                    
                left = random.randint(990, 99999999)
                right = random.randint(990, 99999999)
                expectedAnswer = left + right
                sock.send(bytearray(str(left) + " + " + str(right) + " = ", "UTF-8"))
            
        except socket.timeout as e1:
            break
    
    if (correctAnswersCount >= NUM_OF_PROBLEMS_TO_GET_RIGHT):
        sock.send(bytearray("You Win! FLAG_{GRAY_BUBBLE_BUS_HATS}\r\n", "UTF-8"))
        print("Client {0} got the key!".format(addr))
                            
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Closed");

serverA = MyServer(evaluateClient)
port = 7999
print("My Port Is: " + str(port))
serverA.listen("0.0.0.0", port)
