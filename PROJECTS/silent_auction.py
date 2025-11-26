import os

def find_winner(bidder_info):
    highest_bid = 0
    winner = ""
    for bidder in bidder_info:
        amount_to_bid = bidder_info[bidder]
        if amount_to_bid > highest_bid:
            highest_bid = amount_to_bid
            winner = bidder
    print(f"{winner} won this round with ${highest_bid}")
    
    

bidder_data = {}
termination = False

while not termination:
    bidder_name = input("Enter your name:")
    bid = int(input("How much are you bidding?:"))
    bidder_data[bidder_name] = bid

    re_bid = input("Is there another bidder?(Y/N):").lower()
    if re_bid == 'n':
        find_winner(bidder_data)
        print(bidder_data)
    else:
        os.system('cls')
       
        
        
        
        
         