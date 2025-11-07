"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000
wallet = 0
action = "MAIN MENU"
while True:
    while action == "MAIN MENU":
        action = input("WOULD YOU LIKE TO WITHDRAW, DEPOSIT, CHECK BALANCE, OR CHECK WALLET? ")

    while action == "WITHDRAW":
        action = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW? "))
        if action <= balance and action > 0:
            balance = balance - action
            wallet = wallet + action
            print (f"YOU HAVE {balance} LEFT IN THE ATM AND {wallet} LEFT IN YOUR WALLET")
            action = "MAIN MENU"
        elif action < 0:
            print ("YOU CAN'T WITHDRAW A NEGATIVE AMOUNT >:C ")
            action = "MAIN MENU"
        elif action > balance:
            print ("YOU ARE TOO BROKE LMAO ")
            action = "MAIN MENU"

    while action == "DEPOSIT":
        action = int(input("HOW MUCH WOULD YOU LIKE TO DEPOST? "))
        if action <= wallet:
            balance = balance + action
            wallet = wallet - action
            print (f"YOU HAVE {balance} LEFT IN THE ATM AND {wallet} LEFT IN YOUR WALLET")
        elif action < 0:
            print ("YOU CAN'T DEPOSIT A NEGATIVE AMOUNT >:C ")
            action = "MAIN MENU"
        elif action > wallet:
            print ("YOU ARE TOO BROKE LMAO ")        
            action = "MAIN MENU"

    while action == "CHECK BALANCE":
        print (f"YOU HAVE {balance} LEFT IN THE ATM")
        if balance == 0:
            print ("HAHA BROKE")
        action = "MAIN MENU"

    while action == "CHECK WALLET":
        print (f"YOU HAVE {wallet} LEFT IN YOUR WALLET")
        if wallet == 0:
            print("HAHA BROKE")
        action = "MAIN MENU"
