#Step 1 
from random import choice
from os import system

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
guess = ""
display = []
end_of_game = False

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

print (len(display))

for word in chosen_word:
    display.append("_")

while not end_of_game:
    while len(guess) == 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or len(guess) < 1:
            system("clear")
            guess = ""
        else:
            pass
    for index in range(len(chosen_word)):
        if guess in chosen_word[index]:
            display[index] = guess
            system("clear")
        else:
            system("clear")
            pass

    if "_" not in display:
        end_of_game = True
    print(display)
    guess = ""

print("You win")