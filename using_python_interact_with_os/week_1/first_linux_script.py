#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## First executable sheet in linux

# step 1 -- create the python file
# cat hello_world.py
# print("hello, World")

# when you ran python3 hello_world.py it returns Hello, World

# step 2 -- add the shebang
# Inserting a shebang line (such as #!/usr/bin/env python3) as the first line tells the operating system what command we want to use to execute the script.

# open the file with text editor
# nano hello_world.py
'''
#!/usr/bin/env python3
 print("hello, World")
'''
# then press control X , save the file and accepting the proposed name.

# step 3 -- change to executable
# chmod +x hello_world.py
# now we can now run it as ./ which represents the current directory

# step 4 -- run the script
# ./hello_world.py
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
