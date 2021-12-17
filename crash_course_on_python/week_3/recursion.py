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

"""

#################################
def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)
  
  #################################
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
