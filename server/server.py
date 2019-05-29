# Standard Library imports
import socket
import time

# Custom Library imports
import api

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
                    data = conn.recv(1024)
                    if not data:
                        ret_data = "ERROR EMPTY REQUEST"
                    else:
                        ret_data = "Test Back"
                    conn.sendall(api.buildResponse(ret_data).encode())
