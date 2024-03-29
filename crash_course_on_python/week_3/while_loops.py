#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Anatomy of a While Loop
# A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, 
# followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. 

# Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. 
# What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. 
# Once the statement is no longer true, the loop exits and the next line of code will be executed.  

###############################
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))

##################################
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(10)

####################################
username = get_username()
while not valid_username(username):
  print("Invalid username")
  username = get_username()
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Common Pitfalls With Variable Initialization
# You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. 
# This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. 
# The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

# Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. 
# If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, 
# your code may wind up doing something you didn't expect. Don't forget to initialize your variables before using them!

###################################

  def count_down(start_number):
    current=3
    while (current > 0):
      print(current)
      current -= 1
    print("Zero!")
    


count_down(3)

###################################
  
def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
           return n
        n += 1
       
print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Infinite loops and Code Blocks
# Another easy mistake that can happen when using loops is introducing an infinite loop. 
# An infinite loop means the code block in the loop will continue to execute and never stop. 
# This can happen when the condition being evaluated in a while loop doesn't change. 
# Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete." This means that the code encountered an infinite loop, and it timed out after 5 seconds. You should take a closer look at the code and variables to spot where the infinite loop is.
###################################
# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# fixed
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
'''
Here is your output:
1
2
3
4
5

Great work! You've managed to fix the error in the code that was causing an infinite loop!
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
