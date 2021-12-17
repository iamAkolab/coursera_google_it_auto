#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Strings

'''
Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. 
For example, double_word("hello") should return hellohello10.
'''
def double_word(word):
#    if(word == ""):
#      return 0
#    else:
      doubleWord = word + word 
      return  str(doubleWord) + str(len(doubleWord))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def first_and_last(message):
    while message != "":
      if(message[0] == message[-1]):
        return True
      else:
        return False
    return True
    
    

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## String Indexing
'''
String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. 
It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. 
If you try to access an index that’s larger than the length of your string, you’ll get an IndexError
'''
text = "Random string with a lot of characters"

print(text[-1])
# s
print(text[-2]
# r
      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## String Slicing
'''
 The slice includes the character at index 1, and excludes the character at index 4. 
 You can also easily reference a substring at the start or end of the string by only specifying one end of the range.
'''

color = "Orange"
color[1:4]
 
 #  'ran'

 ############################################################################################
 
 print(fruit[:4])
 # Pine
 # This gave us the characters from the start of the string through index 3, excluding index 4. 
      
 
 print(fruit[4:]) 
 # apple
 # On the other hand this example gives is the characters including index 4, through the end of the string.
      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
 word = "supercalifragilisticexpialidocious"
print(word.index("x"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
# Function to remove all old email domains
 def replace_domain(email, old_domain, new_domain):
      if "@" + old_domain in email:
           index = email.index("@" + old_domain)
           new_email = email[:index] + "@" + new_domain
           return new_email
      return email
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Advanced Strings Methods
'''
The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper method, which will return the string all in uppercase. 
Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be 
super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.

You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and 
rstrip to remove whitespace only from the left or the right side of the string, respectively.

The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting
the number of times a certain word appears in a sentence or paragraph.

If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and 
False if not.

The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string 
contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!

We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings. This method is called on a string that will be used 
to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using 
the initial string. For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence".

The inverse of the join method is the split method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also 
split by any other characters by passing a parameter.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. 
For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
'''
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# String Formatting
'''
You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, 
as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will 
then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us. 

If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside 
the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. 
This allows for more easily readable code, and for more flexibility with the order of variables.

You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} 
means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. 
You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as 
specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.
'''
##############################################################################
'''
Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
'''
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name,grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
 
#################################################################
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# 7.5 8.175

print("Base price: ${:.2f} With a Tax: ${:.2f}".format(price, with_tax))
# Base price: $7.50 With Taz:$8.18
#################################################################
def to_celsius(x):
      return (x -32)* 5/9

for x in range(0,101, 10):
      print("{:>3} F| {:>6.2f} C".format(x, to_celsius(x)))
 
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
