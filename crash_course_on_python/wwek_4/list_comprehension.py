#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## List Comprehensions
'''
You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list comprehension. 
List comprehensions allow you to create a new list from a sequence or a range in a single line.

For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. This would iterate over the range 1 to 10, and multiply each element in the range by 2. 
This would result in a list of the multiples of 2, from 2 to 20.

You can also use conditionals with list comprehensions to build even more complex and powerful statements. 
You can do this by appending an if statement to the end of the comprehension. 
For example, [ x for x in range(1,101) if x % 10 == 0 ] would generate a list containing all the integers divisible by 10 from 1 to 100. 
The if statement we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, it gets added to the list.

List comprehensions can be really powerful, but they can also be super complex, resulting in code that’s hard to read. 
Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# using list comprehension
multiples = [ x * 7 for x in range(1,11)
print(multiples)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. 
Hint: remember that list and range counters start at 0 and end at the limit minus 1.
'''
def odd_numbers(n):
	return [x for x in range(0,n+1) if x > 0 and x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
             
# Here is your output:
[1, 3, 5]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 11]
[1]
[]

# Excellent! You're using the power of list comprehension to do a lot of work in just one line!
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
