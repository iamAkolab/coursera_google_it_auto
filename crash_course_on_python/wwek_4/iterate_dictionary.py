#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Iterating Over Dictionaries
'''
You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence of keys in the dictionary. 
If you want to access the corresponding values associated with the keys, you could use the keys as indexes. Or you can use the items method on the dictionary,
like dictionary.items(). This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.

If you only wanted to access the keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). 
If you only wanted the values, you could use the values() method: dictionary.values().
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
file_counts = {"jpg":10, "txt":14,"csv":2, "py": 23}
print(file_counts)

for extension in file_counts:
  print(extension)

  # jpg
  # txt
  # csv
  # py
  
 for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext)
        
 # There are 10 files with the .jpg extensions
 #
 #
 #
   
 file_counts.keys()
 # dict_key(['jpg','txt','csv','py'])
        
 file_counts.values()
 # dict_values([10, 14, 2, 23)
        
 for value in file_counts.values():
        print(value)
        
  # 10
  # 14
  # 2
  # 23
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' 
Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
Remember that the items method returns a tuple of key, value for each element in the dictionary.
'''
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, limbs in cool_beasts.items():
    print("{} have {}".format(animal,limbs))
        
 '''
 Here is your output:
octopuses have tentacles
dolphins have fins
rhinos have horns

Nice job! Your dictionary skills are getting stronger and
stronger!

'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Let's check out a simple example of counting how many times each letter appears in a piece of text.

In this code, we're first initializing an empty dictionary, then going through each letter in the given string. 
For each letter, we check if it's not already in the dictionary. And in that case, we initialize an entry in the dictionary with a value of zero. 
Finally, we increment the count for that letter in the dictionary. 

To sum up, we've created a dictionary where the keys are each of the letters present in the string and the values are how many times each letter is present.
Let's try out a few example strings. Count_letters. Let's say a, count_letters("tenant") Count_letters, and this time we'll say a long string with a lot of letters.
'''
 def count_letters(text):
        result = {}
        for letter in text{}:
            if letter not in result:
                    result[leter] = 0
            result[letter] += 1
        return result
  
count_letters("aaaa")
#   {'a':5}
        
count_letters("tenant")
# {'t':2
        
count_letters("a long string with a lot of letters")
#{'a':2,
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
