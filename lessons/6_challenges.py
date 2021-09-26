# Challenges

# Challenge 1: Print all even numbers between 1 and 100

# Challenge 2: Print all cubed numbers between 1 and 100

# Challenge 3, FizzBuzz: Run through the numbers 1 to 100 printing the word 'fizz' for every multiple of 3, printing
# 'buzz' for every multiple of 5, and printing 'FizzBuzz!' for every number that is a multiple of both 3 and 5

# Challenge 4: Print all prime numbers between 1 and 100



# See below for hints, BUT try and do it without first!













































# Hints

# Use the range function to generate numbers up to the number you want so you don't have to type them all out
range(100)  # Will generate a list starting at 0, and ending at 99

# Use the '%' operator to determine if something is odd or even - if x % 2 == 0 then it's an even number
for i in range(5):
    if i % 2 == 0:
        print(i)  # prints only even numbers

# Use an if statement with the '<' operator to prevent numbers over a certain value from being printed
for i in range(100):
    if i < 10:
        print(i)  # prints only up to 9
