#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Check the health of computer

## $ python3

# >>> import shutil

# >>> du = shutil.disk_usage("/")
# print(du)
# usage(total = 125479232000, used = 11327320064, free = 107742113792)

# >>> du.free/du.total*100
# 85.85831988379

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Check the CPU Usage

# For this, we can use another module called psutil. This includes a cpu_percent function that returns a number showing how much of the CPU is being used. The amount of CPU used 
# at each instant can change a lot, since processes are starting and finishing all the time. So this function receives an interval of seconds and returns an average percentage of 
# usage in that interval

# >>> import psutil

# >>> psutil.cpu_percent(0.1)
# 0.0

# >>> psutil.cpu_percent(0.1)
# 5.0

# >>> psutil.cpu_percent(0.1)
# 2.5

# >>> psutil.cpu_percent(0.1)
# 4.9

# >>> psutil.cpu_percent(0.1)
# 2.5

# >>> psutil.cpu_percent(0.1)
# 2.5

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
