


def encode(code):
    string = ''
    for i in code:
        j = int(i)+3
        if j >= 10:
            j = str(j)
            j = j[1]

        string += str(j)

    return string


def decode(code): #Colgan Miller coding addition
    decode_string = ""
    for i in code:
        i = int(i)
        j = i - 3
        if j < 0:
            j = 10 + j
        decode_string += str(j)
    return decode_string








def main():
    encoded_password = ""
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))



        if option == 1:
            code = input("Enter your password to encode: ")
            encoded_password = encode(code)
            print("Your password has been encoded and stored!")

        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {code}.")

        elif option == 3:
            break


if __name__ == "__main__":
    main()