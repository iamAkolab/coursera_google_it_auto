#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Working with Files

#  For these operations, we'll be using functions provided by the OS module. This module provides a layer of abstraction between Python and the operating system. 
# It allows us to interact with the underlying system without us knowing whether we're working on a Windows, Mac, Linux, or any other operating system supported by Python. 
# This means that you can write and test a script on one operating system like Windows and then run it on a different operating system like Linux. 
# But one thing to watch out for, paths can be different across different operating systems. So whenever we're using an absolute path in our code, we need to make sure we can 
# provide alternatives for the platforms we want to support. The OS module lets us do pretty much all the same tasks that we can normally do when working with files from the 
# command line. We can change the file permissions and delete or rename files through our code. This means you can write scripts to do these operations for you automatically

# So we first import the OS module. 
import os

# Then we call the remove function the OS module gives us and pass the string novel.txt which is the file we created earlier. 
os.remove("novel.txt")

# The file has now been deleted. Let's see what happens if we try to remove it again.
os.remove("novel.txt")
# fileNotFoundErroe

# We can easily rename a file with the rename function. The first parameter to rename function is the old name of the file and the second is new name. Let's check it out.
os.rename (" first_draft.txt", "finished_masterpiece.txt")

#  There's a sub-module inside the OS module for dealing with things related to file information like whether they exist or not. 
# This is called the OS path sub-module. We can use that exists function in this module to check whether a file exist. 
# Let's try this out with a couple of examples.
os.path.exists("finished_masterpiece.txt")
# True

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
