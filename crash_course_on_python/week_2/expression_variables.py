## Data Types

# In Python, text in between quotes -- either single or double quotes -- is a string data type. 
# An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. 
# For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats. 
# When attempting to mix incompatible data types, you may encounter a TypeError.

# type() -  is used to know what type of data you are handling in python

print(type(input()))
# prints the data type of the input

# Variables are names that we give to certain values in our programs. 
# Those values can be of any data type; numbers, strings or even the results of operations. 

# Think of variables as containers for data. When you create a variable in your code, your computer reserves a chunk of its own memory to store that value. 
# This lets the computer access the variable later to read or modify the value

base = 5
height = 3
area = (base * height)/2

print(area)

# Generally, you can name variables whatever you like but there are some restrictions. 
# First, you shouldn't use as variable names any of the key words or functions that Python reserves for its own, like print. 
# Using these reserved terms will make your program confusing to read and will result in errors. 
# Python also has some restrictions on the characters you can use to define a variable. 
# Variable names can't have any spaces and they must start with either a letter or an underscore. Also, they can only be made up of letters, numbers and underscores.

'''
I_am_a_variable is the valid variable name.
I_am_a_variable2 is also a valid variable name. 
1_is_a_number is invalid because variable names must start with a letter or underscore. 
Apples_&_oranges is invalid because it uses the special character uppers hand. 

Last thing, remember that precision is important when programming. 
Python variables are case sensitive, so capitalization matters. 
Lowercase name, uppercase name and all caps name are all valid and different variable names, and that rule on variables is invariable.
'''

sum = 2048 + 4357 + 97658 + 125 + 8
amount = 5
average = sum/amount

print( "The average size is: " + str(average))

'''
 Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.

By contrast, explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. 
We used this in our video example when we wanted to print a number alongside some text. 
Before we could do that, we needed to call the str() function to convert the number into a string. 
Once the number was explicitly converted to a string, we could join it with the rest of our textual string and print the result.
''
