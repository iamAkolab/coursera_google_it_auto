First, all the files we want to manage with Git must be a part of a Git repository. We initialize a new repository by running the git init command in any file system directory.

### $ mkdir scripts
### $ cd scripts
### $ git init

$ git config -l 
There's a bunch of info in there, and we won't cover all of it. For now, pay special attention to the user.email and the user.name lines

# create the all_check.py file
'''
#!/usr/bin/env python3

def main():
    pass
    
main
'''


### $ chdmod +x all_checks.py
### $ git status
the file is untracked

### $ git add all_checks.py
 move from untracked to stage status and a change it from modified stage to staged state

### $ git commit 
then add comments with nano 'create an empty all_checks.py'


When committing new files or changes with git commit, the user is asked to provide a commit message. What will happen if an empty commit message is entered? 
The commit is aborted


# modify the all_check.py file
'''
#!/usr/bin/env python3

import os

def check_reboot():
     """ Returns True if the computer has a pending reboot."""
     return os.path.exist("/run/reboot-required")
     
def main():
    pass
    
 $ git status
 $ git add all_checks.py
 $ git status
 
 $ git commit -m 'Add a check_reboot function'
 
 
    
main
'''

# Anatomy of a Commit Message 
 A commit message is generally broken up into a few sections. The first line is a short summary of the commit followed by a blank line. This is followed by a full description of the changes which details why they're necessary and anything that might be especially interesting about them or difficult to understand. When you run the git commit command, Git will open up a text editor of your choice so you can write your commit message
 
 
 Take a look at what git tracks as part of the log. It's packing a lot of information in just a few lines. The first thing listed for each commit is its identifier, which is a long string of letters and numbers that uniquely identify each commit. The first commit in the list also says that the head indicator is pointing to the master branch. If this is gibberish to you, don't worry. We'll talk more about what a head and master means in later videos. For each commit, we see the name and the email of the person who made the commit which is indicated as the author. Then we get the date and time the commit was made. Finally the commit message is displayed. Our commit messages are very brief as we're just starting to work on our repository. As the work we do becomes more complex, we'll probably write longer descriptions with a lot more detail
