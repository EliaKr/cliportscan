import time
import socket

socket.setdefaulttimeout(8)
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

openports = []

def checkport(location):
    result = a_socket.connect_ex(location)
    if result == 0:
        return(True)
    else:
        return(False)
    
print("Welcome to cliportscan. Use to scan multiple ports may be blocked by device being scanned.")
print("Enter Target IP Address:")
target = input()

print("Enter Start Port (or leave empty to scan all ports):")
startportinput = input()
if not startportinput:
    startport = 1
    endport = 65535
else:
    print("Enter End Port:")
    startport = int(startportinput)
    endport = int(input())

for i in range(startport, endport + 1):
    print(i)
    loc = (target, i)
    if checkport(loc) == True:
        openports.append(i)
    if i in range(1, 2048):
        time.sleep(0.01)
    else:
        time.sleep(0.001)

print(len(openports), "open ports were found:", openports)
