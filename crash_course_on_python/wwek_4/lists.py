#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Lists
'''
Lists in Python are defined using square brackets, with the elements stored in the list separated by commas: list = ["This", "is", "a", "list"]. 
You can use the len() function to return the number of elements in a list: len(list) would return 4. 
You can also use the in keyword to check if a list contains a certain element. If the element is present, it will return a True boolean. 
If the element is not found in the list, it will return False. For example, "This" in list would return True in our example. 
Similar to strings, lists can also use indexing to access specific elements in a list based on their position. 
You can access the first element in a list by doing list[0], which would allow you to access the string "This".

In Python, lists and strings are quite similar. They’re both examples of sequences of data. Sequences have similar properties, like 
(1) being able to iterate over them using for loops; 
(2) support indexing; 
(3) using the len function to find the length of the sequence; 
(4) using the plus operator + in order to concatenate; and 
(5) using the in keyword to check if the sequence contains a value. 

Understanding these concepts allows you to apply them to other sequence types as well.
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. 
For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1. 
'''
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#############################################################################################
def group_list(group, users):
  members = ", ".join(users)
  return "{}: {}".format(group,members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users:", "")) # Should be "Users:"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Modifying Lists
'''
While lists and strings are both sequences, a big difference between them is that lists are mutable. This means that the contents of the list can be changed, unlike strings, 
which are immutable. You can add, remove, or modify elements in a list.

You can add elements to the end of a list using the append method. You call this method on a list using dot notation, and pass in the element to be added as a parameter. 
For example, list.append("New data") would add the string "New data" to the end of the list called list.

If you want to add an element to a list in a specific position, you can use the method insert. The method takes two parameters: the first specifies the index in the list, 
and the second is the element to be added to the list. So list.insert(0, "New data") would add the string "New data" to the front of the list. This wouldn't overwrite the 
existing element at the start of the list. It would just shift all the other elements by one. If you specify an index that’s larger than the length of the list, the element 
will simply be added to the end of the list.

You can remove elements from the list using the remove method. This method takes an element as a parameter, and removes the first occurrence of the element. If the element 
isn’t found in the list, you’ll get a ValueError error explaining that the element was not found in the list.

You can also remove elements from a list using the pop method. This method differs from the remove method in that it takes an index as a parameter, and returns the element 
that was removed. This can be useful if you don't know what the value is, but you know where it’s located. This can also be useful when you need to access the data and also 
want to remove it from the list.

Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index. For example, you can enter list[0] = "Old data" to 
overwrite the first element in a list with the new string "Old data"
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
The skip_elements function returns a list containing every other element from an input list, starting with the first element. 
Complete this function to do that, using the for loop to iterate through the input list.
'''
def skip_elements(elements):
	# code goes here

	return elements[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
