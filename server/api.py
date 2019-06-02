import time

def buildResponse(data):
    basic_response = """
HTTP/1.1 200 OK
Date: TIME
Server: NodePY
Access-Control-Allow-Origin: *
Last-Modified: TIME
Content-Length: CON_LEN
Content-Type: text/html
Connection: Closed

R_DATA

"""
    current_time = str(time.strftime("%a, %d %b %Y %H:%M:%S PST"))
    basic_response = basic_response.replace("TIME", current_time)
    basic_response = basic_response.replace("R_DATA", str(data))
    data_len = len(basic_response) - 7 # 7 is the length of the CON_LEN identifier that will be replaced
    #data_len = data_len + 2 # troubleshooting bug where JS complains about size mismatch. I checked with Wireshark and my initial calculations are correct. 
    data_len = data_len + len(str(data_len))
    basic_response = basic_response.replace("CON_LEN", str(data_len))
    return basic_response
