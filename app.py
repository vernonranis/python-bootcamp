#Step 1 
from random import choice
from os import system

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
guess = ""
display = []
end_of_game = False

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = len(stages)

#Testing code

for word in chosen_word:
    display.append("_")

while not end_of_game:
    print(f'Pssst, the solution is {chosen_word}.')
    while len(guess) == 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or len(guess) < 1:
            guess = ""
        else:
            pass
    # check guessed letter
    for index in range(len(chosen_word)):
        if guess in chosen_word[index]:
            system("clear")
            display[index] = guess
            print(f"Lives: {lives} {stages[lives]}")
            print(display)
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

        else:
            pass
    
    if guess not in display:
        lives -= 1
        system("clear")
        print(f"Lives: {lives} {stages[lives]}")
        print(display)

    guess = ""
    if "_" not in display:
        end_of_game = True
        print("You Win")
    if lives == 0:
        end_of_game = True
        print("You Lose")
