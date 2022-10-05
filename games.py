import random 
print("Welcome to Paper , Scissor & Rock !! ")
print("Only 5 games.")
print("-----------------------------------")

x = ["rock" , "paper" , "scissor"]
games = 0
point = 0 
while True:
    computer = random.choice(x)
    user = input("Rock , Paper or Scissor? ").lower()
    games = games + 1
    
    print(f"Computer: {computer}")
    print(f"Player: {user}")

    if computer == user:
        print("Equal!!")
        point += 1

    if computer == "rock" and user == "paper":
        print("Paper cover rock. You won!! ")
    if computer == "rock" and user == "scissor":
        print("Rock beats scissor. You lose !!")
    
    if computer == "paper" and user == "rock":
        print("Paper cover rock. You lose !! ")
    if computer == "paper" and user == "scissor":
        print("Scissor cuts paper. You won!!")

    if computer == "scissor" and user == "paper":
        print("Scissor cuts paper. You lose !! ")
    if computer == "scissor" and user == "rock":
        print("Rock beats scissor. You won !!")

    if games == 5 :

        print("Your 5 game has finished!! ")
        print("-----------------------------------")
        print(f"You have won {point} games!!")
        break 


    

    

    