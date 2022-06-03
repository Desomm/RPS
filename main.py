import random


game = False
while not game:
    player = input('Make a choice(R, P, S): ') 

    possibleChoice = ['R', 'P', 'S']
    computer = random.choice(possibleChoice)

    print(f"\nPlayer {player}:CPU {computer}.\n")

    if player == computer:
        print("It is a tie!")
        continue
    if player == 'R' and computer == "S": 
        print("You win, congrats")
        break
    if player == "S" and computer == "R":
        print('Computer wins, sorry')
        break

    if player == 'P' and computer == "R": 
        print("You win, congrats")
        break
    if player == "R" and computer == "P":
        print('Computer wins, sorry')
        break
    
    if player == 'S' and computer == "P": 
        print("You win, congrats")
        break
    if player == "P" and computer == "S":
        print('Computer wins, sorry')
        break
    else:
        print('Your input was invalid,check it and try again.')
