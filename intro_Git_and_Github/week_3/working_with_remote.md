# Intro to Module 3: Working with Remotes

 In this module, we'll learn a load of new things related to GitHub and remote repositories. We'll first talk about what GitHub is and why it matters, and 
 then we'll dive into how to work with GitHub and other remote repositories. Being able to use remote repositories allows us to effectively collaborate with others. 
 
 Our collaborators can be sitting in the same office as we are or they can be thousands of miles away on a different continent working at a different time of day. 
 Using a version control system like Git lets us incorporate the work of different people no matter where they are or when they're working. 
 
 I've personally had a bunch of interesting experiences collaborating through a version control system. One that stands out was a debugging session a friend and 
 I had while at work. I was working on some tricky code and I couldn't figure out the best way to implement a function. I was stuck and ready to give up completely. 
 My colleague suggested that I work on another piece of the file further down while he figured out the optimal solution for the code that I was having trouble with. 
 This was a super seamless experience and was only possible because of a VCS, and the superpower of teamwork of course. 
 
 By the end of the module you'll be able to collaborate with friends and colleagues just like I did


# What is Remotes

When we clone the newly created GitHub repository, we had our local Git Repo interact with a remote repository. 
Remote repositories are a big part of the distributed nature of Git collaboration. It let lots of developers contribute to a project from their own workstations making changes to local copies of the project independently of one another. When they need to share their changes, they can issue git commands to pull code from a remote repository or push code into one. There are a bunch of ways to host remote repositories.

As we called out, there is many internet-based Git hosting providers like GitHub, BitBucket or GitLab which offer similar services. We can also set up a Git server on our own network to host private repositories. A locally hosted Git server can run on almost any platform including Linux, mac OS, or Windows. This has benefits like increased privacy, control, and customization. 

To understand remote repositories, and Git's distributed nature a bit better, imagine you're working together with some friends to design a computer game, each of you has a different portion of the game you're responsible for. 

One person is designing the levels, another the characters while others are writing the code for the graphics, physics, and gameplay. All these areas will have to come together into a single place for the final product. Although your friends might work on their parts by themselves, from time to time, everyone needs to send out progress updates to let each other know what they've been working on. You will then need to combine their work into your own portion of the project to make sure it's all compatible. 

Using Git to manage a project helps us collaborate successfully. Everyone will develop their piece of the project independently in their own local repositories maybe even using separate branches. Occasionally they'll push finished code into a central remote repository where others can pull it and incorporate it into their new developments. So how does this work? Alongside the local development branches like master, Git keeps copies of the commits that have been submitted to the remote repository and separate branches. 

If someone has updated a repository since the last time you synchronize your local copy, Git will tell you that it's time to do an update. If you have your own local changes when you pull down the code from the remote repo, you might need to fix merge conflicts before you can push your own changes. In this way Git let's multiple people work on the same project at the same time. When pulling new code it will merge the changes automatically if possible or will tell us to manually perform the integrating if there are conflicts. 

So when working with remotes the workflow for making changes has some extra steps. Will still modify stage and commit our local changes. After committing, we'll fetch any new changes from the remote repo manually merge if necessary and only then will push our changes to the remote repo. Git supports a variety of ways to connect to a remote repository. Some of the most common are using the HTTP, HTTPS and SSH protocols and their corresponding URLs. HTTP is generally used to allow read only access to a repository. 

In other words, it lets people clone the contents of your repo without letting them push new contents to it. Conversely HTTPS and SSH, both provide methods of authenticating users so you can control who gets permission to push. 

The distributed nature of the work means that there are no limits to how many people can push code into a repository. It's a good idea to control who can push codes to repos and to make sure you give access only to people you trust. Web services like GitHub, offer a bunch of different mechanisms to control access to Repositories. Some of these are available to the general public while others are only available to enterprise users. By now you have an idea of what a remote repository is and how it interacts with local Git repositories.



# Working with Remotes

When we call a git clone to get a local copy of a remote repository, Git sets up that remote repository with the default origin name. We can look at the configuration for that remote by running git remote -v in the directory of the repo.

$ user@ubuntu:~$ cd health-checks/
$ user@ubuntu:~/health-checks$ git remote -v

origin https://github.com/redquionoa/health-checks.git (fetch)
origin https://github.com/redquionoa/health-checks.git (push)

Here we see the URLs associated with the origin remote. There are two URLs. One will be used to fetch data from the remote repository, and the other one to push data to that remote repo.

They'll usually point at the same place. But in some cases, you can have the fetch URL use HTTP for read only access, and the push URL use HTTPS or SSH for access control. This is fine as long as the contents of the repo that you read when fetching are the same that you write to in pushing. Remote repositories have a name assigned to them, by default, the assigned name is origin. This lets us track more than one remote in the same Git directory.

While this is not the typical usage, it can be useful when collaborating with different teams on projects that are related to each other. We won't look at how to do that here, but we'll include a link for more information in the next reading. If we want to get even more information about our remote, we can call git remote show origin.

$ user@ubuntu:~/health-checks$ git remote show origin
. remote origin
Fetch URL: https://github.com/redquionoa/health-checks.git 
Push URL: https://github.com/redquionoa/health-checks.git 
HEAD branch: master
Remote branch: master tracked
Local branch configured for 'git pull': master merges with remote master
Local ref configured for 'git push': master pushes to master (up to date)


There's a ton of information here, and we don't need all of it right now. We can see the fetch and push URLs that we saw before, and the local and remote branches too.
For now we only have a master branch that exists locally and remotely. So the information here seems a bit repetitive.

Once you start having more branches, especially different branches in the local and remote repo, this information starts becoming more complex.

So what are these remote branches that we're talking about anyways?

Whenever we're operating with remotes, Git uses remote branches to keep copies of the data that's stored in the remote repository. We could have a look at the remote branches that our Git repo is currently tracking by running git branch -r.

$ user@ubuntu:~/health-checks$ git branch -r
origin/HEAD -> origin/master
origin/master

These branches are read only. We can look at the commit history, like we would with local branches, but we can't make any changes to them directly. To modify their contents, we'll have to go through the workflow we called out before.

First, we pull any new changes to our local branch, then merge them with our changes and push our changes to the repo. Remember how we've been using git status to check the status of our changes? We can also use git status to check the status of our changes in remote branches as well.

$ user@ubuntu:~/health-checks$ git status

Now that we're working with a remote repository, git status gives us additional information. It tells us that our branch is up to date with the origin/master branch, which means that the master branch in the remote repository called origin, has the same commits as our local master branch.
