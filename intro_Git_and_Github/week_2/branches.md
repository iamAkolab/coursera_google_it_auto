# Branches 

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
