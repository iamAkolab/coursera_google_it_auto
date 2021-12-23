#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Create python module

# Step 1 --- create areas.py file
# cat areas.py
'''
import math

def trainge(base, height):
   return base * (height/2)

def rectangle(base, height): 
   return base * height
   
def circle(radius):
   return math.pi*(radius **2)
'''

# step 2 -- import areas
# >>> import areas
# >>> areas.triangle(3,5)
# 7.5
# >>> areas.circle(4)
# 50.04

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Create python sub module

'''
In some cases, the code we're working with can become more complex. It might make sense to split into submodules. In this case, we create a directory, the name of the module, 
and separate.py files for each of the submodules. So if you have a module split into separate files, and you want the interpreter to recognize the directory has a module, you'll 
need to create the init.py file. If you don't have anything to put in this file, you need to create it. You can leave it empty but it needs to exist for the interpreter to 
recognize directory as a Python module
'''
