def find_highest_bidder(dict_bidder):
    winner = ""
    high = 0
    for key in dict_bidder:
        bid_amount = dict_bidder[key]
        if bid_amount > high:
            high = bid_amount
            winner = key
    print(f"the winner is {winner} with bid {high}$")



import art
print(art.logo)
ans = True
bidder_data={}

while ans:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder_data[name] = bid
    check = input("Ara there any other bidders? Type 'yes' or 'no'. ")
    if check == "no":
        ans = False
        find_highest_bidder(bidder_data)
    else:
        print("\n"*20)














