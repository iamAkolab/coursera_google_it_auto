 $ mkdir checks
 $ cd checks
 
 $ git init
 # when we run git init we initialize an empty git repository in the current directory.

 $ ls -la
 $ ls -l .git/
 # check that this directory exist using the ls-la command which lists files that start with a dot
 # We can also use the ls-l.git command to look inside of it and see the many different things it contains. This is called a Git directory.
 
 # The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current versions of the files.
 
 
 $ cp ../disk_usage.py
 $ ls -l
 
$ git add disk_usage.py
# To make Git track our file, we'll add it to the project using the git add command passing the file that we want as a parameter. With that, we've added our file to the staging area
# The staging area which is also known as the index is a file maintained by Git that contains all of the information about what files and changes are going to go into your next command. 

$ git status
# We can use the git status command to get some information about the current working tree and pending changes.

$ git commit
To get it committed into the.git directory, we run the git commit command

When we run this command, we tell Git that we want to save our changes. It opens a text editor where we can enter a commit message. 
If you want, you can change the editor used to your preferred editor. In our case, this computer has nano configured as a default editor. 
The texts that we get tells us that we need to write a commit message and that the change to be committed is the new file that we've added. 
We'll deep dive into commit messages later. For now, let's enter a simple description of what we did which was to add this one file and 
hen exit the editor saving our commit message and with that we've created our first git commit
