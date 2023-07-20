import os
import platform 

root = "crew"
password = "admin"

username = input("root@crew/: ")
passwordd = input("password@crew/: ")

if username == root and passwordd == password:
    while True:
        process = input('crewLinux/: ')
        if process == "info":
            os_type = platform.system()
            os_version = platform.version()
            print('System Type: {}\nVersion: {}\n'.format(os_type, os_version))
        elif process == "exit":
            os.remove
            print('Okey.')
else:
    print('[ERROR]: Your username or password is incorrect. (yes/no)')

# /*
#  Copyright (C) 2023
#  Crewdev
# */