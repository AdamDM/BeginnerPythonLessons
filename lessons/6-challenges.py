







hint_string = "cdionomdib"

def decode(string: str):
    print("".join([chr(ord(char) - -5) for char in string]))

decode(hint_string)
