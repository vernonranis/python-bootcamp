from os import execl, system
from sys import executable, argv, exit
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

system("clear")
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caecar(message, dir, shift_amount):
    msg = list(message)
    final_msg = []
    if shift_amount > len(alphabet):
        shift_amount %= len(alphabet)
    if dir == "decode":
        shift_amount *= -1
    for index in range(len(text)):
        try:
            orig_char_loc = alphabet.index(msg[index])
            new_char_loc = orig_char_loc + shift_amount
            if new_char_loc > len(alphabet):
                ext_char_loc = new_char_loc - len(alphabet)
                final_msg.append(alphabet[ext_char_loc])
            else:
                final_msg.append(alphabet[new_char_loc])
        except ValueError:
            final_msg.append(msg[index])
            continue
    print("".join(final_msg))

caecar(message = text, dir = direction, shift_amount = shift)

again = input("do you want to try again?(y/n)")

while again:
    if again == "y":
        system("clear")
        execl(executable, executable, *argv)
    elif again =="n":
        exit(0)
    else:
        system("clear")
        print("Invalid Option! Enter Again")