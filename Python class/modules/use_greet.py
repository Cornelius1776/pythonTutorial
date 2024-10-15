# There are many ways to import a file

# 1.
""" import greet
greet.message()
greet.add(2, 198) """

# 2
""" import greet as g  # g can now be used as a shortcut
g.add(2, 198)
g.message() """

# 3
""" from greet import message # this is very recommended as it only import the needed code
message() 
# add() will also be imported only when needed"""

# 4
""" from greet import * # This is NOT recommended
message()
add(2, 203)
 """


# To see the built-in python modules, pass modules as a string to help()
help("modules")
