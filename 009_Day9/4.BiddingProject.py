import os
from art import logo
print(logo)

bidding_data = {}


def find_higest_bidder(bidding_record):
    highest_bid = 0
    # {"Name": 123, "Name2":321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")


bidding = True
while bidding:
    # Add data
    user_name = input("What is your name? : ")
    user_bid = int(input("What is your bid? :"))
    bidding_data[user_name] = user_bid
    want_to_continue = input(
        "Are there any other bidders? Type 'Yes' or 'No'").lower()
    if want_to_continue == "yes":
        os.system('cls')
        # bidding = True
    else:
        os.system('cls')
        bidding = False
        print(logo)
        find_higest_bidder(bidding_data)
