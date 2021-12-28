#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is a CSV file?

# Formats give data structure. And remember that computers love structure and precision. To be able to process a data set, it helps to know ahead of time how that data set will
# be arranged. If you can expect data to be represented in a certain way, it's easier to extract meaning from it.

# Let's look at a very simple example. If we have a file that contains one line per machine and details the users are logged into that machine, then when we read the file we know
# how to parse it to get the information that we want. 

# Parsing a file means analyzing its content to correctly structure the data. We use a bunch of different file formats to structure, store, and transport data. You might be 
# familiar with some already. For example, HTML is a markup format which defines the content of a webpage. JSON is a data interchange format commonly used to pass data between 
# computers on networks, especially the internet. CSV or comma separated values is a very common data format used to store data as segment of text separated by commas. 

# In the Python standard library, you'll find classes and modules for working with many of these data formats, including CSV and HTML. 

# Knowing how to work with CSV files is a pretty useful skill to know. This format lets us easily store and retrieve information that we might need for our scripts like employees
# in our company or computer's inner network. In my job as a system administrator, I create CSV files when I want to convert the output of a command into a format that will be 
# easier to parse later on. For example, the df command prints the currently used disk space in a format that's easy to read by human eyes.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Reading CSV Files

# CSV stands for Comma Separated Values. CSV is a pretty simple format. Each field in that record is separated by a comma, with the contents of the field stored between the commas. 
# For example, if we are storing information about employees at our company, we might store the data like this.

$ cat csv_file.txt
Sabrina Green, 802-867-5309, Sys Admin
Eli Jones, 684-278-0983, IT 
Charles Rivera, 789-234-5678, Web developer

# So, we'll be using the CSV module. And to do that, we'll need to import it like we've been doing with the other modules.

import csv

# Now, before we can parse a CSV file, we need to open the file the same way as before.
f = open("csv_file.txt")

# now we can parse this file using the CSV module.
csv_f = csv.read(f)

# Okay, that has given us an instance of the CSV reader class. We can now iterate through its contents and access information that it parsed.
for rows in csv_f:
    name , phone, role = row
print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))



# As we mentioned, we unpack the row so that we don't have to use indexes to access each element in that list. For example, we could have used row[0] to access the name of 
# the employee. This is valid but it can be hard to follow when reading a lot of code. Unpacking the list into name variables makes the code easier to understand later on. 
# And before we forget, let's close this file now that we're done with it.

f.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Generating CSV

# We'll start by storing the data that we want to write into a list.

hosts = [ ["workstation.local","192.168.25.46"], ["webserver.cloud","10.2.5.6"]
         
# We've created a list of lists. This is the data that we want to store in the CSV file, representing the names of the machines in our network and their IP addresses. 
# All right, with that data ready to be written, let's open the file in write mode. We'll use the width block that we saw before so we don't forget to close the file.
# Now that we have the file opened for writing, let's call the writer function of the CSV module with this file as a parameter
# The writer variable is now an instance of a CSV writer class. There are two functions that we can use: write row, which we'll write one row at a time; and write rows, 
# which we'll write all of them together. In this case, we already have all the data that we want to write. So we'll call right rows.
# With that, we've run our data to the CSV file. Before we move on, let's see how this looks when we use a tool outside of Python, like the cat command.
         
with open('host.csv', 'w') as hosts_csv:
         writer = csv.writer(host_csv)
         writer.writerows(hosts)
         
 $ cat host.csv
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Reading and Writing CSV Files with Dictionaries

# In our earlier examples, we saw how we can read and write CSV files, and we use list as datatype on the Python side. This works when we know what the fields are going to be, 
# but it can be pretty cumbersome when we have a lot of columns, and we need to remember which is which. Imagine if your lists of employees not only had name, phone number and 
# role but also start date, username, office location, department, preferred pronouns and so on. It would soon get hard to keep track of which column corresponds to which 
# position in the row. For cases like this, it's common for CSVs to include the names of the columns as a first line in the file, like in this example; this CSV file list a 
# bunch of internally developed programs used at the company including the latest version, the current development status and the number of people using it. Check out how the 
# first line of the file includes the names of each of the fields
         
$ cat software.csv
 # name, version. status, users
 # MailTree, 5.34, production, 324
 # CalDoor, 1.25, beta, 22
 # Chatty Chicken, 0.34, alpha, 4
 
# We can profit from this additional information by using DictReader, a slightly different reader that's also provided by the CSV module. This reader turns each row of the data
# in a CSV file into a dictionary. We can then access the data by using the column names instead of the position in the row. Let's see how that looks. 

with open('software.csv') as software:
         reader = csv.DictReader(software)
         for row in reader:
             print(("{} has {} users").format(row["Name"], rows["users"]))
         
# MailTree has 324 users
# CalDoor has 22 users
# Chatty Chickens has 4 users
         

# So here we're opening the  file and creating a DictReader to process our CSV data, then when going through the rows we can access information in each row using the keys just 
# like we would when accessing data in the dictionary. See how we use row, name and row users to get the name of the number of users.
         
# we can use DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries. This means that each element in the list will be a row in the file, 
# and the values of each field will come out of each of the dictionaries. For this to work, we'll also need to pass a list of the keys that we want to be stored in the file 
# when creating the writer. Let's see this in action.
         
 # First we need a list of dictionaries with the data that we want to store. For this example, we want to store data about the users in our company and the departments that 
 # they work in. So here we have our list of dictionaries and each contain the keys, name, username and department.
  
users = [ {"name": "Sol Mansi", "username": "solm", "separtment": "IT Infrastructure"}, 
          {"name": "Sol Mansi", "username": "solm", "separtment": "IT Infrastructure"},
          {"name": "Sol Mansi", "username": "solm", "separtment": "IT Infrastructure"},]
   
# So we first define the list of keys that we want to write to the file       
keys = ["name", "username", "deparemnt"]
   
 # then we open the file for writing. Next we created the DictWriter passing the keys that we had identified before, and then we call two different methods on the writer. 
 # The right header method will create the first line of the CSV based on keys that we passed, and the right rows method will turn the list of dictionaries into lines in that file  
         
 with open('by_department.csv', 'w') as by_department:
         write = csv.DictWriter(by_department, fieldnames = keys)
         write.writeheader()
         writer.writerows(users)
         
# To check if it works correctly 
$ cat by_department.csv
         
# You can read, write and work with files and directories, and now, you can also read and write CSV files      
         
         
# DictReader() allows us to convert the data in a CSV file into a standard dictionary. DictWriter() \ allows us to write data from a dictionary into a CSV file. 
# What’s one parameter we must pass in order for DictWriter() to write our dictionary to CSV format? The fieldnames parameter of DictWriter() requires a list of keys
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## CSV Files Cheat Sheet

# Check out the following links for more information:
# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
