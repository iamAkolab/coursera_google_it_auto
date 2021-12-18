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

'''
Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).
'''
class Dog:
  years = 0
  def dog_years(self) :
         return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
