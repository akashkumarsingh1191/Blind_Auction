# Blind Auction
from replit import clear
from Logo import logo
print(logo)



def find_highest_amount(p_bids):
    highest_bid=0
    bidder_name=""
    for key,value in p_bids.items():
        if value > highest_bid:
            highest_bid=value
            bidder_name=key
    print(f"The winner is {bidder_name} with a bid of $ {highest_bid}")
bids=dict()
bidding_finish=False

while not bidding_finish:   
    name=input("What is your name?: ")
    bid_amount=int(input("What is your bid amount? $"))
    bids[name]=bid_amount
    should_continue=input("Are there any other bidders?(Y/N) ").upper()
    if should_continue =="N":
        bidding_finish = True
        find_highest_amount(bids)
    elif should_continue =="Y":
        clear()