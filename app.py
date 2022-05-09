#Step 1 
from random import choice
from os import system, execl
from sys import executable, argv
from hangman_art import stages, logo
from hangman_words import word_list


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)
guess = ""
display = []
end_of_game = False
lives = len(stages) - 1
guessed = set()
try_again = ""

for word in chosen_word:
    display.append("_")

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
system("clear")
while not end_of_game:
    while len(guess) == 0:
        system("clear")
        print(f"{logo}\nLives: {lives}\n{stages[lives]}")
        print(display)
        print(f'Pssst, the solution is {chosen_word}.')
        guess = input("Guess a letter: ").lower()
        #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        if len(guess) > 1 or len(guess) < 1:
            guess = ""
        else:
            pass

    # check guessed letter
    if guess in guessed:
        input(f"You have already entered the letter {guess}! Try again!")
    else:
        for index in range(len(chosen_word)):
            if guess in chosen_word[index]:
                system("clear")
                display[index] = guess
                print(logo)
                print(f"Lives: {lives}\n{stages[lives]}")
                print(display)
            else:
                pass
        
        if guess not in display:
            lives -= 1
            system("clear")
            #TODO-2: - Import the stages from hangman_art.py and make this error go away
            print(logo)
            print(f"Lives: {lives}\n{stages[lives]}")
            print(display)

    guessed.add(guess)
    guess = ""
    if "_" not in display:
        try_again = input("You Win! Do you want to try again? (y/n): ").lower()
        if try_again == "n":
            print("Thank you for playing!")
            end_of_game = True
        elif try_again == "y":
            execl(executable, executable, *argv)
    if lives == 0:
        end_of_game = True
        print("Game Over! You Lose")
