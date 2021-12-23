#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Working with Python Scripts

# Option 1: Windows Users: Connecting to your VM
# In this section, you will use the PuTTY Secure Shell (SSH) client and your VM’s External IP address to connect.
# Download your PPK key file

# Connect to your VM using SSH and PuTTY
# You can download Putty from here https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe
# In the Host Name (or IP address) box, enter username@external_ip_address.
# In the Category list, expand SSH.
# Click Auth (don’t expand it)
# In the Private key file for authentication box, browse to the PPK file that you downloaded and double-click it.
# Click on the Open button.
# Click Yes when prompted to allow a first connection to this remote SSH server. Because you are using a key pair for authentication, you will not be prompted for a password.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Fix file permissions

# We have a python script ready for you. From your home directory (~), use the following command to navigate to the scripts directory:
'''
student-02-4c5016a37ae5@linux-instance:~$ cd scripts
student-02-4c5016a37ae5@linux-instance:~/scripts$ ls
health_checks.py
student-02-4c5016a37ae5@linux-instance:~/scripts$ cat health_checks
cat: health_checks: No such file or directory
student-02-4c5016a37ae5@linux-instance:~/scripts$ cat health_checks.py
#!/usr/bin/env python3
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
student-02-4c5016a37ae5@linux-instance:~/scripts$ ./health_check.py
-bash: ./health_check.py: No such file or directory
student-02-4c5016a37ae5@linux-instance:~/scripts$ ./health_checks.py
-bash: ./health_checks.py: Permission denied
student-02-4c5016a37ae5@linux-instance:~/scripts$ ls
health_checks.py
student-02-4c5016a37ae5@linux-instance:~/scripts$ sudo chmod +x health_checks.py                                                                                                                                                             student-02-4c5016a37ae5@linux-instance:~/scripts$ ./health_checks.py
ERROR!
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Debug the issue

# The Python script returns ERROR only if there's not enough disk usage or CPU usage. Try to debug this issue.
# Hint: The problem is that the function check_cpu_usage should return true if the CPU usage is less than 75%, but in this case, it returns false.

'''
student-02-4c5016a37ae5@linux-instance:~/scripts$ nano health_checks.py
student-02-4c5016a37ae5@linux-instance:~/scripts$ ./health_checks.py
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Create a new Python module

# you are going to write a Python module. A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
# The module you are going to write will be used to test the network connections

# install the request module
# navigate to the scripts directory first and then create the file
# Create a file named network.py
# Use nano editor to create a new file network.py:

'''
student-02-4c5016a37ae5@linux-instance:~/scripts$ sudo apt install python3-requests
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  python3-chardet python3-urllib3
Suggested packages:
  python3-openssl python3-socks
The following NEW packages will be installed:
  python3-chardet python3-requests python3-urllib3
0 upgraded, 3 newly installed, 0 to remove and 37 not upgraded.
Need to get 275 kB of archives.
After this operation, 1,337 kB of additional disk space will be used.
Do you want to continue? [Y/n] cd ~/scripts
Abort.
student-02-4c5016a37ae5@linux-instance:~/scripts$ cd ~/scripts
student-02-4c5016a37ae5@linux-instance:~/scripts$ nano network.py
student-02-4c5016a37ae5@linux-instance:~/scripts$ cat network.py
'''

# Add a shebang line to define where the interpreter is located
# Import the request module into the file using the import statements.
# import the socket module.
# write a function check_localhost, which checks whether the local host is correctly configured. We do this by calling the gethostbyname within the function.
# Pass the parameter localhost to the function gethostbyname. The result for this function should be 127.0.0.1.
# Edit the function check_localhost so that it returns true if the function returns 127.0.0.1
# function called check_connectivity
# use the request module for this, and call the GET method by passing http://www.google.com as the paramet
# This returns the website's status code. This status code is an integer value. Now, assign the result to a response variable and check the status_code attribute of that variable. It should return 200.
# Edit the function check_connectivity so that it returns true if the function returns 200 status_code.
'''
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost=="127.0.0.1"

def check_connectivity():
        request = requests.get("http://www.google.com")
        return request.status_code== int(200)
'''


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Use the Python module

# open the script health_checks.py
# Now import network module at the beginning of the file.
# Replace the else part with an elif clause.
'''
elif check_localhost() and check_connectivity():
    print("Everything ok")
Copied!
Add an else part at the end of the file.

else:
    print("Network checks failed")
    '''

## Once you have completed editing the file, press Ctrl-o, Enter, and Ctrl-x to exit.

## ./health_checks.py


'''
#!/usr/bin/env python3

from network import *
import shutil
import psutil

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
    
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage <75
    
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
'''
