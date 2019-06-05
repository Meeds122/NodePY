# Standard Library imports
import time
import sys

# Testing imports
sys.path.insert(0, './calls') # Include py files in calls/ 
import serverTime

# Globals
API_CALLS = {} # a dictionary that contains a map of api calls to api functions.

# Testing
API_CALLS['serverTime'] = serverTime.main

"""
call(request):
    Takes request, calls apropriate function, returns data from function. 
"""
def call(request):
    global API_CALLS # dictionary of known API calls

    # Sanity checks
    if len(request) <= 1:
        return "BAD REQUEST"

    # Format request into [Request without preceding slash, arg1, argc]
    if request.find('&') != -1:
        api_call = request.split("&")
    else:
        api_call = [request,]
    api_call[0] = api_call[0][1:]

    # Check if call function is already in dictionary of calls. 
    try:
        f = API_CALLS[api_call[0]]
    except KeyError:
        # Do see if API py file exists. If exists, add, otherwise return BAD REQUEST
        pass
    
    return str(f(api_call[1:]))


"""
buildResponse(data):
    Takes data and appends it to a basic HTTP response.
    Returns generated response
"""
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
    # The following was disabled to allow for continued development. There is a bug, somewhere... Issue #1
    #data_len = len(basic_response) - 7 # 7 is the length of the CON_LEN identifier that will be replaced 
    #data_len = data_len + len(str(data_len))
    #basic_response = basic_response.replace("CON_LEN", str(data_len))
    return basic_response
