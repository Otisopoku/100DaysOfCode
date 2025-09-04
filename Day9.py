# creating a secret action program

auction_dict = {}
highest_bid = ""

print("Welcome to the secret auction program.")

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    if auction_dict.get(bid) == None:
        auction_dict[bid] = [name]
    else:
        auction_dict[bid].append(name)


    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if other_bidders.lower() == "no":
        break
    else:
        print("\033c", end="") # clears the terminal 



def find_highest_bidder():
    max_bid = max(auction_dict.keys())
    return max_bid

highest_bid = find_highest_bidder()

print(f"The highest bid is {auction_dict[highest_bid][0]}, ${highest_bid}")
