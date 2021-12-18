#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## object-oriented programming 

# a way of thinking about and implementing our code.
'''
In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object. 
Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we’re creating an object which is an instance 
of the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, 
while methods are functions that are part of the class.

The idea of object-oriented programming might sound abstract and complex, but you've actually been using objects already without even realizing it. Almost everything in Python 
is an object, all of the numbers, strings, lists, and dictionaries we've seen so far, and have used in our exercises and quizzes, have been objects. And each of them was an 
instance of a class representing a concept. The core, apple pun intended, concept of object-oriented programming comes down to attributes and methods associated with a type. 
The attributes are the characteristics associated to a type, and the methods are the functions associated to a type. In the apple example, the attributes are the color and flavor.
What would the methods be? Well, it depends on what we're going to do with apple. We could maybe have a cut method that turns one whole apple into four slices, or we could have 
an eat method that reduces the amount of apple available with every bite. Let's think about a more IT focused example, like a file in our computer. A file has lots of attributes, 
it has a name, a size, the date it was created, permissions to access it, its contents, and a whole lot more. There are actually so many different file attributes, that Python has
multiple classes to deal with files. The typical file object focuses on the file's contents, and so this object has a bunch of methods to read and modify what's inside the file. 
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Classes and Objects in Python (Optional)
'''
tyoe (string)
# <class str>

When we use the type function as we just did here, Python tells us which class the value or variable belongs to. And since this is a class, it has a bunch of attributes and methods
associated with it. Let's take the string class for an example. In this case, the only attribute is the content of the string. What about the methods? Well, in earlier videos, we 
looked at a bunch of methods provided by the string class, like upper() to create an uppercase version of the string. Or isnumeric() which checks whether or not the contents are 
all numeric. Each string we've used in Python up to now has been a different instance of the string class. They all had the same methods, but the contents were different. This 
meant that the result of calling those methods was different alsol. You can get your computer to list all the attributes and methods in a class. To do that Just use the dir 
function. This gets the Interpreter to print to the screen a list of all the attributes and methods.


We can use the type() function to figure out what class a variable or value belongs to. For example, type(" ") tells us that this is a string class. The only attribute in this 
case is the string value, but there are a bunch of methods associated with the class. We've seen the upper() method, which returns the string in all uppercase, as well as 
isnumeric() which returns a boolean telling us whether or not the string is a number. You can use the dir() function to print all the attributes and methods of an object. 
Each string is an instance of the string class, having the same methods of the parent class. Since the content of the string is different, the methods will return different 
values. You can also use the help() function on an object, which will return the documentation for the corresponding class. This will show all the methods for the class, along 
with parameters the methods receive, types of return values, and a description of the methods.
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Defining Classes (Optional)
'''
We can create and define our classes in Python similar to how we define functions. We start with the class keyword, followed by the name of our class and a colon. Python style
guidelines recommend class names to start with a capital letter. After the class definition line is the class body, indented to the right. Inside the class body, we can define 
attributes for the class.

Let's take our Apple class example:
'''

class Apple:
  color = ""
  flavor = ""

 '''
 We can create a new instance of our new class by assigning it to a variable. This is done by calling the class name as if it were a function. We can set the attributes of our 
 lass instance by accessing them using dot notation. Dot notation can be used to set or retrieve object attributes, as well as call methods associated with the class.
 '''
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

'''
We created an Apple instance called jonagold, and set the color and flavor attributes for this Apple object. We can create another instance of an Apple and set different 
attributes to differentiate between two different varieties of apples.
'''
golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
