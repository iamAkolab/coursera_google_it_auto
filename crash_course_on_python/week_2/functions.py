def print_seconds(hours, minutes, seconds):
    print(hours*3600 + minutes *60 + seconds)

print_seconds(1,2,3)

'''
We start a function definition with the def keyword, followed by the name we want to give our function. 
After the name, we have the parameters, also called arguments, for the function enclosed in parentheses. 
A function can have no parameters, or it can have multiple parameters. 

Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. 
Lastly, we put a colon at the end of the line.

After the colon, the function body starts. It’s important to note that in Python the function body is delimited by indentation. 
This means that all code indented to the right following a function definition is part of the function body. 
The first line that’s no longer indented is the boundary of the function body. 

It’s up to you how many spaces you use when indenting -- just make sure to be consistent. 
So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.
'''

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# That double slash operator is called floor division. A floor division divides a number and takes the integer part of the division as the result. 
# For example, five slash slash two is two instead of 2.5

5 // 2 = 2
5 / 2 = 2.5

# None is a very special data type in Python used to indicate that things are empty or that they return nothing.

## CODE REUSE

'''
In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month 
as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed.
'''

def print_monthly_expense(month, hours):
  month_expense = hours * 0.65
  print("In {0} we spent: {1}".format(month,month_expense))

print_monthly_expense("june", 243)
print_monthly_expense("july", 325)
print_monthly_expense("august", 298)



# Take this code snippet for example. It's hard to determine the purpose of this code by just looking at it. The names of the variables don't give the reader much information 
# and although you can likely work out the result of the calculation, there are no clues to what that result might be used for. 
# In programming lingo, when we re-write code to be more self-documenting, we call this process refactoring. 

def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))
	
rectangle_area(5,6)
