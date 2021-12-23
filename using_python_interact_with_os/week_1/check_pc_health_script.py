#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Check your pc health script

# step 1 -- set up python script to use use interpreter with shebang
# step 2 -- import neccessary modules
# step 3 -- define a check_disk_usage function that will receive a distant check and return true if there's more than 20 percent free or false if it's less.
# step 4 -- define a check_cpu_usage function that will check the usage for a whole second. We'll say the machine is healthy, it a cpu_usage is less than 75 percent.

'''
#!/usr/bin/env python3
 
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20
    
def check_cpu_usage():
   usage = psutil.cpu_percent(1)
   return usage < 75
   
 if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
   print("Everything is ok")
'''

# step 5 -- save our script as health_checks.py
# step 6 -- change to executable
# $ chmod +x health_checks.py

# step 7 -- run the script
# ./health_checks.py

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
