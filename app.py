alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    unencrypted_msg = list(text)
    encrypted_msg = []
    for index in range(len(text)):
        orig_char_loc = alphabet.index(unencrypted_msg[index])
        new_char_loc = orig_char_loc + shift
        if new_char_loc > 25:
            ext_char_loc = new_char_loc - len(alphabet)
            encrypted_msg.append(alphabet[ext_char_loc])
        else:
            encrypted_msg.append(alphabet[new_char_loc])
    print("".join(encrypted_msg))

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    unencrypted_msg = list(text)
    encrypted_msg = []
    for index in range(len(text)):
        orig_char_loc = alphabet.index(unencrypted_msg[index])
        new_char_loc = orig_char_loc - shift
        encrypted_msg.append(alphabet[new_char_loc])
    print("".join(encrypted_msg))
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(plain_text = text, shift_amount = shift)
else:
    print("Invalid choice!")