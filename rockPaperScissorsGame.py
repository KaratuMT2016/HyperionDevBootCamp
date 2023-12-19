import random as rd

def rock_paper_scissors(choice):

    option = ["Rock", "Paper", "Scissors"]

    system_choice = rd.choice(option)

    if system_choice == choice:
        return f"You chose {choice}, and the System chose {system_choice}. So, its a tie!"
            
    elif system_choice == "Rock" and choice == "Paper":
        return f"You chose {choice}, and the System chose {system_choice}. You win!"
        
    elif system_choice == "Rock" and choice == "Scissors":
        return f"You chose {choice}, and the System chose {system_choice}. You win!"
        
    elif system_choice == "Paper" and choice == "Scissors":
        return f"You chose {choice}, and the System chose {system_choice}. You win!"
        
    elif system_choice == "Rock" and choice == "Scissors":
        return f"You chose {choice}, and the System chose {system_choice}. You win!"
        
    elif system_choice == "Paper" and choice == "Rock":
        return f"You chose {choice}, and the System chose {system_choice}. You lose!"
        
    elif system_choice == "Paper" and choice == "Scissors":
        return f"You chose {choice}, and the System chose {system_choice}. You win!"
        
    elif system_choice == "Scissors" and choice == "Rock":
        return f"You chose {choice}, and the System chose {system_choice}. You lose!"
        
    elif system_choice == "Scissors" and choice == "Paper":
        return f"You chose {choice}, and the System chose {system_choice}. You lose!"
        
        
user_choice = input("Enter your choice to play : ").capitalize()

result = rock_paper_scissors(user_choice)

print(result)