# Standard Library imports
import socket
import time
import sys

# Custom Library imports
import api

# Testing imports
sys.path.insert(0, './calls') # Include py files in calls/ 
import serverTime

# Constants
REQUEST_SIZE = 1024 # 1kb maximum request size. 

class Server():
    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)
        self.mainLoop()
    def mainLoop(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(5)
            while True:
                conn, addr = s.accept()
                with conn:
                    print("Connected by", addr)
                    data = conn.recv(REQUEST_SIZE)
                    if not data:
                        ret_data = "ERROR EMPTY REQUEST"
                    else:
                        ret_data = serverTime.main(data)
                    conn.sendall(api.buildResponse(ret_data).encode())
