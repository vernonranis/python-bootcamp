rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choose = [ rock, paper, scissors ]
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if you not in [0, 1, 2]:
  print("You entered an invalid choice")
  exit()
player_1 = choose[you]
print(f"{player_1}")

computer_random = random.randint(0, len(choose)-1)
player_2 = choose[computer_random]
print(f"The computer chose:\n{player_2}")

if player_1 == choose[0] and player_2 == choose[0]: print("its a draw")
if player_1 == choose[0] and player_2 == choose[1]: print("you lose")
if player_1 == choose[0] and player_2 == choose[2]: print("you win")

if player_1 == choose[1] and player_2 == choose[0]: print("you win")
if player_1 == choose[1] and player_2 == choose[1]: print("its a draw")
if player_1 == choose[1] and player_2 == choose[2]: print("you lose")

if player_1 == choose[2] and player_2 == choose[0]: print("you lose")
if player_1 == choose[2] and player_2 == choose[1]: print("you win")
if player_1 == choose[2] and player_2 == choose[2]: print("its a draw")