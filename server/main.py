
import server

"""
getConfig(file_name):
    Reads in file_name, parses for keyword, returns dict of results. 
    Example output: {"ip":"0.0.0.0", "port":"31337"}
"""
def getConfig(config_file_name):
    out_dict = {}
    with open(config_file_name, 'r') as config_file:
        for line in config_file.readlines():
            if str(line)[0]=="#":
                #Ignore Line
                continue
            if "ip" in str(line):
                out_dict[str(line).split("=")[0]] = str(line).split("=")[1].strip() # convert "ip=x.x.x.x" to {..., "ip":"x.x.x.x"}
            elif "port" in str(line):
                out_dict[str(line).split("=")[0]] = str(line).split("=")[1].strip() # convert "port=31337" to {..., "port":"1337"}
            else:
                print("[!] Unable to parse", line, "in configuration file!")
    return out_dict

if __name__ == "__main__":
    # 1. Validate file structure

    # 2. Trigger getConfig() and parse results
    confs = getConfig("config.txt")
    try:
        host = confs["ip"]
    except KeyError:
        print("[!] Bad configuration file -- ip !")
        quit()
    try:
        port = int(confs["port"])
    except KeyError:
        print("[!] Bad configuration file -- port !")
        quit()
    except ValueError:
        print("[!] Bad configuration file -- port is not integer !")
        quit()
    if port < 2 or port > 65535:
        print("[!] Bad configuration file -- port is not within range! 2-65535")

    # 3. Start server main loop
    print("[*] Server starting")
    server.Server(host, port)