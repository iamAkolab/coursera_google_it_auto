 Any Git project will consist of three sections. 
 
 The Git directory, the working tree, and the staging area. 
 The Git directory contains the history of all the files and changes. 
 The working tree contains the current state of the project, including any changes that we've made. And the staging area contains the changes 
 that have been marked to be included in the next commit.
 
 This can still be confusing. So it might be helpful to think about Git as representing your project. 
 Which is the code and associated files and a series of snapshots. Each time you make a commit, 
 Git records a new snapshot of the state of your project at that moment. 
 It's a picture of exactly how all these files looked at a certain moment in time. 
 Combined, these snapshots make up the history of your project, and it's information that gets stored in the Git directory.
 
 When we operate with Git, our files can be either tracked or untracked. 
 Tracked files are part of the snapshots, while untracked files aren't a part of snapshots yet. This is the usual case for new files. 
 Each track file can be in one of three main states, modified, staged or committed. Let's look at what each of these mean.
 So, the next step is to stage those changes. When we do this, our modified files become stage files. 
 In other words, the changes to those files are ready to be committed to the project. All files that are staged will be part of the next snapshot we take. 
 And finally, when a file gets committed, the changes made to it are safely stored in a snapshot in the Git directory. 
 This means that typically a file tracked by Git, will first be modified when we change it in any way. 
 Then it becomes staged when we mark those changes for tracking. And finally it will get committed when we store those changes in the VCS
 
 $ cd checks
 $ ls -l
 $ git status
 $ atom disk_usage.py
 $ git status
 
 $ git add disk_usage
 $ git status
 
 $ git commit -m 'Add periods to the end of sentences'
