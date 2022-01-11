# 1.0 Branches 

Branches are an important part of the Git work flow. 

In Git, a branch at the most basic level is just a pointer to a particular commit. But more importantly, it represents an independent line of development in a project. Of which 
the commit it points to is the latest link in a chain of developing history. 

The default branch that Git creates for you when a new repository initialized is called master. 

All of our examples and development have taken place on this branch so far. The master branch is commonly used to represent the known good state of a project. When you want to 
develop a feature or try something new in your project, you can create a separate branch to do your work without worrying about messing up this current working state.

If this  seems confusing, maybe an analogy will help. You can think of a Git project as an assignment your teacher gives you in a class. You do all your work on the assignment in a set 
of notebooks, each notebook representing a different branch. You use some notebooks to jot down rough drafts in experiments, but you keep one notebook the master branch, in a 
tidy state and you copy the polish versions of these drafts into it. No doodling in the master note book, please. Branches make it really easy to experiment with new ideas or 
strategies and projects. When you want to add a feature or fix something, you can create a new branch and do your development there. You can merge back into the master branch, 
when you've got something you like, or discard your changes without negative impact if they don't work out. 

In Git, branches are used all the time, as a part of the normal development workflow. As an example, think back to the problematic commit we fixed in an earlier video. We added a call to the disk full function, but forgot to actually 
define the function. So we had to roll it back because our users we're seeing errors. Knowing what we know now, we could have done that work on a separate branch, maybe called 
something like add disk full. In that case, we could have iterated on our code there until it was working correctly, without it effecting the master branch. Only after the code 
is ready to be deployed, we would merge those changes back into the master branch. 

In the next few videos, we'll look into how to create new branches and merge their content into the master branch. We'll also go over what to do if you run into any scary merge
conflicts. 

# 2.0 Creating New Branches
As branches are essential to how work is done in git, there's tons of different ways to work with them. We can use the git branch command to list, create, delete, and manipulate branches. Running git branch by itself will show you a list of all the branches in your repository. Let's try it out in our checks repo.

### user@ubuntu:~$ cd checks
### user@ubuntu:~/checks$ git branch
*master


Our list is looking pretty empty right now, but don't worry. Creating a branch is a snap. We do it by calling git branch with the name of the new branch Let's create a new feature branch and then list the branches again with git branch. 

### user@ubuntu:~/checks$ git branch new-feature
### user@ubuntu:~/checks$ git branch
*master
new-feature

Our new branch was created based on the value of head. Remember that this might not necessarily be the master branch. The list we get shows that we're still on the master branch. We can tell because the current branch is indicated in the command's output with an asterisk in a different color.

Right now we want to switch to a new branch. To do that, we'll need to use the git checkout command. We saw earlier how we can use git checkout to restore a modified file back to the latest commit. Checking out branches is similar in that, the working tree is updated to match the selected branch including both the files and the git history. 
It might help to remember that we use git checkout to check out the latest snapshot for both files and for branches. All right. Let's switch to our new feature branch by calling git checkout new feature, and then listing our branches once again.

### user@ubuntu:~/checks$ git checkout new-feature
Switched to branch 'new-feature'
### user@ubuntu:~/checks$ git branch
master
*new-feature

Before we were working on the master branch but now that we've changed to our new branch, the star has moved to new feature. 

Creating a branch and switching to it immediately is a pretty common task. So common that git gives us a useful shortcut to create a new branch and to switch to it in a single command. We can use the git checkout -b new branch to do this. Take a look.

### user@ubuntu:~/checks$ git checkout -b even-better-feature
Switched to a new branch 'even-better-feature'

See how the message says that we've switched to a new branch? Git created the new branch and switched to it in just one command. Super efficient. Now that we have our shiny new branch, let's create a new file in. We'll create a new Python3 file, that will include the usual shebang line and empty main function and a call to that function.

### user@ubuntu:~/checks$ atom free_memory.py

### free_memory.py
#!/usr/bin/env python3

def main():
    pass
    
main()

This file is empty because it's only the beginning of our work. As it's in a separate branch, it's okay for it to not be finished yet. Let's save our file and commit it to the current branch now.

### user@ubuntu:~/checks$ git commit -m 'Add an empty free_memory.py'
[even-better-feature 4361880] Add an empty free_empty.py
1 file changed, 6 insertions(+)
create mode 100644 free_memory.py

We've added a commit in this branch and it's looking better. Let's check the last two entries in the log.

### user@ubuntu:~/checks git log -2
commit 7d361880r74704229ir9qr9i39 (HEAD -> even-better-performance)
Author: My name < mw@example.com>
Date: Mon Jan 6 09:47:07 2020 -0800
       Add an empty free_memory.p
       
commit 4361880r74704229ir9qr9i39 (new-feature, master)
Author: My name < mw@example.com>
Date: Mon Jan 6 09:15:58 2020 -0800
       Revert "New name for disk_usage.py"
       Rollback reason: the previous name was actually better :)
       This reverts commit 30e87d45hd489gfh
     
We see the last two commits in this branch. Notice how next to the latest commit ID, git shows that this is where head is pointing to and that the branch is called even better feature. Next to the previous commit, git shows that both the master and the new feature branches are pointing to that snapshot of the project. In this way, we can see that the even better feature branch is ahead of the master branch. With that, we've seen how we can create new branches and commit changes to them. You might say your knowledge of branches has grown.

# 3.0 Working with Branches

Let's check out the current status of our repo by calling git status and ls dash l.

### user@ubuntu:~$ cd checks
### user@ubuntu:~/checks$ git status
On branch even-better-feature
### user@ubuntu:~/checks$ ls -l
total 8
-rwxr-xr-x 1 user user 658 Jan 6 09:15 disk_usage.py
-rw-r--r-- 1 user user 57 Jan 6 09:46 free_memory.py

So we see that we're on a clean working tree in the even better feature branch, and that a new free memory py file is in our working tree. Let's now change back to the master branch using git checkout master and then lists the latest two commits there. When we switch to a different branch using git checkout, under the hood, git changes where head is pointing. Thanks to this checkout, head went from pointing to the latest commit in the even better feature branch to the most recent commit of the master branch. The commit from even better feature doesn't show up at all, and the latest snapshot is the second entry we've seen before. 

Remember that when we switch branches, git will also change files in our working directory or working tree to whatever snapshot head is currently pointing at. Let's look at the current contents of our directory.

### user@ubuntu:~$ ls -l
total 4
-rwxr-xr-x 1 user user 658 Jan 6 09:15 disk_usage.py

Free memory py isn't there. This demonstrates that when we switch branches in git, the working directory and commit history will be changed to reflect the snapshot of our project in that branch. 

When we check out a new branch and commit on it, those changes will be added to the history of that branch. Since free memory py was committed on another branch, it doesn't show up in the history or working directory of the master branch. One thing to note after all this back and forth, is that each branch is just a pointer to a specific commit in a series of snapshots. It's very easy to create new branches because there isn't any data that needs to be copied around. When we switch to another branch, we check out a different commit and git updates both head and the contents of our working directory. Head floats around with us. It's like a free spirit. What a head trip. Okay. We've now seen how to create and switch between branches. So what if we want to delete a branch that we don't need anymore? We can do that by using git branch dash d. 

Let's first list the current branches in our repo and then get rid of the new feature branch by calling git branch dash d new-feature. Just like that, our branch was trimmed. 

### user@ubuntu:~$ git branch
even-better-feature
*master
new-feature

### user@ubuntu:~$ git branch -d new-feature
Deleted branch new-feature (was 7d1de19).

We can check with another call to git branch that is not there anymore.

### user@ubuntu:~$ git branch
even-better-feature
*master


If there are changes in the branch we want to delete that haven't been merged back into the master branch, git will let us know with an error.

### user@ubuntu:~$ git branch -d even-better-feature
error: The branch 'even-better-feature" is not fully merged.
Hopefully, git also gives us the command to run if we were sure that we wanted to delete the branch, even if it has unmerged changes. But we won't do that just yet. We actually want to merge those changes back into the repo first. How do we do that? It's all coming up in our next video
