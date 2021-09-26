# Booleans and conditionals

# A boolean is another type that we haven't come across yet. It can be either True or False
print(True)
print(False)

# Like how numbers have special operations that can be performed on them, booleans have conditional logic

# The 'and' operator will take two booleans, and return True if they are both True, and False otherwise
print(True and True)  # Prints True, the others print False
print(False and False)
print(False and True)

# The 'or' operator will take two booleans and return True if either or both of them are True, and False
# otherwise
print(False or False)  # Prints False, all others print True
print(True or True)
print(False or True)

# Booleans can be created by evaluating other types

# The '==' operator will check if the values are the same
print(1 == 1)  # True
print(1 == 2)  # False
print("Hello" == "Hello")  # True

# The '!=' operator is not equals. It will return true if the values are NOT the same
print(1 != 1)  # False
print(1 != 2)  # True
print("Hello" != "Hello")  # False

# The '<' and '>' operators are less than or greater than
print(1 > 0)  # True
print(3 < 1)  # False

# The 'not' operator is negation. It will turn True into False, and False into True
print(not True)
print(not False)

# The 'in' operator checks if a value is in a list
my_list = [1, 2, 3, 4, 5]

print(2 in my_list)  # True

# Conditionals

# Conditionals are ways of making some sections of code run and others not
# The 'if' conditional be followed by a boolean. If the boolean is True, the code in that section will run
# If the boolean is false that section of the code will be skipped
if True:
    print("It was true")
if False:
    print("This doesn't print")

# You can substitute boolean calculations instead of the True or False
if 1 in range(10):
    print("1 was present")

# You can immediately follow an if block with an 'elif' block, which acts like an if statement except
# that it will only run if the 'if' statement before it (or other 'elif's) didn't run
if False:
    print("This won't print")
elif True:
    print("This will print")
elif True:
    print("This won't because the previous one was satisfied")

# A block of if / elif statements can be finished by an 'else' block which will always run if nothing
# before it ran
if False:
    print("This won't print")
elif False:
    print("This also won't print")
else:
    print("This will print correctly")

# You can combine the things in this lesson to make more complicated blocks of code
is_tuesday = True
is_october = False

if is_tuesday and not is_october:
    print("it's a Tuesday and not October")
