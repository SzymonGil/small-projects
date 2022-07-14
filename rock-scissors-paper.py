import random


while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("pick one from : rock, paper, scissors:").lower()

    if computer == player:
        print(computer)
        print(player)
        print("it's a tie")
    
    elif player == "rock":
        if computer == "paper":
            print(computer)
            print(player)
            print("you lose")
        if computer == "scissors":
            print(computer)
            print(player)
            print("you win")
        
    elif player == "scissors":
        if computer == "roock":
            print(computer)
            print(player)
            print("you lose")
        if computer == "paper":
            print(computer)
            print(player)
            print("you win")
        
    elif player == "paper":
        if computer == "scissors":
            print(computer)
            print(player)
            print("you lose")
        if computer == "rock":
            print(computer)
            print(player)
            print("you win")


    
    play_again = input("do you want to play again? yes/no").lower()
    if play_again != "yes":
        break    