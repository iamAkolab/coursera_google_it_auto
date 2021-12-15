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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
