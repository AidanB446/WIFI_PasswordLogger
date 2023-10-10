# importing subprocess

# This only works for windows, I haven't (and probably wont) write it for macOS or Linux.

import subprocess

def getInterfaces() :
    names = [] # this is the object well return
    
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True) # command to get the interface names

    data = meta_data.decode('utf-8', errors ="backslashreplace") # used so we can parse it as a string

    data = data.split('\n') 

    for i in data:

        if "All User Profile" in i :

            i = i.split(":") # name always comes after the colom
            
            i = i[1] # wifi name

            # first and last character is use less
            i = i[1:-1]

            names.append(i) # add to list 

    return names


msg = ""

for name in getInterfaces() :
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], shell=True)
    
    msg = msg + meta_data.decode('utf-8', errors="backslashreplace")


f = open("savedWifiData.txt", 'w')
f.write(msg)
f.close()


