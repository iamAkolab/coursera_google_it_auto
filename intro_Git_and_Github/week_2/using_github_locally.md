# 1.0 Intro to Module 2: Using Git Locally

We'll start by learning some handy shortcuts and looking into how we can get more info out of our version control system. Then we'll experience the true power of Git by seeing how
we can undo some of our changes. The ability to revert previous changes is one of the most useful aspects of version control systems. Depending on what needs to be undone, there's 
a bunch of different techniques that we can use in Git. We can discard the changes made to a file, fix a commit that was incorrect and even roll back our project to an older 
snapshot. We'll look into all these techniques and dive into when to use each of them. Finally, we'll check out yet another important concept, Branches. We can use branches to 
work on an experimental feature without affecting the main code of our project. Support separate versions of a program that can't be merged together and much more. We'll dive 
into what branches are, when and how to use them and how to deal with merge conflicts.

# 2.0 Skipping the Staging Area
When we covered the basic Git workflow, we called out that the process is usually to make changes, stage them, and then commit them. The separate step between staging and 
committing allows us to stage several changes in one commit.
The -a flag lets us add and commit in the same step.  At first, you might think that git commit dash a is just a shortcut for git add followed by git commit but that's not exactly true. Git commit -a doesn't work on new files because those are untracked. Instead, git commit -a is a shortcut to stage any changes to tracked files and commit them in one step. If the modified file has never been committed to the repo, we'll still need to use git add to track it first.

### $ cd scripts$

### $ atom all_checks.py

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


### $ git commit -a -m "Check_reboot from main, exit with 1 on error"
[master fdb0987f] Call back check_reboot from main, exit with 1 on error
1 file changed, 4 insertions(+), 1 deletion(-)

These shortcuts are useful when making small changes that we know we'll want to commit directly without keeping them in the staging area and having to write long and complex descriptions. Keep in mind that when you use the -m shortcut, you can only write short messages and can't use the best practices regarding commit descriptions that we talked about earlier. So it's best reserved for truly small changes that don't require extra context or explanation, short and sweet. Heads up, when you use the -a shortcut, you skip the staging area. Meaning, you can't add any other changes before creating the commit. So you need to be sure that you've already included everything you want to include in that commit. In the end, using a shortcut like -a is just like using the regular commit workflow. The commit will show up in the log along with the message just as usual

### $ log

So let's clarify. Git uses the head alias to represent the currently checked out snapshot of your project. This lets you know what the contents of your working directory should be. In this case, the current snapshot is the latest commit in the project. We'll soon learn about branches. In that case, head can be a commit in a different branch of the project. We can even use git to go back in time and have head representing old commit from before the latest changes were applied. In all cases, head is used to indicate what the currently checked out snapshot is. This is how git marks your place in the project. Think about it as a bookmark that you can use to keep track of where you are. Even if you have multiple books to read, the bookmark allows you to pick up right where you left off. When you run git commands like diff, branch, or status, git will use the head bookmark as a basis for whatever operation it's performing. We'll see Head used when we learn how to undo things and perform rollbacks.


# 3.0 Getting More Information About Our Changes
By default, it prints the commit message, the author, and the date of the change. This is useful, but if we're combing through a history of changes in a repo to try and find what caused the latest outage, we'll probably also need to look at the actual lines that changed in each commit. To do this with git log, we can use the -p flag. The p comes from patch, because using this flag gives us the patch that was created. Let's try it out.

### $ git log -p

The format is equivalent to the diff-u output that we saw on an earlier video.
It shows added lines with plusses and remove lines with dashes. Because the amount of text is now longer than what fits on your screen, Git automatically uses a paging tool that allows us to scroll using page up, page down, and the arrow keys.
Using this option, we can quickly see what changes were made to the files in our repository. This can be especially useful if we're trying to track down a change that recently broke our tools. If we don't want to scroll down until we find the commit that we're actually interested in, another option is to use the git show command. This command takes a commit ID as a parameter, and will display the information about the commit and the associated patch

Let's check this out by first listing the current commits in the repo and then calling git show for the second commit in the list. First, I'm going to exit out by pressing q

### $ git log

We've shown how we can use git log for listing commits, and git log -p for showing the associated patches. Another interesting flag for git log is the --stat flag. This will cause git log to show some stats about the changes in the commit, like which files were changed and how many lines were added or removed. Let's try it with our repo.

### $ git log --stat

Now, what about changes that haven't been committed yet? Until now, whenever we've made changes to our files, we've either added them to the staging area with git add and committed them with git commit, or committed them directly using git commit -a. This works fine, but it means we have to know exactly which changes we've made.

Now, what about changes that haven't been committed yet? Until now, whenever we've made changes to our files, we've either added them to the staging area with git add and committed them with git commit, or committed them directly using git commit -a. This works fine, but it means we have to know exactly which changes we've made.
Let's make a new change to our script and then try this command out. We'll add another message to the user to say that everything is okay when the check is successful and then exit with 0 instead of 1.

Okay, we've made the change. Let's now save it and check out what git diff shows us.

### $ git diff

Again, this format is equivalent to the diff -u output that we saw in an earlier video. In this case, we see that the only change is the extra lines that we've added. If our change was bigger and included several files, we could pass a file by parameter to see the differences relevant to that specific file instead of all the files at the same time. 

Something else we can do to review changes before adding them is to use the -p flag with the git add command. When we use this flag, git will show us the change being added and ask us if we want to stage it or not. This way we can detect if there's any changes that we don't want to commit. Let's try that one out.


### $ git add -p

We've staged our change and it's now ready to be committed.

If we call git diff again, it won't show any differences, since git diff shows only unstaged changes by default. Instead, we can call git diff -- staged to see the changes that are staged but not committed. With this command, we can see the actual stage changes before we call git commit.

### $ git comiit -m 'Add a message when everything is ok'

# 4.0 Deleting and Renaming Files
Let's say that you've decided to clean up some old scripts and want to remove them from your repository Or you've done some refactoring, which makes that particular file, obsolete. You can remove files from your repository with the git rm command, which will stop the file from being tracked by git and remove it from the git directory.

File removals go through the same general workflow that we've seen. So you'll need to write a commit message as to why you've deleted them. Let's try this out in our checks repository that contains a file we decided we actually don't want. Well first look the contents of the directory with ls, then delete the file with git rm, then check the contents with ls again, and finally check the status with git status.

### $ cd checks/

### ~/checks$ ls -l
total 8

### ~/checks $ git rm process.py
rm 'process.py'

### ~/checks $ ls -l

### ~/checks $ git commit -m 'Delete unneeded processes file'

hese are all lines in the file that are no longer there. And it states the file itself was deleted. What if you have a file that isn't accurately named? This can happen. For example, if you start writing a script that you thought would only do one thing, and then expands to cover more use cases. Or conversely, if you named your script thinking that it would be very generic, but it ends up being more specific. You can use the git mv command to rename files in the repository. Let's rename our existing script to check_free_space.py and check what git status has to say about that.

### ~/checks $ git mv disk_usage.py check_free_space.py
### ~/checks $ git status

The status shows us that the file was renamed and clearly displays the old and new names. As with the previous example, the change is staged, but not committed. Let's commit it by calling git commit once again

### ~/checks $ git commit -m 'New name for disk_usage.py'

The git mv command works in a similar way to the mv command on Linux and so can be used for both moving and renaming. If our repository included more directories in it, we can use the same git mv command to move files between directories.

As you can probably tell from our examples, the output of git status is a super useful tool to help us know what's up with our files. It shows us which files have tracked or untracked changes, and which files were added, modified, deleted or renamed. It's important that the output of these commands stays relevant to what we're doing. If we have a long list of untracked files, we might lose an important change in the noise. If there are files that get automatically generated by our scripts, or our operating system generates artifacts that we don't want in our repo, we'll want to ignore them so that they don't add noise to the output of git status. To do this, we can use the gitignore file.

Inside this file, we'll specify rules to tell git which files to skip for the current repo. For example, if we're working on an OSX computer, we'll probably want to ignore the dot DS store file, which is automatically generated by the operating system. To do this, we'll create a .gitignore file containing the name of this file.

### ~/checks $ echo .DS_STORE > .gitignore
### ~/checks $ ls -la

Remember that the dot prefix in a Unix-like file system indicates that the file or directory is hidden and won't show up when you do the normal directory listing. That's why we have to use ls-la to see all files.
We've added a gitignore file to our repo but we haven't committed it yet. This file needs to get tracked just like the rest of the files in the repo. Let's add it now.

### ~/checks $ git add .gitignore
### ~/checks $ git commit -m 'Add a gitignore file, ignoring .DS_STORE files'




