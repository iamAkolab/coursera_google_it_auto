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

import re

log
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##
