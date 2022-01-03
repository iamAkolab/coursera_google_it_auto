#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

# As we called it out before, we use the re module to apply regular expressions in Python. This module includes a bunch of different functions that can help manipulate strings. 
# Let's see how we can use this module for some basic matching

import re

result = re.search(r"aza", "plaza")

# We call the search function on the re module, and told it to use the pattern aza on the string plaza. We then stored the return value of that function in the result variable. 
# The r at the beginning of the pattern indicates that this is a rawstring. This means that Python interpreter shouldn't try to interpret any special characters, and instead,
# should just pass the string to the function as is. In this example, there are no special characters. The rawstring and the normal string are exactly the same, but it's a good
# idea to always use rawstrings for regular expressions in Python

# let's print the result of the variable and see what we get.
print(result)
# <re.Match object; span=(2,5), match='aza'>

# Great. Our result is a match object. The output we get when calling print already shows some interesting information, like the position in the string that matched ,and what 
# the actual matching string was. Let's try this out again with different word.

# Let's try this out again with different word.

result = re.search(r"aza", "bazar")
print(result)
# <re.Match object; span=(1,4), match='aza'>

# In this case, we can see that the span attribute is different. That's because the match sub-string is in a different position inside the string. The match sub-string is still 
# same though, because we're matching with a plane string. No special syntax yet. What do you think will happen if we pass a string that doesn't match the expression? 

# Let's try and find out

result = re.search(r"aza", "maze")
print(result)
# None

#  If the expression doesn't match the string that we pass, we get none as a result. 
# Remember, none is a special value that Python uses that show that there's none actual value there.


# Let's practice the special characters that we've seen up until now with a few examples.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## QUESTION 1
# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

'''
Here is your output:
True
False
True

Great work! You've written your first regular expression!
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
