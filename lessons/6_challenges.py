
# Challenge 1: Print all even numbers between 1 and 100

# Challenge 2: Print all cubed numbers between 1 and 100

# Challenge 3, FizzBuzz: Run through the numbers 1 to 100 printing the word 'fizz' for every multiple of 3, printing
# 'buzz' for every multiple of 5, and printing 'FizzBuzz!' for every number that is a multiple of both 3 and 5

# Challenge 4: Print all prime numbers between 1 and 100








hint_string = "cdionomdib"

def decode(string: str):
    print("".join([chr(ord(char) - -5) for char in string]))

decode(hint_string)
