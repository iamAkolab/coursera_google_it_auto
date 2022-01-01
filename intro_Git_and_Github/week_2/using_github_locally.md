# Intro to Module 2: Using Git Locally

We'll start by learning some handy shortcuts and looking into how we can get more info out of our version control system. Then we'll experience the true power of Git by seeing how
we can undo some of our changes. The ability to revert previous changes is one of the most useful aspects of version control systems. Depending on what needs to be undone, there's 
a bunch of different techniques that we can use in Git. We can discard the changes made to a file, fix a commit that was incorrect and even roll back our project to an older 
snapshot. We'll look into all these techniques and dive into when to use each of them. Finally, we'll check out yet another important concept, Branches. We can use branches to 
work on an experimental feature without affecting the main code of our project. Support separate versions of a program that can't be merged together and much more. We'll dive 
into what branches are, when and how to use them and how to deal with merge conflicts.

# Skipping the Staging Area
When we covered the basic Git workflow, we called out that the process is usually to make changes, stage them, and then commit them. The separate step between staging and 
committing allows us to stage several changes in one commit.
The -a flag lets us add and commit in the same step.  At first, you might think that git commit dash a is just a shortcut for git add followed by git commit but that's not exactly true. Git commit -a doesn't work on new files because those are untracked. Instead, git commit -a is a shortcut to stage any changes to tracked files and commit them in one step. If the modified file has never been committed to the repo, we'll still need to use git add to track it first.

# $ cd scripts$

# $ atom all_checks.py

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

main()
'''

Now that we've made the change, we're ready to try out the new -a flag. We'll also use the -m flag to add the commit message directly. This time, we'll say that we're calling check underscore reboot and exiting with one on the error condition


# $ git commit -a -m "Check_reboot from main, exit with 1 on error"
[master fdb0987f] Call back check_reboot from main, exit with 1 on error
1 file changed, 4 insertions(+), 1 deletion(-)

These shortcuts are useful when making small changes that we know we'll want to commit directly without keeping them in the staging area and having to write long and complex descriptions. Keep in mind that when you use the -m shortcut, you can only write short messages and can't use the best practices regarding commit descriptions that we talked about earlier. So it's best reserved for truly small changes that don't require extra context or explanation, short and sweet. Heads up, when you use the -a shortcut, you skip the staging area. Meaning, you can't add any other changes before creating the commit. So you need to be sure that you've already included everything you want to include in that commit. In the end, using a shortcut like -a is just like using the regular commit workflow. The commit will show up in the log along with the message just as usual

# $ log

So let's clarify. Git uses the head alias to represent the currently checked out snapshot of your project. This lets you know what the contents of your working directory should be. In this case, the current snapshot is the latest commit in the project. We'll soon learn about branches. In that case, head can be a commit in a different branch of the project. We can even use git to go back in time and have head representing old commit from before the latest changes were applied. In all cases, head is used to indicate what the currently checked out snapshot is. This is how git marks your place in the project. Think about it as a bookmark that you can use to keep track of where you are. Even if you have multiple books to read, the bookmark allows you to pick up right where you left off. When you run git commands like diff, branch, or status, git will use the head bookmark as a basis for whatever operation it's performing. We'll see Head used when we learn how to undo things and perform rollbacks.
