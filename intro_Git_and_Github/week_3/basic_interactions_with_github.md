# Basic Interaction with GitHub


To use it, you first need to create an account on the site. Once you have your account, you're ready to create your brand new repository on GitHub.

We'll start by clicking the Create a repository link on the left. This will take us to the repo creation wizard. The wizard is pretty straightforward. 
The first thing we need to do is give a name for our repo. We'll call this repo health checks. After that comes a description of what the repo will be used for. 
We'll say that'll be used for scripts that check the health of our computers. Then we need to select whether we want the repo to be public or private. 
We'll go with private for now. Finally, the wizard can help us get started with some few initialization files like a README, a gitignore, or license file. 
We'll go with just the README for now, and then create the repo. Yeah. Using the wizard, we created the repo and have a fresh remote repository ready to go. 
Just like magic. Let's get to work. 

First step is to create a local copy of the repository. We'll do that by using the git clone command followed by the URL of the repo. 
GitHub conveniently lets us copy the URL from our repo from the interface so that we don't have to type it.
We're now ready to clone the repo into our computer. We'll do that by calling git clone and paste in the URL we copied. 
To do this, GitHub will ask for our username and password.
```
$ user@ubuntu:~$ git clone https://github.com/redquinoa/health-checks.git
cloning into 'health-checks'...
Username for 
Password for 
```

Just like that, we've downloaded a copy of the remote repository from GitHub onto the local machine. This means that we can perform all the git actions that we've learned up 
till now. Since the repo is called health checks, a directory with that name was automatically created for us and now has the working tree of the Repository in it. 

So let's change that directory and look at the contents. Our repo is basically empty. It only has the README file that GitHub created for us. 
This file is in a special format called markdown.
```
$ user@ubuntu:~$ cd health-checks/


$ user@ubuntu:~/health-checks$ ls -l
total 4
--rw-r--r-- 1 user user 62 Jan 6 14:06 README.md

Let's add a bit more content to it

$ user@ubuntu:~/health-checks$ atom README.md
````
--------README.md--------------------
health-checks

Scripts that checks the health of my computer

This repo will be populated with lots of fancy checks

-------------------------------------

We've changed this file. What do we need to do now? We need to stage the change and committed. We've seen a couple of different ways to do that. 
Let's use our shortcuts to do this in just one command.

```
$ user@ubuntu:~/health-checks$ git commit -a -m "Add one more line to README.md"
[master 807cb50] Add one more line to README.md
1 file changed, 2 insertions(+)
```
Okay. We've modified our README file. But we've seen all this before. We got to remote repository set up on GitHub. 
So let's use it. We can send our changes to that remote repository by using the git push command which will gather all the snapshots we've taken and 
send them to the remote repository.

To push our modified README up to GitHub, we'll just call git push.
```
$ user@ubuntu:~/health-checks$ git push
Username for 
Password for 
```

Once again, we're asked for our password. After that, we see a bunch of messages from git related to the push. When we access our project, 
we see the contents of the README file. So if we check our repository on GitHub, we should see the updated message.

Pretty cool, right? We've taken the local changes on our computer and pushed them out to a remote repository hosted on GitHub. You've probably noticed that we had to 
enter our password both when retrieving the repo and when pushing changes to the repo. There are a couple ways to avoid having to do this. One way is to create an SSH key pair 
and store the public key in our profile so that GitHub recognizes our computer. Another option is to use a credential helper which caches our credentials for a time window 
so that we don't need to enter our password with every interaction. Git already comes with a credential helper baked in. We just need to enable it. We do that by calling 
```
git config - - global credential.helper cache.

$ user@ubuntu:~/health-checks$ git onfig - - global credential.helper cache
```
Now that we've enabled the credential helper, we'll need to enter our credentials once more. After that, they'll be cached for 15 minutes. 
To check this, we can try another git command, git pull which is the command we use to retrieve new changes from the repository. We'll enter our credentials on the first call 
to the command and they'll be cached, so we won't need to enter them again
```
$ user@ubuntu:~/health-checks$ git pull
Username for 
Password for 
```
