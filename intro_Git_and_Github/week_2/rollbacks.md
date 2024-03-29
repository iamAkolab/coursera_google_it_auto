# 3.0 Rollbacks

Fixing your work before you commit is good. But what happens if it's already been snapshotted by Git? Let's say you host to Git repository on a company server that contains all 
kinds of useful automation scripts that you and your coworkers use. One morning before coffee, you make a few changes to one of these scripts and commit the updated files. 
A few hours later, you start to receive tickets from users indicating some part of the script is broken. From the errors they describe, it sounds like the problem is related 
to your recent changes. Oh, you could look at the code you updated to see if you can spot the bug. But more tickets are pouring in and you want to fix the problem as fast as 
possible. You decided it's time for a rollback. There are a few ways to rollback commits in Git. For now, we'll focus on using the git revert command. Git revert doesn't just 
mean undo. Instead, it creates a commit that contains the inverse of all the changes made in the bad commit in order to cancel them out. For example, if a particular line was 
added in the bad commit, then in the reverted commit, the same line will be deleted. This way you get the effect of having undone the changes, but the history of the commits 
in the project remains consistent leaving a record of exactly what happened. So git revert will create a new commit, that is the opposite of everything in the given commit. 
We can revert the latest commit by using the head alias that we mentioned before. Since we can think of head as a pointer to the snapshot of your current commit, when we 
pass head to the revert command we tell Git to rewind that current commit, makes sense? To check this out, we'll first add a faulty commit to our example repo.

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
     if disk_full():
          print("Disk Full.")
          sys.exit(1)
      print("Everything ok.")
      sys.exit(0)

main() 

'''

### ~/scripts$ git commit -a -m 'Add call to disk_full function'

So now, our code is committed. We didn't even test it which is a bad idea if you're doing this for real. You might have already spotted the problem with our code. 
This is where users start filing tickets and saying that things are broken, and so we run our script to see what happens.

Oops, we use the function that we forgot to define. Okay. It's rollback time. Let's get rid of this faulty code by typing git revert head. So once we issue that git revert 
command, we're presented with the text editor commit interface that we've all seen before. In this case, we can see that git has automatically added some text to the command 
indicating it's a rollback. The first-line mentions that it's reverting the commit we just did called Add call to disk full function. The extra description even includes the 
identifier of the commit that got reverted. While we could use this description as is, it's usually a good idea to add an explanation of why we're doing the rollback. Remember 
that the goal of these descriptions is to help our future selves understand why things happen. In this case, we'll explain that the reason for the rollback is that the code was 
calling a function that wasn't defined.

### ~/scripts$ git revert HEAD
[master 0832461] Revert "Add call to disk_full function"
1 file changed, 3 deletions(-)

Once we're done entering the description, we can exit and save as usual. You'll notice the output that we get from the git revert command looks like the output of the git commit
command. This is because git revert creates a commit for us. Since a revert is a normal commit, we can see both the commit and the reverted commit in the log. Let's look at the 
last two entries in the log using dash P and dash two as parameters. As demonstrated before, the dash P parameter lets us see the patch created by the commit while the dash two 
perimeter limits the output to the last two entries. So in this log, we can see that when we called revert, git created a new commit that's the inverse of the previous one. This
removes the lines that we added in the previous commit. We can see that the original commit shows the lines we added by preceding them with a plus sign. The same line shows up 
with a minus sign in the newer commit message indicating that they were removed. Just like that, the bad commit is reverted and the error stopped. In this example, we reverted 
the latest commit in our tree. 
