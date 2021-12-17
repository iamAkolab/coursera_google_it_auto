#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Strings

'''
Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. 
For example, double_word("hello") should return hellohello10.
'''
def double_word(word):
#    if(word == ""):
#      return 0
#    else:
      doubleWord = word + word 
      return  str(doubleWord) + str(len(doubleWord))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def first_and_last(message):
    while message != "":
      if(message[0] == message[-1]):
        return True
      else:
        return False
    return True
    
    

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## String Indexing
'''
String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. 
It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. 
If you try to access an index that’s larger than the length of your string, you’ll get an IndexError
'''
text = "Random string with a lot of characters"

print(text[-1])
# s
print(text[-2]
# r
      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## String Slicing
'''
 The slice includes the character at index 1, and excludes the character at index 4. 
 You can also easily reference a substring at the start or end of the string by only specifying one end of the range.
'''

color = "Orange"
color[1:4]
 
 #  'ran'
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 fruit = "Pineapple"
 
 print(fruit[:4])
 # Pine
 # This gave us the characters from the start of the string through index 3, excluding index 4. 
      
 
 print(fruit[4:]) 
 # apple
 # On the other hand this example gives is the characters including index 4, through the end of the string.
      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
      
 
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
