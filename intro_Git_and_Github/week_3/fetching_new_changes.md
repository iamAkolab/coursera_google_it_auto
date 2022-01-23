# Fetching New Changes

While we were learning about remotes, our colleague Blue Kale added some files to our repo. We could always use the GitHub website to browse the changes that were submitted. 
But we want to learn how to do it by interacting through the command line because you might need to do it this way at your job, and it'll work the same no matter which 
platform you use to interact with Git. So first, let's look at the output of the Git remote show origin command.

$ user@ubuntu:~$ cd health-checks/

$ user@ubuntu:~/health-checks$ git remote show origin
. remote origin
Fetch URL: https://github.com/redquionoa/health-checks.git 
Push URL: https://github.com/redquionoa/health-checks.git 
HEAD branch: master
Remote branch: master tracked
Local branch configured for 'git pull': master merges with remote master
Local ref configured for 'git push': master pushes to master (local out of date)

Check out how it says that the local branches out of date. This happens when there were commits done to the repo that aren't yet reflected locally. Git doesn't keep remote and 
local branches in sync automatically, it waits until we execute commands to move data around when we're ready. To sync the data, we use the git fetch command. 
This command copies the commits done in the remote repository to the remote branches, so we can see what other people have committed. Let's call it now and see what happens.

$ user@ubuntu:~/health-checks$ git fetch

Fetched content is downloaded to the remote branches on our repository. So it's not automatically mirrored to our local branches. We can run git checkout on these branches 
to see the working tree, and we can run git log to see the commit history. Let's look at the current commits in the remote repo by running git log origin/master.

$ user@ubuntu:~/health-checks$ git log origin/master


Looking at this output, we can see that the remote origin/branch is pointing to the latest commit. While the local master branch is pointing to the previous commit we made 
earlier on. Let's see what happens if we run git status now. 

$ user@ubuntu:~/health-checks$ git status

Git status helpfully tells us that there's a commit that we don't have in our branch. It does this by letting  us know our branches behind their remote origin/master branch. 
If we want to integrate the branches into our master branch, we can perform a merge operation, which merges the origin/master branch into our local master branch. 
To do that, we'll call git merge origin/master.

$ user@ubuntu:~/health-checks$ git merge origin/master
Updating 807cv50..b62cd2e
Fast-forward
all_checks.py | 18 +++++++++++++++++++++
disk_usage.py | 24 +++++++++++++++++++++
2 files changed, 42 insertions(+)
create mode 1000755 all_checks.py
create mode 100644 disk_usage.py


Great. We've merged the changes of the master branch of the remote repository into our local branch. See how Git tells us that the code was integrated using fast-forward? 
It also shows that two files were added, all checks and disk_usage.py. If we look at the log output on our branch now, we should see the new commit. 


$ user@ubuntu:~/health-checks$ git log

We see that now our master branch is up to date with the remote origin/master branch. With that, we've updated our branch to the latest changes. We can use git fetch like this to review the 
changes that happen in the remote repository. If we're happy with them, we can use git merge to integrate them into the local branch. Fetching commits from a remote 
repository and merging them into your local repository is such a common operation in Git that there's a handy command to let us do it all in one action. 
