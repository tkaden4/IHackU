from package import hex
import time
#import os
#import sys
import socket
from threading import Thread

class Hex_Server:
    serverSocket = None
    hex_program = None
    stopSock = False

    def __init__(self, hex_program):
        self.hex_program = hex_program
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def listen(self, host, port):
        self.serverSocket.bind((host, port))
        self.serverSocket.settimeout(1)
        self.serverSocket.listen(5)
        stopSock = False
        try:
            while not stopSock:
                try:
                    (clientSocket, address) = self.serverSocket.accept()
                    t = Thread(target=self.hex_program, args=(clientSocket, address))
                    t.start()
                    
                except socket.timeout as e1:
                    pass
            
        except KeyboardInterrupt as e2:
            stopSock = True
            
        self.serverSocket.close()

def evaluateClient(cSocket, address):
    print("Client {0} trying to connect".format(address))
    bufferSize = 2048
    
    returnData = "Welcome to GrayCTF."
    returnData += "\r\nThe theme is hexadecimal."
    returnData += "\r\nYou will be solving a series of problems to get the cookie! (flag)"
    returnData += "\r\n\r\n"
    cSocket.send(bytearray(returnData, "UTF-8"))

    hexClass = hex.Hex_Challenge()
    #hexClass.print_hextable()
    error_code = hexClass.print_rows(cSocket, bufferSize)
    if error_code == -1:
        cSocket.close()
        print("User closed the connection.")
    elif error_code == 1:
        cSocket.shutdown(socket.SHUT_RDWR)
        cSocket.close()

grayServer = Hex_Server(evaluateClient)
port = 2210
print("My port is: " + str(port))
grayServer.listen("169.254.155.222", port); #"107.170.192.50", port)
