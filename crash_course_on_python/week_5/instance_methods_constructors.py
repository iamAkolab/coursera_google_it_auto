#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Instance Methods
'''
What Is a Method?
Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example, only 
modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These instance methods 
can take a parameter called self which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation, 
like self.name, which will access the name attribute of that specific instance of the class object. When you have variables that contain different values for different 
instances, these are called instance variables.
'''
class Piglet:
  name = "piglet"
  
  def speak(self):
    print("Oink! I'm {}! Oink!".format(self.name)

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
# Oink! I'm Hamlet! Oink!


# Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

class Dog:
  years = 0
  def dog_years(self) :
         return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Constructors and Other Special Methods 
          
'''
Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a 
lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.
'''
 class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor         
'''
When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__. You might remember that special methods start and 
end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. 
These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color 
and flavor values all in go:
'''
          
jonagold = Apple("red", "sweet")
print(jonagold.color)
# Red  
 
 '''
 In addition to the __init__ constructor special method, there is also the __str__ special method. This method allows us to define how an instance of an object will be printed 
 when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position
 of the object in memory. Not super useful. Here is our Apple class, with the __str__ method added:
 '''
class Apple:
     def __init__(self, color, flavor):
         self.color = color
         self.flavor = flavor
          
     def __str__(self):
         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
# Now, when we pass an Apple object to the print function, we get a nice formatted string:
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Now, when we pass an Apple object to the print function, we get a nice formatted string:
jonagold = Apple("red", "sweet")
print(jonagold)
# This apple is red and its flavor is sweet
          
# It's good practice to think about how your class might be used and to define a __str__ method when creating objects that you may want to print later.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
