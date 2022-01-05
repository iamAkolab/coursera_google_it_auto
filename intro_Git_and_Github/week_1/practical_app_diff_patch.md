Imagine this, a colleague is asking our help with fixing a script named disk_usage.py. 

The goal of the script is to check how much disk space is currently used, and print an error if it's too little space for normal operation. 
But the script is currently broken because it has a few bugs. We’ll help our colleague fix those  bugs to demonstrate how to use diff and patch. 
Before we change anything, let’s make a couple copies of the script. We'll add _original to one copy, which we’ll 
keep unmodified and use for comparison and _fixed to the other copy, which we’ll use to repair our fix.

#### $ cp disk_uage.py disk_usage_original.py
#### $ cp disk_uage.py disk_usage_fixed.py

Okay, now that we have our copies, we'll edit the _fixed version and actually fix it.

then create a diff file

### $ diff -u disk_usage_original.py sisk_usage_fixed.py > disk_usage.diff
### $ cat disk_usage.diff

Run  
### $ patch disk_usage.py < disk_usage.diff.
