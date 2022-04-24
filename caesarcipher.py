import random

def encode(word, shift_nr):
    # shift the word about shift_nr (use ascii)
    # get ascii value with chr() or odr()    
    for i in range(0, len(word)):
        c = word[i] # c is the current character we want to shift
        intvalue = ord(c)
        if intvalue < 97 or intvalue > 122:
            continue
        intvalue += shift_nr
        temp = intvalue
        if temp > 122:
            temp -= 25
        new_c = chr(temp)
        word = word[:i] + new_c + word[i+1:]
    print(f"Encoded Word: {word}")
    return word


def decode(word, shift_nr):
    for i in range(0, len(word)):
        c = word[i] # c is the current character we want to shift
        intvalue = ord(c)
        if intvalue < 97 or intvalue > 122:
            continue
        intvalue -= shift_nr
        temp = intvalue
        if temp < 97:
            temp += 25
        new_c = chr(temp)
        word = word[:i] + new_c + word[i+1:]
    print(f"Decoded Word: {word}")
    

def greet(a, b):
    print(f"Hello {a}, welcome to Ceasar Cipher!")
    print(f"The {b} will not be listening.")
    instruction = input(f"Would you like to encode (encrpyt) or decode (decrypt) ? ")
    if instruction == "encode":
        user_input = input("Input the message you want to encode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode(user_input, shift)
    elif instruction == "decode":
        user_input = input("Input the message you want to decode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decode(user_input, shift)
    else:
        print("Sorry we don't support that instruction, you Donut.")
    
    go_on = input("Type 'yes' if you want to go again. Otherwise type anything else.\n")
    while go_on == 'yes':
        instruction = input(f"Would you like to encode (encrpyt) or decode (decrypt) ? ")
        if instruction == "encode":
            user_input = input("Input the message you want to encode:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encode(user_input, shift)
        elif instruction == "decode":
            user_input = input("Input the message you want to decode:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decode(user_input, shift)
        else:
            print("Sorry we don't support that instruction, you Donut.")
        go_on = input("Type 'yes' if you want to go again. Otherwise type anything else.\n")

        print("Bye, see u next time.")


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            return False
    print("prime")    
    return True

greet("Francis", "CIA")  