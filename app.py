#Write your code below this line 👇

def prime_checker(number):
  prime_test = []
  for index in range(number):
    prime_test.append(number % (index + 1))
  if prime_test.count(0) == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
