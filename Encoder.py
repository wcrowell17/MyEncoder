# William Crowell
"""
Password encoder
receive  an 8 digit password as a string

convert string characters to int and add 3

if the characters are greater than 10, return only the last digit.

"""


def encode(password):
    for char in password:
        char = int(char)
        char += 3
        if char >= 10:
            char = str(char)
            char = char[-1]
        else:
            char = str(char)

        return char


encode("12345678")

def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    input()
    if