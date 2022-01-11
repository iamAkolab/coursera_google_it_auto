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

Right now we want to switch to a new branch. To do that, we'll need to use the git checkout command. We saw earlier how we can use git checkout to restore a modified file back to the latest commit. Checking out branches is similar in that, the working tree is updated to match the selected branch including both the files and the git history. It might help to remember that we use git checkout to check out the latest snapshot for both files and for branches. All right. Let's switch to our new feature branch by calling git checkout new feature, and then listing our branches once again.

Before we were working on the master branch but now that we've changed to our new branch, the star has moved to new feature. Creating a branch and switching to it immediately is a pretty common task. So common that git gives us a useful shortcut to create a new branch and to switch to it in a single command. We can use the git checkout -b new branch to do this. Take a look.
