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
