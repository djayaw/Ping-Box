import os
import re
import time

def ipchecking():
    f = open("text.txt", "r")
    t = f.readline()
    splitting = t.split(' ',)
    timer = splitting[3]
    for x in f:
        ipcheck = re.findall("^IP:",x)
        if ipcheck:
            hostname = x[4:]
            response = os.system("ping -c 1 " + hostname)
            if response == 0:
                print(hostname+" is up!")
            else:
                print (hostname+" is down!")
    sleeping = int(timer)
    time.sleep(sleeping)

while True:
    ipchecking()
