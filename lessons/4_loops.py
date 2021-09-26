# Loops

# There is a form of multi-line code block that can make a section of code repeated as many times over
# as you want
for i in range(20):
    print(i)

# It is important that the code you want repeated, after the ':' on the following line, is indented with
# either 4 spaces or 1 tab, and that the whole script must either use spaces or tabs for indentation
# or it won't run properly

# Range is a new function that returns a list with numbers from 0 up to the number you give it as an argument
list_from_range = range(10)  # creates a list with numbers from 0 to 9

for value in list_from_range:
    print(value)

# You can see that the 'i' in the first loop example has been replaced with 'value' in this one. That is a
# variable created to hold each item in the list being iterated over, at the beginning of each new iteration
# You can rename it and use it as you see fit

# See if you can understand what this loop is doing
cumulative_count = 0

for number in range(20):
    cumulative_count = cumulative_count + number
    print(cumulative_count)

# Each iteration it adds the number taken from the list from range(20) to the cumulative_count variable
# as a result this variable grows each time, giving a running total

# What happens if you change the '+' operator in the previous loop example to a '*' operator? Try it out
