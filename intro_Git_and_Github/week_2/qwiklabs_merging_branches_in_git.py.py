#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Explore repository

# There is a Git repository named food-scripts consisting of a couple of food-related Python scripts.

 $ cd ~/food-scripts

# Now, list the files using the ls command. There are three files named favorite_foods.log, food_count.py, and food_question.py.

# Let's explore each file. Use the cat command to view each file.
# 1. favorite_foods.log: This file consists of a list of food items. You can view it using the following command:

$ cat favorite_foods.log
''' 
pie
burgers
pizza
pie
tacos
fried chicken
spaghetti
rice
cake
broccoli
cake
cereal
salad
avocados
burgers
rice
rice
salad
ice cream
avocados
pie
pizza
fish
fried chicken
rice
strawberries
broccoli
bananas
salad
pizza
tacos
spaghetti
burgers
spaghetti
spaghetti
watermelon
avocados
strawberries
avocados
burgers
spaghetti
salad
pie
fried chicken
rice
fish
fried chicken
ice cream
fried chicken
pizza
salad
avocados
rice
pie
pie
tacos
fish
rice
salad
bananas
burgers
salad
rice
tacos
fried chicken
pizza
bananas
rice
bananas
rice
cereal
pizza
ice cream
strawberries
cereal
fried chicken
rice
burgers
bananas
broccoli
rice
burgers
avocados
tacos
fish
broccoli
fried chicken
pizza
burgers
cake
tacos
pie
burgers
ice cream
broccoli
watermelon
fried chicken
pie
burgers
ice cream
'''

# 2. food_count.py: This script returns a list of each food and the number of times the food appeared in the favorite_foods.log file.

$ ./food_count.py
'''
rice, 12
burgers, 10
fried chicken, 9
pie, 8
salad, 7
pizza, 7
tacos, 6
avocados, 6
ice cream, 5
bananas, 5
broccoli, 5
spaghetti, 5
fish, 4
strawberries, 3
cereal, 3
cake, 3
'''

# 3. food_question.py: This prints a list of foods and prompts the user to enter one of those foods as their favorite. It then returns an answer of how many others in the 
# list like that same food.

$ ./food_question.py
'''
Traceback (most recent call last):
  File "./food_question.py", line 10, in <module>
    if item not in counter:
NameError: name 'item' is not defined
'''

# Uh oh , this gives us an error. One of your colleagues reports that this script was working fine until the most recent commit. We'll be fixing this error later during the lab.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Understanding the repository
# Let's use the following Git operations to understand the workflow of the repository:

# git status
# git log
# git branch

# Git status: This displays paths that have differences between the index file and the current HEAD commit; paths that have differences between the working tree and the index 
# file; and paths in the working tree that are not tracked by Git. You can view the status of the working tree using the command: [git status]

$ git status
#You can now view the status of the working tree.

'''On branch master
nothing to commit, working tree clean'''

#Git log: This lists the commits done in the repository in reverse chronological order; that is, the most recent commits show up first. This command lists each commit with its 
# SHA-1 checksum, the author's name and email, date, and the commit message.

$ git log
'''
commit 21cf376832fa6eace35c0bf9e4bae4a3400452e9
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:09:39 2020 +0530

    Rename item variable to food_item.

commit b8d00e33237b24ea1480c363edd972cf4b49eedf
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:08:35 2020 +0530

    Added file food_question.py that returns how many others in the list like that same food.

commit 8d5a3189b88d273ef08286e5074b5e38d616da21
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:07:15 2020 +0530

    Added file food_count.py that returns a list of each food and the number of times each food appears in favorite_foods.log file.

commit 0a202e03e0356d2b5c323e51905d3d06e5e2d0ed
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:06:21 2020 +0530

'''


# Git branch: Branches are a part of the everyday development process on the master branch. Git branches effectively function as a pointer to a snapshot of your changes. When 
# you want to add a new feature or fix a bug, no matter how big or small, you spawn a new branch to encapsulate your changes. This makes it difficult for unstable code to get 
# merged into the main codebase
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Configure Git

# Before we move forward with the lab, let's configure Git. Git uses a username to associate commits with an identity. It does this by using the git config command. Set the Git 
# username with the following command:

$ git config user.name "Name"


# Replace Name with your name. Any future commits you push to GitHub from the command line will now be represented by this name. You can even use git config to change the name 
# associated with your Git commits. This will only affect future commits and won't change the name used for past commits.


# Let's set your email address to associate them with your Git commits.


$ git config user.email "user@example.com"


# Replace user@example.com with your email-id. Any future commits you now push to GitHub will be associated with this email address. You can also use git config to change the 
# user email associated with your Git commits

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Add a new feature

# In this section, we'll be modifying the repository to add a new feature, without affecting the current iteration. This new feature is designed to improve the food count (from 
# the file food_count.py) output. So, create a branch named improve-output using the following command:

$ git branch improve-output

# Move to the improve-output branch from the master branch.

$ git checkout improve-output
Switched to branch 'improve-output'

# Here, you can modify the script file without disturbing the existing code. Once modified and tested, you can update the master branch with a working code.
# Now, open food_count.py in the nano editor using the following command:
  
$ nano food_count.py  

# Add the line below before printing for loop in the food_count.py script:
#!/usr/bin/env python3

# Dictionary to keep track of food likes
counter = {}

# Open up the favorite foods log and add it to the dictionary
with open("favorite_foods.log", "r") as f:
    for i in f:
        i = i[:-1]
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

# Sorts the liked foods in descending order
sort_foods = sorted(counter.items(), key = lambda x : x[1], reverse = True)

# Prints out the liked foods
for i in range(len(sort_foods)):
    print("Favourite foods, from most popular to least popular")
    print("{}, {}".format(sort_foods[i][0], sort_foods[i][1]))

# Save the file by pressing Ctrl-o, the Enter key, and Ctrl-x. Then run the script food_count.py again to see the output:

$ ./food_count.py
"""
Favourite foods, from most popular to least popular
rice, 12
burgers, 10
fried chicken, 9
pie, 8
pizza, 7
salad, 7
avocados, 6
tacos, 6
ice cream, 5
spaghetti, 5
broccoli, 5
bananas, 5
fish, 4
cereal, 3
cake, 3
strawberries, 3
watermelon, 2
"""

# After running the food_count.py script successfully, commit the changes from the improve-output branch by adding this script to the staging area using the following command:

$ git add food_count.py

# Now, commit the changes you've done in the improve-output branch.

$ git commit -m "Adding a line in the output describing the utility of food_count.py script"
"""
[improve-output b7c46f4] Adding a line in the output describing the utility of food_count.py script
 1 file changed, 2 insertions(+), 1 deletion(-)
"""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Fix the script
# In this section, we'll fix the script food_question.py, which displayed an error when executing it. You can run the file again to view the error.

$ ./food_question.py
'''
Traceback (most recent call last):
  File "./food_question.py", line 10, in <module>
    if item not in counter:
NameError: name 'item' is not defined
'''
# This script gives us the error: "NameError: name 'item' is not defined" but your colleague says that the file was running fine before the most recent commit they did.
# In this case, we'll revert back the previous commit.

# For this, check the git log history so that you can revert back to the commit where it was working fine.

$ git log
'''
commit b7c46f422999be5d113374d6c78c31e08e8217d8
Author: Akolab <alex_cooper@gmail.com>
Date:   Wed Jan 12 02:39:22 2022 +0000

    Adding a line in the output describing the utility of food_count.py script

commit 21cf376832fa6eace35c0bf9e4bae4a3400452e9
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:09:39 2020 +0530

    Rename item variable to food_item.

commit b8d00e33237b24ea1480c363edd972cf4b49eedf
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:08:35 2020 +0530

    Added file food_question.py that returns how many others in the list like that same food.

commit 8d5a3189b88d273ef08286e5074b5e38d616da21
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:07:15 2020 +0530

    Added file food_count.py that returns a list of each food and the number of times each food appears in favorite_foods.log file.

commit 0a202e03e0356d2b5c323e51905d3d06e5e2d0ed
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:06:21 2020 +0530

    Added file favorite_foods.log that contains list of foods.
'''
# Here, you'll see the commits in reverse chronological order and find the commit having "Rename item variable to food_item" as a commit message. 
# Make sure to note the commit ID for this particular commit.

# To revert, use the following command:

$ git revert [commit-ID]

# Replace [commit-ID] with the commit ID you noted earlier.

# This creates a new commit again. You can continue with the default commit message on the screen or add your own commit message.

# Then continue by clicking Ctrl-o, the Enter key, and Ctrl-x.

# Now, run food_question.py again and verify that it's working as intended.

$ ./food_question.py
'''
Select your favorite food below:
cereal
tacos
bananas
broccoli
fried chicken
avocados
spaghetti
watermelon
cake
rice
strawberries
burgers
salad
fish
pie
pizza
ice cream

'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Merge operation

# Before merging the branch improve-output, switch to the master branch from the current branch improve-output branch using the command below:

$ git checkout master
'''
Switched to branch 'master'
'''
# Merge the branch improve-output into the master branch.

$ git merge improve-output
'''
Updating 21cf376..34f5370
Fast-forward
 food_count.py    | 3 ++-
 food_question.py | 2 +-
 2 files changed, 3 insertions(+), 2 deletions(-)
'''

# Now, all your changes made in the improve-output branch are on the master branch.

./food_question.py
'''
Select your favorite food below:
burgers
pie
fish
spaghetti
cereal
avocados
fried chicken
ice cream
broccoli
salad
bananas
rice
watermelon
strawberries
pizza
cake
tacos
Which of the foods above is your favorite? cake
3 of your friends like cake as well!
'''
# To get the status from the master branch, use the command below:

$ git status
'''
On branch master
nothing to commit, working tree clean
'''
# To track the git commit logs, use the following command:

git log
'''

commit 34f537019520d6dcbf23c7e08c9bd568de6b5165
Author: Akolab <alex_cooper@gmail.com>
Date:   Wed Jan 12 02:47:54 2022 +0000

    Revert "Rename item variable to food_item."

    This reverts commit 21cf376832fa6eace35c0bf9e4bae4a3400452e9.

commit 33ffab316d44ee94f55becb629135fcab50d8c9d
Author: Akolab <alex_cooper@gmail.com>
Date:   Wed Jan 12 02:46:24 2022 +0000

    Revert "Adding a line in the output describing the utility of food_count.py script"

    This reverts commit f49440c9d4ceb2a47eec95e311dfd3ca4a59c415.

commit f49440c9d4ceb2a47eec95e311dfd3ca4a59c415
Author: Akolab <alex_cooper@gmail.com>
Date:   Wed Jan 12 02:41:51 2022 +0000

    Revert "Adding a line in the output describing the utility of food_count.py script"
    fixed the scripted

    This reverts commit b7c46f422999be5d113374d6c78c31e08e8217d8.

commit b7c46f422999be5d113374d6c78c31e08e8217d8
Author: Akolab <alex_cooper@gmail.com>
Date:   Wed Jan 12 02:39:22 2022 +0000

    Adding a line in the output describing the utility of food_count.py script

commit 21cf376832fa6eace35c0bf9e4bae4a3400452e9
Author: Alex Cooper <alex_cooper@gmail.com>
Date:   Wed Jan 8 14:09:39 2020 +0530

    Rename item variable to food_item.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##
