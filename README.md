# pyAPI
Basic web framework for non web programmers

*Currently in Alpha*

How to test:
1. Modify server/config.txt and client/request.js to reflect the server and port you will be using for the API backend. 
2. Run run.sh
3. Browse to the host hosting the client/ folder
4. Press the test button. It should read with the current server time. 
5. Read more about developing applications for this framework in help.txt

How to install:
1. Modify server/config.txt and client/request.js to reflect your enviroment's ip and port.
2. Expose the client/ folder to the internet using a standard web server. Apache HTTPd, nginx, and Lighttpd come to mind. In a pinch, sometimes I'll even do python -m "SimpleHTTPServer" in the client/ directory for testing purposes.
3. Double check that you cannot access any of the server/ files from the webserver you spun up in step 2.
4. Modify run.sh and change `python3 main.py` to `python3 main.py >> log.txt` to append the server logging to a file rather than the console. 
5. Create a cron job, init entry, or otherwise a scheduled task to start the run.sh script when the server starts. This ensures that the API backend comes back up in a reboot. 


What it does:
1. Provides an API server that translates HTTP requests responses to and from python scripts
2. Provides a Javascript function to make requests to the API server

In essence, this framework provides the glue between python scripts running on a server and client web browsers.

What it does not do:
1. Assist in developing front end HTML, CSS, or Javascript
2. Assist in developing back end Python.

Road Map:
1. Configuration files
2. TLS/HTTPS support
3. Threading and multi-processing
