#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Figure out what's the relationship between the strings "cat" and "Cat" by replacing the plus sign with comparison operators.

print("cat" < "Cat")
# returns False and "cat" is larger than "Cat"

'''
In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False. 

To check if two values are the same, we can use the equality operator: == 

To check if two values are not the same, we can use the not equals operator: != 

We can also check if values are greater than or lesser than each other using > and <. 
If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError. 

We can make very complex comparisons by joining statements together using logical operators with our comparison operators. 
These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. 
When using the or operator, if either side of the comparison is true, then the whole statement is true. 

Lastly, the not operator simply inverts the value of the statement immediately following it. 
So if a statement evaluates to True, and we put the not operator in front of it, it would become False.
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Branching
'''
 we can dive right into how to use them in our scripts to perform different actions based on their values. 
 The ability of a program to alter its execution sequence is called branching, and it's a key component in making your scripts useful. 
 You probably use the idea of branching a bunch in your everyday life. For example, if it's before noon, you might greet someone by saying good morning instead of good afternoon 
 or good evening. If it's raining outside, you might choose to take an umbrella. If it's cold, you probably wear a jacket. 
 
 In your scripts, you can instruct your computer to make decisions based on inputs to



You may notice that there are some similarities between how an if block and the function are defined. The keyword, either def or if, indicates the start of a special block. 
At the end of the first line, we use a colon, and then the body of the function or the if block is indented to the right. But there's also an important difference between 
how an if block and a function are defined. The body of the if block will only execute when the condition evaluates to true; otherwise, it skipped.
'''

def is_positive(number):
  if number > 0:
    return True
  
  '''
  Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to
  perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. 
  
  This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the 
  if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!
  '''
    


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comparison operators
'''
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b

# Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
