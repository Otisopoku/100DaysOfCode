# Using the Ceaser cipher to encode and decode a message

import string

letters = string.ascii_lowercase

def caesar_cipher(text, shift, mode = "encode"):
    result = []
    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha(): # only shift letters
            base_letter = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base_letter + shift) % 26 + base_letter)
            result.append(new_char)
        else:
            result.append(char) #keep spaces and punctuations as is
    return "".join(result)

while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ")
    shift_number = int(input("Type the shift number: "))

    print(f"Here's the {choice} result: {caesar_cipher(message, shift_number, choice)}")

    re_play = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if re_play == "no":
        break