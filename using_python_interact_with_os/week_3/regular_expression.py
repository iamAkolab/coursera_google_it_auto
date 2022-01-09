#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Intro to Module 3: Regular Expressions

# With regular expressions, we'll be able to find and operate on text in a more flexible way than we have up until this point. This is a complex subject
# Regex is a search query that matches the regular expression pattern you've specified.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What are regular expressions?

# A regular expression, also known as regex or regexp, is essentially a search query for text that's expressed by string pattern. When you run a search against a particular piece 
# of text, anything that matches a regular expression pattern you specified, is returned as a result of the search. Regular expressions let you answer the questions like 

# what are all the four-letter words in a file? Or 
# how many different error types are there in this error log? 

# In other words, regular expressions allow us to search a text for strings matching a specific pattern. Knowing about regular expressions can be useful for anyone who needs to 
# perform text processing. For example, if I have a file that lists NFS mounts and options and I want to pull only the server name, I can write a regular expression that strips 
# each line of the excess data and returns only a list of the information I need. Regular expressions are a pretty big topic in IT. In this course will end to cover the most 
# important parts, but we won't go through them all. For your scripts basic regexs will usually be enough to get you started, and they'll enhance your programs ability to process 
# text. With time and practice, you'll pick up even more advanced techniques.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Why use regular expressions?

#  At this point, you might be wondering why do I need more processing power than just looking for strings in a text which I already know how to do in Python? The answer lies in 
# the power and flexibility of regular expressions. For example, let's say we have log entries with a typical log line format like this one.

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1 : index+6])

# We want to extract the process identifier from this line, which is a number between the square brackets 12345. There's a lot of extra text in this log line that we don't need,
# like the date, the computer name and other info. We could extract the process ID by using the index method to find the first square bracket in the string. Remember that when 
# accessing strings, the index of the character is the position of that character in the string starting from 0. In this example, the index of the first square bracket would be 
# 39. If we don't want to capture the square brackets, we will start at the next version and include five more characters after that. Let's give it a go
# Hm, although we get the text that we wanted, we might hit a few bumps down the road. Can you spot them? One problem is we don't know for sure how long the process ID string 
# will be in all cases. In this example, we can see that it's five characters long. But that may change in the future if the computers restarted, or the number of processes 
# increases. This could also break if for any reason, the line includes another square bracket before the process ID. So it's a solution but it's a very brittle one

# Instead, we could use a regular expression to extract the process ID in a more robust fashion. For that, we're going to import the RE module, which lets us use the search 
# function to find regular expressions inside strings.

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Great, this regular expression will work no matter where our process ID shows up or how long or short the line is. As long as there's a single sequence of numbers in the 
# string marked by square brackets, this regex will extract those numbers for us. If the regular expressions stored in the regex variable looks like gibberish at this point, 
# don't worry, that's expected. We'll explore syntax and how we use these expressions in upcoming videos. At this point, the key takeaway is that regular expressions are both 
# powerful and flexible tools. By the end of this module, you'll be able to read and unpack statements like the one in this example, we're off to a strong start. 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Basic Matching with grep

# We can also use regular expressions with a bunch of command line tools. Grep is an especially easy to use yet extremely powerful tool for applying regexes
# The simplest of all matchings is just to search to see if the string is present. Remember, that grep works by printing out any line that matches the query that we pass it. 
# So for a simplest query of passing a plain old string, grep will print any lines containing that string in the file that we give it. Let's try this out using grep to find 
# words inside the /usr/share/dict/words file, which is a file that some spell-checking programs use to verify if the word exists or not. This file contains one word per line. 
# We'll start by looking at words that contain the particle thon. Let's see what happens

user@ubuntu:~$ grep thon /usr/share/dict/words
'''
Marathon
Python
python's
telethon
thongs
thong's
'''

# So when we call grep with thon as a pattern to match on and we pass our list of words as a file, we see that it matches with a bunch of different words. These words, all 
# contain the string thon somewhere inside of them, which is why they appear in our results. We also see that the output is highlighted for us, showing us the matching part 
# of the line in a different color. This added visual indicator is something that grep does for us so that we can easily see where the match occurred. 


# It's worth calling out that the string we're passing in grep is case sensitive. So it needs to be matched exactly. If we use uppercase letters, they'll only be matched by 
# uppercase letters. If we wanted to match a string regardless of case, we will have to pass the -i parameter to the grep command, like this.

user@ubuntu:~$ grep -i python /usr/share/dict/words
'''
Python
python's
'''
  
# Nice. So we now know that any basic string is already a regular expression which will match a line that contains that string. 

# To get the most out of regular expressions, we need to learn more of their syntax, which can be as complicated as it is powerful. 
# In particular, we have to know the reserved characters that give extra meaning to the patterns that we create. It's these characters that allow us to do more advanced matching
# than just checking for a literal string. 

# For example, a dot matches any character. This means that if we include a dot in our expression, that dot is a wildcard that can be replaced by any other character in the 
# results. Let's check out an example of this
  
user@ubuntu:~$ grep l.rts /usr/share/dict/words
'''
alerts
blurts
flirts
'''

# This pattern matches three different words; alerts, blurts, and flirts. Check out how for each of those words, the dot in our pattern was substituted by different letter. 
# Are you starting to see the power of regular expressions? With them, we can find portions of texts that match a given pattern even when the pattern isn't a whole word. 
# We could use this, for example, to look for entries in a log file that match a certain format or to find rows in a CSV file that share the same characteristics even if they 
# are not exactly the same.

######################################################################################################
# Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?

user@ubuntu:~$ grep s.ing /usr/file.txt
# Nice work! In regex, a dot is a wildcard, so it can represent any character. This command will print both “sting” and “sling”, if they are in the file.
#####################################################################################################

# Other easy examples of special characters that we can use in a irregular expressions are the caret, or circumflex and the dollar sign anchor characters. These tell us where in
# the line the regex should match from. The circumflex indicates the beginning and the dollar sign indicates the end of the line. For example, to look for all the words that 
# start with a string fruit, we would write grep circumflex fruit in our file.

user@ubuntu:~$ grep ^fruits /usr/share/dict/words
'''
fruit
fruits's
fruitcakes
fruited
fruition
fruitless
'''

# Let's check out one more example. We'll use grep to find all the words that end with cat by writing grep cat dollar sign into our file.
user@ubuntu:~$ grep cat$ /usr/share/dict/words
'''
Muscat
Bobcat
Copycat
pussycat
tomcat
wildcat
'''

# One thing to remember is that the circumflex and the dollar sign specifically match the start and end of the line, not a string. Take a log file for example, where each line 
# contains a lot of different words. We can use a circumflex to check if a line begins with a pattern or use a dollar sign and check if it ends with a pattern, but our patterns
# will match only if the line fits that criteria, not the contained words.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
