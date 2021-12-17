#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Recursion
"""
Recursion is the repeated application of the same procedure to a smaller problem. Recursion let's us tackle complex problems by reducing the problem to a simpler one

Have you ever played with a Russian nesting doll? They are a great visual example of recursion. Each doll has a smaller doll inside it. 
When you open up the doll to find the smaller one inside, you keep going until you reach the smallest doll which can't be opened

Here's another example with a more complex problem. Imagine you're in a line of people and you want to know how many people are in front of you, and let me tell you 
I can't stand long lines. Anyway, if the line is long, it might be hard to count the people without leaving the line and losing your place. 
Instead you can ask the person in front of you how many people are in front of them. Since this person will be in the same situation as you, 
they'll have to ask the same question to the person in front of them and so on and so on until the question reaches the first person in the line. 
This person can confidently reply that there are no people in front of them. So then the second person in line can reply one, the person behind them replies two, 
and so on until the answer reaches you.

Well, in programming, recursion is a way of doing a repetitive task by having a function call itself. 
A recursive function calls itself usually with a modified parameter until it reaches a specific condition. 
This condition is called the base case. In our earlier examples, the base case would be the smallest Russian doll or the person at the front of the queue. 

A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. 
The base case returns a value without calling the same function.

A recursive function will usually have this structure:
"""
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
    
    
############################################################################
def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)
  
  ####################################################################################################################
  '''
  The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
  For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:
  '''
  
  def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# 
'''
Let's say that you need to write a tool that goes through a bunch of directories in your computer and calculates how many files are contained in each. 
When listing the files inside a directory, you might find subdirectories inside them and you'd want to count the files in those subdirectories as well. 
This is a great time to use recursion. The base case would be a directory with no subdirectories. For this case, the function would just return the amount of files. 
The recursive case would be calling the recursive function for each of the contained subdirectories. 
The return value of a given function call would be the sum of all the files in that directory plus all the files in the contained subdirectories. 
A directory of files that can contain other directories is an example of a recursive structure. 
Because directories can contain subdirectories that contain subdirectories that contain subdirectories, and so on. 
When operating over recursive structure, it's usually easier to use recursive functions than for or while loops. 

Another IT-focused example of a recursive structure is anything that deals with groups of users that can contain other groups. 
We see this situation a lot when using administrative tools like active directory or LDAP. Say your group management software allows you to create groups that have
both users and other groups as their members. And you want to list all human users that are part of a given group. Here you would use a recursive function to go 
through the groups. The base case would be a group that only includes users listing all of them. The recursive case would mean going through all the groups contained 
listing all the users in them and then listing any users contained in the current group.

It's important to call out that in some languages there's a maximum amount of recursive calls you can use. 
In Python by default, you can call a recursive function 1,000 times until you reach the limit. 
That's fine for things like subdirectories or user groups that aren't thousands of levels deep.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
