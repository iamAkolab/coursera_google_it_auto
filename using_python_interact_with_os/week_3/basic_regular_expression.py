#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Simple Matching in Python

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

print(re.search(r"^X", "xenon"))
# <re.Match object; span=(0,1), match='x'>

# Here, we told the Storage function to use the circumflex X pattern on the string xenon. We can see that it matched at the beginning of the line on our X as we expected. 
# What happens if we use a dot which can match any character?

print(re.search(r"aza", "maze"))
# <re.Match object; span=(1,4), match='aza'>

# Now we're using p.ng as a search pattern. It matches the word penguin that we're passing. In the match object ,we see the matching string is peng. 
# Let's try it out with a couple other strings.

print(re.search(r"p.ng", "penguin"))
# <re.Match object; span=(0,4), match='peng'>


print(re.search(r"p.ng", "sponge"))
# <re.Match object; span=(1,5), match='pong'>

print(re.search(r"p.ng", "clapping"))
# <re.Match object; span=(4,8), match='ping'>

# Here we can see the match attribute always has a value of the actual sub string that match the search pattern. The span attribute, indicates the range where the sub string
# can be found in the string we passed. We can also pass additional options to the search function. 

# For example, if we want our match to be case insensitive, we can do this by passing the re.IGNORECASE option
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# <re.Match object; span=(4,8), match='Pang'>

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
## Wildcards and Character Classes
# We've seen by now how we can use a dot in our regular expressions as a special character that can match any character. In the regex world, this is known as a wildcard because 
# it can match more than one character. Using a dot is the broadest possible wildcard because it matches absolutely any character. But what if we wanted something stricter, 
# to restrict our wildcards to a range of characters to do this. For this task we use another feature of regexes called character classes. Character classes are written inside 
# square brackets and let us list the characters we want to match inside of those brackets. For example, say we want to match the word Python but allow for both lowercase or 
# uppercase p. We could do it like this.

print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18,22), match='hway'>

# Inside the square brackets, we can also define a range of characters using a dash. For example, we could use lowercase a to lowercase z to state any lowercase letter. So if we 
# wanted to look for the string way preceded by any letter, we could write the expression like this one

print(re.search(r"[a-z]way", "What a way to go"))
# None

# In this case, we didn't get a match. That's because the string way is preceded by a space and that doesn't match the range that we defined. We can define more ranges like upper 
# case A to upper case Z for all upper case letters or 0 to 9 for all digits. We can combine as many ranges and symbols as we want, like this.

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0,6), match='cloudy'>

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
# <re.Match object; span=(0,6), match='cloud9'>

# Sometimes we may want to match any characters that aren't in a group. To do that, we use a circumflex inside the square brackets. For example, let's create a search pattern 
# that looks for any characters that's not a letter.

print(re.search(r"[^a-zA-Z]", "This is a sentnence with spaces."))
# <re.Match object; span=(4,5), match=' '>
# Here, our pattern matched the first space in the sentence. What if we also add a space to the list of characters that we don't want to match?

print(re.search(r"[^a-zA-Z ]", "This is a sentnence with spaces."))
# <re.Match object; span=(30,31), match='.'>
# Because we added a space inside the character class, our example now matched the final dot in the sentence, which isn't in the list of characters to exclude. 

#If we want to match either one expression or another, we can use the pipe symbol to do that. This lets us list alternative options that can get matched. 
# For example, we could have an expression that matches either the word cat or the word dog, like this.

print(re.search(r"cat|dog", "I like cats."))
# <re.Match object; span=(7,10), match='cat'>

# So since the string contains the sub string cat, the search function could find it. Let's try an example with dog.

print(re.search(r"cat|dog", "I like dogs."))
# <re.Match object; span=(7,10), match='dog'>

# This expression contains a sub string dog, so we found a match. Let's try a sentence with both dogs and cats

print(re.search(r"cat|dog", "I like dogs and cat."))
# <re.Match object; span=(7,10), match='dog'>

# In this string, we actually have two possible matches for our search. But we only get the first one. That's the way the search function works. If we want to get all possible 
# matches, we can do that using the findall function, which is also provided by the re module, like this.

print(re.findall(r"cat|dog", "I like dogs and cat."))
# ['dog','cat']

# So with findall, we don't need to choose between cats and dogs. What a relief.
# These tools can be super useful in the IT world, so you'll definitely want to get a good handle on them. 
# Now, what do you think we'd have to do if we wanted to match something more than once?
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## QUESTION 2
# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

'''
Here is your output:
True
False
True
True
False

Right on! You're seeing the flexibility of character classes
in regular expressions!
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Repetition Qualifiers

# Say we wanted to find the longest word in the string, or we wanted to find the host names in a log file by checking for a bunch of alphanumeric characters between brackets. 
# We can do this using another interesting RegEx concept, repeated matches. It's quite common to see expressions that include a dot followed by a star. This means that it
# matches any character repeated as many times as possible including zero. Let's see a couple of examples of this.

print(re.search(r"Py.*n", "Pygmalion"))
# <re.Match object; span=(0,9), match='Pygmalion'>

# In plain English, you could read this RegEx as match pi followed by any number of other characters followed by n. But with our dot star combination we expanded the range of 
# the match to the whole word. See how the dot takes a different value for each letter? 

#Let's try a different string, Python programming. What do you think the pattern will match?

print(re.search(r"Py.*n", "Python programing"))
# <re.Match object; span=(0,9), match='Python programin'>
# Remember, the Star takes as many characters as possible. In programming terms, we say that this behavior is greedy. It's possible to modify the repetition qualifiers to 
# make them less greedy


# While our pattern could have matched the word Python, it expanded all the way until the last n in the string. If we only wanted our patterns match letters, we should have
# used the character class instead like this.

print(re.search(r"Py[a-z]*n", "Python programing"))
# <re.Match object; span=(0,9), match='Python'>

# Remember how we said that zero times is also a possibility? That will let the string pin also match our pattern. Let's try that out.
print(re.search(r"Py[a-z]*n", "Pyn"))
# <re.Match object; span=(0,3), match='Pyn'>

# As we called out earlier, implementations of regular expressions aren't always the same. Repetition qualifiers are one way they differ. 
# Some implementations like the one used by grep only include the store qualifier that we just discussed. You can do a lot with just a star qualifier. So that's usually good 
# enough. Other implementations like the one used by Python or by the Egrep command include two additional repetition qualifiers plus and question mark, that can help us 
# construct more complex expressions.

# Let's check that out. 

# The plus character matches one or more occurrences of the character that comes before it. So we had the pattern O plus L plus. Let's check it against a few words.
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1,3), match='ol'>
# In this case, there was one occurrence of each. In the match pattern shows us the shortest possible matching string.

print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1,3), match='ooll'>
# Here, there were two of each. Again, we can see the match is a whole string that matches the condition. 

# Let's try something that doesn't match
print(re.search(r"o+l+", "boil"))
# None
#  while our string here had an O and an L, it had another character in between them. Because of this, it doesn't match the search pattern

# The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how this works.

print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3,7), match='each'>
# The P wasn't present but with the question mark we marked it as optional. So we still got a match. Let's see what happens when the P is present.

print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7,12), match='peach'>

# Great the P was president and so match included it. Nice job you're moving right along through basic regular expressions
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## QUESTION 3
# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, 
# while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 

import re
def repeating_letter_a(text):
  result = re.search(r"a.*a|A.*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

'''
Here is your output:
True
False
True
True

You get an A! See how handy the repetition qualifiers can
be, when we're working with lots of different text!
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Escaping Characters

# We've now seen a lot of special characters that we can use in our regular expressions to make them match different kinds of strings: dot, star, plus, question mark, circumflex,
# dollar sign, and square brackets. But what can we do if we need our pattern to match one of the special characters? Say, for example, that we wanted to check that a certain 
# string contained a dot as part of it. If we just put a dot there, it would match any character.

print(re.search(r".com", "welcome"))
# <re.Match object; span=(2,6), match='lcom'>

# Here, we wanted to match on strings that had.com in them, but we match a string with something else in it. That's not what we wanted. To match an actual dot, we need to use an
# Escape character, which in the case of regular expressions is a backslash character. So let's add that to our pattern.

print(re.search(r"\.com", "welcome"))
# None

# By escaping the dot, it no longer matched the word Welcome, and since there's no.com in the string, it returned none. Let's try something that should actually match.

print(re.search(r"\.com", "mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>

# Great. By adding the backslash, we've got this to correctly match what we wanted it to match. We can use a backslash in this way to escape any special characters, including 
# the ones that we haven't even talked about yet. Something to watch out for. It can get really confusing with backslashes since they're also used to define some special string 
# characters. We've called out, for example, that \n is a sequence using Python to indicate a new line, and \t does the same for tabs. When we see a pattern that includes a 
# backslash, it could be escaping a special regex character or a special string character. Using raw strings, like we've been doing, helps avoid some of these possible confusion
# because the special characters won't be interpreted when generating the string. They will only be interpreted when parsing the regular expression. On top of this, Python also 
# uses the backslash for a few special sequences that we can use to represent predefined sets of characters. For example, \w matches any alphanumeric character including letters,
# numbers, and underscores. Let's check out a couple of examples.

print(re.search(r"\w*", "And this is another"))
# <re.Match object; span=(0, 19), match='And'>

print(re.search(r"\w*", "And_this_is_another"))
# <re.Match object; span=(0, 19), match='And_this_is_another'>

# As we said, \w matches letters, numbers, and underscores. In the first example, our pattern matched the first four letters until the space because spaces aren't part of that 
# set of characters. While in the second example, it matched the whole string. 
# There's also \d for matching digits, \s for matching whitespace characters like space, tab or new line, \b for word boundaries and a few others

# You can always consult our cheat sheet or other similar references that tell you which sequence represents which characters. Another great resource for testing out your 
# regular expressions is a website called regex101.com. You can use this to try out your regexes, analyze each part of the expression, and figure out what's up with them 
# when they don't work.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## QUESTION

# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace
# characters.

import re
def check_character_groups(text):
  result = re.search(r"\w\s+\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

'''
Here is your output:
False
True
True
False

You got it! There's no escaping your regular expression
expertise!
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
