import random

def getUserChoice():

    while True:

        userChoice = input("Choose Rock, Paper, or Scissors: ").strip().lower()

        if userChoice in ['rock', 'paper', 'scissors']:
            return userChoice
        
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def getComputerChoice():
    
    return random.choice(['rock', 'paper', 'scissors'])

def determineWinner(userChoice, computerChoice):

    if userChoice == computerChoice:
        return "It's a tie!"
    
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'paper' and computerChoice == 'rock') or \
         (userChoice == 'scissors' and computerChoice == 'paper'):
        return "You win!"
    
    else:
        return "Computer wins!"

def play():

    print("Let's play Rock-Paper-Scissors!")
    userChoice = getUserChoice()
    computerChoice = getComputerChoice()
    print(f"You chose {userChoice}, and the computer chose {computerChoice}.")
    print(determineWinner(userChoice, computerChoice))

play()