# 1.0 Merging

A typical workflow for managing branches in Git, is to create a separate branch for developing any new features or changes. Once the new feature's in good shape, we merge the 
separate branch back into the main trunk of code. Merging is the term that Git uses for combining branch data and history together. We'll use the git merge command, which lets 
us take the independent snapshots and history of one Git branch, and tangle them into another

Let's try this out with our example branch from the last video. First, will check that we're in master branch, and then we'll call git merge even-better-feature to merge the 
even-better-feature branch into the master branch. Now we've brought the master branch up to speed, which we can see by looking at the git log.

### user@ubuntu:~/checks$ git branch
even-better-feature
*master

### user@ubuntu:~/checks$ git merge even-better-feature
updating 7d1de19...436810
Fast-forward
     free.memory.py | 6 ++++++
     1 file changed, 6 insertions(+)
     create mode 100644 free_memory.py

As we're on the master branch, HEAD points at master. We can see the even-better-feature and master branches are now both pointing at the same commit.

Git uses two different algorithms to perform a merge, fast-forward and three-way merge. Th/e merge we just performed is an example of a fast-forward merge. This kind of merge 
occurs when all the commits in the checked out branch are also in the branch that's being merged. If this is the case, we can say that the commit history of both branches doesn't 
diverge. In these cases, all Git has to do is update the pointers of the branches to the same commit, and no actual merging needs to take place. 

On the other hand, a three-way merge is performed when the history of the merging branches has diverged in some way, and there isn't a nice linear path to combine them via fast-forwarding. This happens when
a commit is made on one branch after the point when both branches split.

In our case, this could have happened if we made a commit on the master branch after creating the other branches.

When this occurs, Git will tie the branch histories together with a new commit. And merge the snapshots at the two branch tips with the most recent common ancestor, the commit 
before the divergence. To do this successfully, Git tries to figure out how to combine both snapshots. If the changes were made in different files, or in different parts of the
same file, Git will take both changes and put them together in the result. If instead the changes are made on the same part of the same file, Git won't know how to merge those
changes, and the attempt will result in a merge conflict. This sounds scary, but don't panic. Git doesn't quit, we'll solve those conflicts in our next video.

# 2.0 Merge Conflicts

From time to time, we might find that both the branches we're trying to merge have edits to the same part of the same file. This will result in something called a merge conflict. Normally, Git can automatically merge files for us. But when we have a merge conflict, it will need a little help to figure out what to do. To see how this would look, let's edit the free_memory.py file in the master branch and replace the pass statement with a comment about what the main function should do

### user@ubuntu:~/checks$ atom free_memory.py

### free_memory.py
#!/usr/bin/env python3

def main():
    """Checks if there's enough free money in the computer."""
    
main()



Cool, we made the change so let's save it and commit it back to our master branch.


### user@ubuntu:~/checks$ git commit -a -m 'Add commnet to Main()'
[master fef2fc5]  Addc omment to main()
1 file changed, 2 insertions(+), 2 deletions(-)

Next, Let's check out the even-better-feature branch and make a change in the same place. In this case, we will replace the call to pass with a call to print, saying that everything is okay.


### user@ubuntu:~/checks$ git checkout even-better-feature
Switched to branch 'even-better-feature'


### user@ubuntu:~/checks$ atom free_memory.py


### free_memory.py
#!/usr/bin/env python3

def main():
    print("Everything is ok.")
    
main()


Now, we'll save this other change and commit it to this branch.


### user@ubuntu:~/checks$ git commit -a -m 'Print everything is ok'
[even-better-feature ca6de99]  Print everything is ok
1 file changed, 2 insertions(+), 2 deletions(-)

### user@ubuntu:~/checks$ git checkout master

We are primed for chaos with our file all setup for a merge conflict. Let's check out the master branch again and try to merge the even-better-feature back into it.


### user@ubuntu:~/checks$ git merge even-better-feature
Auto-merging free-memory.py
CONFLICT (content): Merge conflict in free_memory.py
Automatic merge failed; fix conflicts and then commit the result

Git tells us it tried to automatically merge the two versions of the free memory file, but it didn't know how to do it. We can use Git's status to get more information about what's going on.


### user@ubuntu:~/checks$ git status

As usual, git status gives us a lot of additional information. It tells us that we have files that are currently unmerged, and that we need to fix the conflicts or abort the merge if we decide it was a mistake. It also tells us that we need to run Git add on each unmerged file to mark that the conflicts have been resolved. Let's get to work. To fix the conflict, let's open up free_memory.py in our text editor.

### user@ubuntu:~/checks$ atom free_memory.py


### free_memory.py
#!/usr/bin/env python3

def main():
    Use me =
    <<<<<<<<<<<<<<< HEAD
    """Checks if there's enough free money in the computer."""
===========
     print("Everything is ok.")
     >>>>> even-better-feature
     Use me =
 
main()

Thankfully, Git has added some information to our files to tell us which parts of the code are conflicting. The unmerged content of the file at head, remember, in this case, head points to master, is the docstring stating what the main function should do. The unmerged content of the file in the even-better-feature branch is the call to the print function. It's up to us to decide which one to keep or if we should change the contents of the file altogether. In this case, we'll keep both statements and delete the merger markers.

### free_memory.py
#!/usr/bin/env python3

def main():
    """Checks if there's enough free money in the computer."""
     print("Everything is ok.")
 
main()


Now that we've fixed the conflict, we'll mark it as resolved by running git add on the file, and then call the git status to see how our merge is doing. See how Git now tells us that all conflicts have been resolved. Woo-hoo, we just need to call git commit to wrap up the merge.


### user@ubuntu:~/checks$ git add free_memory.py
On branch Master
All conflicts fixed but you are still to merge


### user@ubuntu:~/checks$ git commit

The comments that git commit shows us look different than other commits. That's because this is a merge and Git tells us so. It also tells us which file had conflicts which have now been resolved. The commit already has a description saying that it's merging the other branch. This description was automatically created when we called the git merge command. But we can add onto this description if we want. For example, we can say that we're keeping the lines from both branches, and then just save and exit as usual.


The merge conflict is resolved. 


### user@ubuntu:~/checks$ git log --graph --online

To see what the commit history looks like now, we'll use a couple of handy options to the git log command; --graph for seeing the commits as a graph, and --oneline to only see one line per commit. 

This format helps us better understand the history of our commits and how merges have occurred. We can see the new commit that was added and also the two separate commits that we merged. One coming from the master branch and the other coming from the even-better-feature branch. 

We can also see that master is pointing to the merge commit but even-better-feature is still pointing to the previous one. 


In our example, resolving the conflict was straightforward and easy. But in the real world, this won't always be the case. Merge conflicts can sometimes be tricky, complicated, and spread across multiple files. 


If you want to throw the merge away and start over, you can use the git merge --abort command as an escape hatch. This will stop the merge and reset the files in your working tree back to the previous commit before the merge ever happened. So by now you know how to create, delete, and switch between branches in Git. You've also seen that each branch represents a pointer to a commit in a sequence of independent snapshots. You know how to merge these commits back into the main trunk by using the git merge command.
