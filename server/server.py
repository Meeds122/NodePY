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
                    conn.sendall(self.buildResponse(ret_data).encode())
    def buildResponse(self, data):
        basic_response = """
HTTP/1.1 200 OK
Date: TIME
Server: NodePY
Access-Control-Allow-Origin: *
Last-Modified: TIME
Content-Length: CON_LEN
Content-Type: text/html
Connection: Closed

DATA
        """
        current_time = str(time.strftime("%a, %d %b %Y %H:%M:%S PST"))
        basic_response.replace("TIME", current_time)
        basic_response.replace("DATA", str(data))
        data_len = len(basic_response) - 7 # 7 is the length of the CON_LEN identifier that will be replaced
        data_len = data_len + len(str(data_len))
        basic_response.replace("CON_LEN", str(data_len))
        return basic_response
