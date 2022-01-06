# 1.0 Undoing Changes Before Committing

Being able to revert our changes is one of the most powerful features offered by version control systems. There's a bunch of different techniques available depending on which 
changes we need to undo. For example, you might find yourself in a situation where you've made a bunch of changes to a file but decide that you don't want to keep them. 
You can change a file back to its earlier committed state by using the git checkout command followed by the name of the file you want to revert. Speaking of, let's try this out 
using our scripts repository. We'll edit our all checks pi script and remove the check reboot function, then save and go back to the command line.

### ~$ cd scripts
### ~/scripts$ atom all_checks.py

''' 
#!/usr/bin/env python3

import os 
import sys

def check_reboot(): 
    """ Retruns True if the computer has a pending reboot.""" 
    return os.path.exist("/run/reboot-required")

def main(): 
     if check_reboot(): 
          print("Pending Reboot.") 
          sys.exit(1)
      print("Everything ok.")
      sys.exit(0)

main() 

'''
to 

''' 
#!/usr/bin/env python3

import os 
import sys

def main(): 
     if check_reboot(): 
          print("Pending Reboot.") 
          sys.exit(1)
      print("Everything ok.")
      sys.exit(0)

main() 

'''

### ~/scripts$ ./all_checks.py
Traceback (most recent call last)



By deleting that function, we've actually broke the script. Let's see what git status has to say about this. 


### ~/scripts$ git status
On branch master
Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>.." to discard changes in working directory)
  
  modified:   all_checks.py

no changes added to commit (use "git add" and/or "git commit -a")

As expected, we see that our file is modified and the changes aren't staged yet. Check out how git gives us a couple helpful tips on what to do now. 
We can run git add to stage our changes or we can run git checkout to discard them. If you need help remembering what this command does, think of it this way, 
you're checking out the original file from the latest storage snapshot. Let's do that now. We'll check out at the  original file and then take a look at what 
git status has to say about it and finally retry our script.
  
### ~/scripts$ git checkout all_checks.py
### ~/scripts$ git status
On branch master
nothing to commit, working tree clean

### ~/scripts$ atom all_checks.py

''' 
#!/usr/bin/env python3

import os 
import sys

def check_reboot(): 
    """ Retruns True if the computer has a pending reboot.""" 
    return os.path.exists("/run/reboot-required")

def main(): 
     if check_reboot(): 
          print("Pending Reboot.") 
          sys.exit(1)
      print("Everything ok.")
      sys.exit(0)

main() 

'''

### ~/scripts$ ./all_checks.py
Everything ok.


Done and done. With that, we've demonstrated how we can use git checkout to revert changes to modify files before they get staged. This command will restore the file to the 
latest storage snapshot, which can be either committed or staged. 
