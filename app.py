import random
print("This is Scissor, Rock, Paper Game")

oponent = ["scissor", "rock", "paper"]

while True:
    print("Player 1: choose one of the following: scissor, rock, paper")
    player1 = input("1. scissor\n2. rock\n3. paper\n > ").lower()
    player2 = random.choice(oponent)
    print(f"Player 2 chosed {player2}")

    if player1 == "scissor" and player2 == "rock":
        print("Player 2 wins")
        
    elif player1 == "scissor" and player2 == "paper":
        print("Player 1 wins")
        
    elif player1 == "rock" and player2 == "scissor":
        print("Player 1 wins")
        
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins")
        
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 wins")
        
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins")
        
    elif player1 == player2:
        print("It's a tie")
        
    else:
        print("Invalid input")

    play_again = input("Do you want to play again? (y/n)")
    if play_again == "n":
        break
    else:
        continue

print("Thank you for playing")

