from random import choice
from os import system, execl
from sys import executable, argv
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = choice(word_list)
guess = ""
display = []
end_of_game = False
lives = len(stages) - 1
guessed = set()
try_again = ""

for word in chosen_word:
    display.append("_")

system("clear")
while not end_of_game:
    while len(guess) == 0:
        system("clear")
        print(f"{logo}\nLives: {lives}\n{stages[lives]}")
        print(f"Correct Letters so far: {display}")
        print(f"Letters you've already guessed: {list(guessed)}")
        # print(f'Pssst, the solution is {chosen_word}.')
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or len(guess) < 1:
            guess = ""
        else:
            pass

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
            print(logo)
            print(f"Lives: {lives}\n{stages[lives]}")
            print(display)

    guessed.add(guess)
    guess = ""
    if "_" not in display:
        while try_again == "":
            try_again = input("You Win! Do you want to try again? (y/n): ").lower()
            if try_again == "n":
                print("Thank you for playing!")
                end_of_game = True
            elif try_again == "y":
                execl(executable, executable, *argv)
            else:
                print("INVALID INPUT! TRY AGAIN!")
                try_again = ""
    if lives == 0:
        end_of_game = True
        print("Game Over! You Lose")
