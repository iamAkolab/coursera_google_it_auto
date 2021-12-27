#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Programming with Files

# As an IT specialist, it's likely that you'll need to manipulate files and directories on a computer a lot. When you need to work on a large number of files and directories, 
# that's when automation can be a huge help. As a sysadmin, in my job, I interact with files and directories all the time, sometimes even if I have no intention of modifying them.
# For example, I use Python to check if a certain file exists on the file system before doing any other operations. 

# As you might remember, operating systems like Mac OS, Windows, and Linux use file systems to organize and control how data is stored and access. Data is usually stored on a disk
# and saved in files which are held in containers called directories or folders. File systems are usually organized in a tree structure with directories and files nested under 
# their parents. We know where a resource like a directory or a file is located within that tree structure by its path. 

# An absolute path is a full path to the resource in the file system. For example, on a Windows computer, the absolute path to the folder for the user Jordan would be 
# C:\Users\Jordan. On a Linux computer, the absolute path to the equivalent directory would be /home/jordan. We call it absolute path because it doesn't matter where in the file 
# system our script is running, the absolute path will always lead us to the resource. On the flip side, relative paths use only a portion of a path to show where the resource is 
# located in relation to the current working directory. 

# Relative paths are a shortcut that you can use so you don't have to write out the full file path. But keep in mind, they only makes sense relative to the current location. 
# So for example, if we list the contents of the directory examples, we'll get different outputs depending on what the current directory is. If our current directory is /home/jordan,
# we'll get the contents of /home/jordan/examples. But if the current directory is /user/share/doc/python3, we'll get the contents of /user/share/doc/python3/examples.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
