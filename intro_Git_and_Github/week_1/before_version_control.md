# Version Control System
A version control system allows us to keep track of when and who did what changes to our files. Those can be code, configuration, images, or whatever else we need to track.

### $ diff rearrange 1.py rearrange 2.py

We can use the diff command line tool to take two files or even to directories, and show the differences between them in a few formats.

We can see that diff splits the changes in two separate sections. The section that starts with 5c5,6 shows a line in the first file that was replaced by two different lines in the second file. The number at the beginning of this section indicates the line number in the first and second files. The c in between the numbers means that a line was changed. The section that starts with 11a13,15 shows three lines that are new in the second file. The a stands for, you guessed it, added, but that block looks a bit strange doesn't it? It seems like we're adding a return and an if condition but nobody for the if block. What's up with that? 

### $ diff -u validation1.py validation1.py

To understand this better we can use the dash u flag to tell diff to show the differences in another format
This unified format is pretty different from the one that we saw before. It shows the change lines together with some context, using the minus sign to mark lines that were removed, and the plus sign to mark lines that were added. The extra context let's us better know what's going on with the change that we're diffing.

Some examples of this include: meld, KDiff3, or vimdiff.

applying changing
To do this, we typically use a command line like diff-u old_file new_ file > change.diff. As a reminder, the greater than sign redirects the output of the diff command to a file. So with this command, we're generating a file called change.diff with the contents of diff-u command. By using the -u flag, we include more context which helps the person reading the file understand what's going on with the change. The generated file is usually referred to as a diff file or sometimes a patch file. It includes all the changes between the old file and the new one, plus the additional context needed to understand the changes and to apply those changes back to the original file

### $ cat cpu_usage.diff


### $ patch cpu_usage.py < cpu_usage.diff
we told patch to apply the changes that come from cpu_usage.diff to our cpu_usage.py file. We get one single line that says the file was patched, which means that we've successfully applied the changes
