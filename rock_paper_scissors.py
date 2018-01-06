from random import randint


options = ["Rock", "Paper", "Scissors"]
score = [0,0]

while(True):
    choice = input("Enter Rock, Paper, Scissors, or Quit: ")
    
    if choice == "Quit":
        if score[0] == score[1]:
            print("Tie Game!")
        elif score[0] > score[1]:
            print("You Win!")
        else:
            print("You Lose!")
        exit()
    
    opponent_choice = options[randint(0,2)]
    
    print("Opponent:", opponent_choice)
    print("Your choice:", choice)
    
    if opponent_choice == "Rock":
        if choice == "Rock":
            print("Tie")
        elif choice == "Paper":
            print("Win")
            score[0] += 1
        else:
            print("Lose")
            score[1] += 1
    elif opponent_choice == "Paper":
        if choice == "Paper":
            print("Tie")
        elif choice == "Scissors":
            print("Win")
            score[0] += 1
        else:
            print("Lose")
            score[1] += 1
    else:
        if choice == "Scissors":
            print("Tie")
        elif choice == "Rock":
            print("Win")
            score[0] += 1
        else:
            print("Lose")
            score[1] += 1
        
        