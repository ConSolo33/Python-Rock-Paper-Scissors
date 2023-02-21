from random import randint

print("Let's Play Rock Paper Scissors!")
print('To enter your selection type "rock", "paper", or "scissors". \nTo see scoreboard, type "score". To end session, type "quit".\nHave fun!' )

def computer():
    decision = randint(0,2)
    if decision == 0:
        return "rock"
    elif decision == 1:
        return "paper"
    elif decision == 2:
        return "scissors"

def playerInput():
    player_input = input("Choose your fighter! ")
    if (player_input.lower()) == "quit":
        print("Thanks for playing!")
        return "quit"
    elif (player_input.lower()) == "rock":
        player_choice = "rock"
        return player_choice
    elif (player_input.lower()) == "paper":
        player_choice = "paper"
        return player_choice
    elif (player_input.lower()) == "scissors":
        player_choice = "scissors"
        return player_choice
    elif (player_input.lower()) == "score":
        return "score"
    else:
        print("Invalid input, please try again.")

def run():

    computer_score = 0
    player_score = 0

    while True:
        computer_des = computer()
        player_input = playerInput()


        if computer_des == player_input:
            print(f"Computer chose... {computer_des}")
            print("It's a tie!")
        elif computer_des == "rock" and player_input == "paper":
            print(f"Computer chose... {computer_des}")
            print("You win!")
            player_score += 1
        elif computer_des == "rock" and player_input == "scissors":
            print(f"Computer chose... {computer_des}")
            print("You lose...")
            computer_score += 1   
        elif computer_des == "paper" and player_input == "scissors":
            print(f"Computer chose... {computer_des}")
            print("You win!")
            player_score += 1
        elif computer_des == "paper" and player_input == "rock":
            print(f"Computer chose... {computer_des}")
            print("You lose...")
            computer_score += 1  
        elif computer_des == "scissors" and player_input == "rock":
            print(f"Computer chose... {computer_des}")
            print("You win!")
            player_score += 1
        elif computer_des == "scissors" and player_input == "paper":
            print(f"Computer chose... {computer_des}")
            print("You lose...")
            computer_score += 1  
        elif player_input == "score":
            print(f"Scoreboard: Computer: {computer_score} Player: {player_score}")
            if computer_score > player_score:
                print("Keep trying, you'll get there!")
            elif computer_score == player_score:
                print("It's a dead heat!")
            else:
                print("Great job, keep it up!")
        elif player_input == "quit":
            break 


run()


