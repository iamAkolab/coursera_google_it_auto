#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Dictionaries Defined
'''
Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. 
However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. 
You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, 
like a string, integer, float, or even tuples.

When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary, the key is specified first, followed by the corresponding value, separated by a colon. For example, animals = { "bears":10, "lions":1, "tigers":2 } creates a dictionary with three key value pairs, stored in the variable animals. The key "bears" points to the integer value 10, while the key "lions" points to the integer value 1, and "tigers" points to the integer 2. You can access the values by referencing the key, like this: animals["bears"]. This would return the integer 10, since that’s the corresponding value for this key.

You can also check if a key is contained in a dictionary using the in keyword. 
Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False.

Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists.
You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals["zebras"] = 2.
This creates the new key in the animal dictionary called zebras, and stores the value 2. 
You can modify the value of an existing key by doing the same thing. So animals["bears"] = 11 would change the value stored in the bears key from 10 to 11.

Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals["lions"] you would remove the key value pair from the animals dictionary.
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = {}

file_counts = {"jpg":10, "txt":14,"csv":2, "py": 23}
print(file_counts)

file_counts["txt"]
# 14

"jpg" in file_counts
# true

"html" in file_counts
# False

# new entry
file_counts["cfg"] = 8

del file_counts["cfg"]
print
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	
1) Add an entry for Epilogue on page 39. 	
2) Change the page number for Chapter 3 to 24. 	
3) Display the new dictionary contents. 	
4) Display True if there is Chapter 5, False if there isn't.
'''
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

'''
Here is your output:
{'Introduction': 1, 'Chapter 1': 4, 'Chapter 2': 11, 'Chapter 3': 24, 'Chapter 4': 30, 'Epilogue': 39}
False
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
