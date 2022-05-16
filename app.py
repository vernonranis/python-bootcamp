from art import logo
from os import system

bidders = {}
highest_bidder = {}
more_bidders = True

while more_bidders:
    system("clear")
    print(logo)
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bidders[name] = bid
    loop = input("Are there more bidders:(y/n)")
    if loop == "y":
        more_bidders = True
    elif loop == "n":
        more_bidders = False


for bid in bidders:
    if highest_bidder == {}:
        highest_bidder[bid] = bidders[bid]
    elif list(highest_bidder.values())[0] < bidders[bid]:
        highest_bidder.popitem()
        highest_bidder_key = bid
        highest_bidder_value = bidders[bid]
        highest_bidder[highest_bidder_key] = highest_bidder_value

    
print(f"The highest bidder is {list(highest_bidder.keys())[0]} with a bid of ${list(highest_bidder.values())[0]}")