# Types and Variables

# A type is a form in which data can exist in code. You've seen the 'string' type already in the previous
# lesson - comments and printing

# There is a type called integer that represents whole numbers, and this can be shown by just writing the
# numbers out in code

# This is an integer
42

# The print function will accept an integer and print its value
print(42)

# There is another type called float which represents numbers and their decimals. Include a decimal in the
# number to create one
5.5

# This can also be printed
print(5.5)

# Variables

# To store a value of a certain type, you can use a variable. Simply pick a name for it and use the '=' sign
# to assign the value to the newly created variable
my_variable = "hello world"

print(my_variable)

# As you can see, after creating the variable, it can be referenced later to access its value

# You can change the value of a variable multiple times. Try running the following 4 lines of code to
# understand why it does what it does
my_variable = 42
print(my_variable)
my_variable = 9001
print(my_variable)

# You can have a list of values, a collection of many entries all grouped into one thing
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Lists in Python can contain different types
my_list = ["hello", 42, 3.1, "world"]
print(my_list)
