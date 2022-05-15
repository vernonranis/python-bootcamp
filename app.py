alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caecar(message, dir, shift_amount):
    msg = list(message)
    final_msg = []
    if dir == "decode":
        shift_amount *= -1
    for index in range(len(text)):
        orig_char_loc = alphabet.index(msg[index])
        new_char_loc = orig_char_loc + shift_amount
        if new_char_loc > 25:
            ext_char_loc = new_char_loc - len(alphabet)
            final_msg.append(alphabet[ext_char_loc])
        else:
            final_msg.append(alphabet[new_char_loc])
    print("".join(final_msg))

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caecar(message = text, dir = direction, shift_amount = shift)