# William Crowell
"""
Password encoder
receive  an 8 digit password as a string

convert string characters to int and add 3

if the characters are greater than 10, return only the last digit.

"""


def encode(password):
    encode = ''
    for char in password:
        char = str((int(char) + 3) % 10)
        encode = encode + char

    return encode

def decode(password):
    # Zachary Novak made this one :)
    result = ''
    for i in password:
        result += str((int(i)-3) if (int(i) > 2) else (int(i)+7))
    return result

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit \n")
        menu_select = input("Please enter an option:")

        if menu_select == '1':
            print("Please enter your password to encode:", end="")
            encode(input())
            print("Your password has been encoded and stored!")
        elif menu_select == '2':
            decoded_password = decode(input())
            print(f'Your decoded password is: {decoded_password}')
        elif menu_select == '3':
            return


if __name__ == "__main__":
    main()
