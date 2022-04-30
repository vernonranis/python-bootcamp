# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1 = name1.lower()
n2 = name2.lower()
combi = n1 + n2

true = combi.count("t") + combi.count("r") + combi.count("u") + combi.count("e")
love = combi.count("l") + combi.count("o") + combi.count("v") + combi.count("e")
conv_str = str(true) + str(love)
conv_int = int(conv_str)

if conv_int < 10 or conv_int > 90:
  print(f"Your score is {conv_int}, you go together like coke and mentos.")

elif conv_int >= 40 and conv_int < 50:
  print(f"Your score is {conv_int}, you are alright together.")

else:
  print(f"Your score is {conv_int}.")

