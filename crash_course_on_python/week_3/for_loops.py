#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## For Loops Recap

# For loops allow you to iterate over a sequence of values.

for x in range(5):

  print(x)
  
# The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. 
# You can use for loops to iterate over a list of strings, such as usernames or lines in a file.

# Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. 
# A for loop works well when you want to iterate over a sequence of elements. 

###################################
# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

###################################
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## A Closer Look at the Range() Function
# Previously we had used the range() function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. 
# But the range() function can do much more than that. We can pass in two parameters: the first specifying our starting point, the second specifying the end point. 
# Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified.

# The range() function can take a third parameter, too. This third parameter lets you  alter the size of each step. 
# So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5.

# To quickly recap the range() function when passing one, two, or three parameters:
# One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
# Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
