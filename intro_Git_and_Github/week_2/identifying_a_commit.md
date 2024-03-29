# 4.0 Identifying a Commit

Let's have a look at the latest log entry in our checks repo.

The commit ID is the 40 character long string after the word commit, you really can't miss it. This long jumble of letters and numbers is actually something called a hash, which 
is calculated using an algorithm called SHA1. Essentially, what this algorithm does is take a bunch of data as input and produce a 40 character string from the data as the output. 
In the case of Git, the input is all information related to the commit, and the 40 character string is the commit ID. Cryptographic algorithms like SHA1 can be really complex, so 
we won't go too deep into what this means. If you're interested, you'll find links to more information in the next reading. Still you might be wondering, why on earth would you 
use a long jumble of letters as an ID for commit, instead of incrementing an integer, like 123, etc? To answer that, let's take a quick look at the reason why Git uses a hash 
instead of a counter, and how that hash is computed. Although SHA1 is a part of the class of cryptographic hash functions, Git doesn't really use these hashes for security. 
Instead, they're used to guarantee the consistency of our repository.

Having consistent data means that we get exactly what we expect. To quote Git's creator, Linus Torvalds, you can verify the data you get back out is the exact same data you put in.
This is really useful in distributed systems like Git because everyone has their own repository and is transmitting their own pieces of data. Computing the hash keeps data 
consistent because it's calculated from all the information that makes up a commit. The commit message, date, author, and the snapshot taken of the working tree. The chance of two
different commits producing the same hash, commonly referred to as a collision, is extremely small. So small, it wouldn't happen by chance. It'd take a lot of processing power to
cause this to happen on purpose. If you use a hash to guarantee consistency, you can't change anything in the Git commit without the SHA1 hash changing too.

The data integrity offered by the commit ID means that if a bad disk or network link corrupt some data in your repository, or worse, if someone intentionally corrupt some data, 
Git can use the hash to spot that corruption. Aha, it will say, the data you've got isn't the data you expected, something went wrong.






### ~/scripts$ git log -2
commit bb9d78272709e9f2bbb (HEAD -> master)
Author: My name <me@example.com>
Date:   Mon Jan 6 07:43:32 2020 - 0800

      Add a gitignore file, ignore .DS_STORE
      

commit bfffffwdfvdczsb9d78272709e9f2bbb 
Author: My name <me@example.com>
Date:   Mon Jan 6 07:37:32 2020 - 0800

How can you use commit IDs to specify a particular commit to work with, like during a rollback? Let's look at the last two entries in our repo using the git log -2 command.
Say we realized that we actually liked the previous name of our script, and so we want to revert this commit where we renamed it. First, let's look at that specific commit using 
git show, which we mentioned in an earlier video.


### ~/scripts$ git show <commit id>
  
We've copied and pasted the commit ID that we wanted to display, and that works. Alternatively, we could provide just the first few characters identifying the commit to the command,
and Git will be smart enough to guess which commit ID starts with those characters, as long as there's only one matching possibility. 

Two characters is not enough, but usually four to eight characters will be plenty.

Okay, now that we've seen how we can identify the commit that we want to revert, let's call the git revert command with this identifier. 

 ### ~/scripts$ git revert 30e70712
  
As usual, this will open an editor where  we should add a reason for the rollback. In this case, we'll say that the previous name was actually better. Hooray for flip-flopping.

As we called out before, when we generate the rollback, Git automatically includes the ID of the commit that we're reverting. This is useful when looking at a repo with a 
complicated history that includes a lot of commits. Now, once we save and exit the commit message, Git will actually perform the rollback and generate a new commit with its own 
ID. See how before the name of our commit the revert command already shows the first eight characters of the commit ID? 

All right, we've managed to revert a commit that wasn't the most recent one. Well done, time travelers. 
