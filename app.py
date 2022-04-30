height = float(input("How tall are you in CM?: "))
age = int(input("How old are you?: "))
photos = input("Do you want photos?: ")
bill = 0

if height > 120:
  # print("Can ride")
  if age < 12:
    bill += 5
  elif age < 18:
    bill += 7
  elif age >= 45 & age <= 55:
    print("Everything is going to be okay. Have a free ride on us!")
  else:
    bill += 12
else:
  print("Can't ride")

if photos == "Y" or photos == "y":
  bill += 3
elif photos == "N":
  bill += 0
else:
  print("invalid response!")

print(f"Your total bill is {bill}")