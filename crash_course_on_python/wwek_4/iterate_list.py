#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Iterating Over Lists Using Enumerate
'''
When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable.
But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. 
The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. 
The first value of the tuple is the index and the second value is the element itself.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.
'''
def skip_elements(elements):
	# code goes here
	
	return elements[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Here is your output:
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']

# Great job! The enumerate function sure makes things easier,
# doesn't it?
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
