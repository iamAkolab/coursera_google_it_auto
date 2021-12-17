#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Tuple
'''
As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data 
type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. 
They’re specified using parentheses instead of square brackets.

You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and 
will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the 
element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values 
as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate 
variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds

result = conver_seconds(5000)
print(result)
# (1, 2, 30)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Let's use tuples to store information about a file: its name, its type and its size in bytes. 
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes)up to 2 decimal places. 
'''
def file_size(file_info):
	___, ___, ___= file_info
	return("{:.2f}".format(___ / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
