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
## More File Information

# We can get a lot more info about our files using functions in OS.path module. 
# For example, to check how big a file is, we can use the getsize function which returns the file size in bytes.
os.path.getsize("spider.txt")


# To check when the file was last modified, the getmtime function comes in really handy. Let's check out how this works.
os.path.getmtime("spider.txt")
# 15783222923.89999994

# What's that long number? It doesn't look like time, does it? That's because it's a timestamp. In this case specifically, it's a Unix timestamp. It represents the number of 
# seconds since January 1st, 1970. Seems a bit random, but there's actually a really good reason behind this date.

# While Unix timestamps have a 50-year history, they're still very much present today. They're used by file systems to show when a file was created, accessed, or modified. 
# They are also used in other systems like databases. As an IT specialist, you're bound to run into them in your day to day. But despite all of that, the number is pretty hard
# to make sense of. We can use the datetime module to make it easier for us humans to read, like this

import datetime

timestamp = os.path.getsize("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
# datetime.datetime(2020, 1, 6, 7, 2,3, 899999)

# Remember, the functions and the OS.path module take the info provided by the operating system so that we can use it in our scripts no matter what OS we're running. 
# We can check a file size or last modification date without having to know the operating system the machines running or the type of file system that the file stored in

#######################################################################################################################################################################
# Some more functions of the os.path module include getsize() and isfile() which get information on the file size and determine if a file exists, respectively. 
# In the following code snippet, what do you think will print if the file does not exist?

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")
    
# False 
# File not Found

# Awesome! Because the file does not exist, getsize() will never be called and our error message will be printed instead.

#  Another cool feature of the functions is that we can work with both relative and absolute paths. In our examples, we've been using the relative file names without having to 
# specify their full paths. In some cases, we may need to specify exactly where the file is to work with it in our script. This is where the abspath function can help.

os.path.abspath("spider.txt")
'/home/user/spider.txt'

# The abspath function takes a filename and turns it into an absolute path. Python uses the current working directory which is where the script is being run to start looking 
# for the file and construct the full path that identifies it. This is useful if you want to store at the file's full path or access a file no matter what the current 
# directory is. There is a ton more functions in the OS and OSpath modules that let us work with files.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Directories

# As with files, Python provides a bunch of different functions that let us create, delete and browse the contents of directories
# To check which current directory your Python program is executing in, you can use the getcwd method. 
# If you use a unix-like system, you might remember that the name of the command that prints the working directory is called pwd

print(os.getcwd())
# /home/user

#  To create a directory, we use the mkdir function. This function has the same name as both the Windows and Linux commands that do the same exact thing.
os.mkdir("new_dir")

# You can also change directories in your program by using the chdir function and passing the directory you'd like to change to as a parameter. 
# Just like the other functions we've seen, we can use relative or absolute paths to do that.
os.getcwd()
# '/home/user/new_dir'

# we can use our rmdir to remove them like this
os.mkdir("newer_dir")
os.rmdir("newwer_dir")

# but the rmdir function will only work if the directory is empty. If we try to remove a directory that has files in it, we get an error. 
# We need to first delete all the files and sub-directories in that directory before we can actually remove it


# The os.listdir function returns a list of all the files and sub-directories in a given directory. Let's see how this looks for our website directory.

import os

os.listdir("website")
['images', 'index.html', 'favicon.ico']

# So we've got a list of strings. Since they're just strings, we don't know if they're directories or files. 
# To find out what they are, we can use functions like os.path.isdir but before we look at how that works. See how the list contains just file names. 
# If we want to know whether one of these files is a directory, we need to use os.path.join to create the full path. Let's see all of this in action now.

dir - "website" 
for name in os.listdir(dir):
   fullname = os.path.join(dir,name)
   if os.path.isdir(fullname):
      print("{} is a directory".format(fullname))
   else:
      print("{} is a file".format(fullname))

# website/images is a directory
# website/index.html is a file
# website/favicon.ico is a file

# This code is doing a bunch of interesting stuff but let's go through it step-by-step. First, we're defining a dir variable with the name of the directory that we want 
# to check. This makes our code more readable and more usable. Then we're iterating through the file names returned by the os.listdir. We know from our previous execution 
# of this function that these are just the names of the files without directory. So using os.path.join, we join the directory to each of those file names and create a String 
# with a valid full name. Finally, we use that full name to call os.path.isdir to check if it's a directory or a file. 

# Well, the join function let's us be independent from the operating system again. 
# In Linux and MacOS, the portions of a file are split using a forward slash. 
# On Windows, they're split using a backslash. 
# By using the os.path.join function instead of explicitly adding a slash, we can make sure that our scripts work with all 
# operating systems. It's another one of those handy little tools that help us avoid errors when working on different platforms. 

# As we called out earlier, there's a lot of Functions to manage directories in Python and we only covered a handful here.

# Files and Directories Cheat-Sheet
# Check out the following links for more information:

https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/os.path.html
https://en.wikipedia.org/wiki/Unix_time
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
