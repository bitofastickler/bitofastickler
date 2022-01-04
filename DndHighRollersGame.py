# This is an attempt at creating a version of "rollies" DND vis a vis Crit Role
import random
import sys
import time
print('WELCOME TO D20 HIGH ROLLERS!!!')

# Amount of money the player has
playerMoney = 50

# The main game loop
while True:
    if playerMoney < 1:
        print('Sorry mate, youre out of money.')
        sys.exit()
    playerMoney = int(playerMoney)
    print('You have %s gold, how much do you wager?' % (playerMoney))
    while True:  # Player input loop
        playerMoney = int(playerMoney)
        print('MAKE YOUR MOVE: enter numeric value or press (q) to quit')
        playerBet = int(input())
        if playerBet == 'q':
            sys.exit()  # Quit the program
        if int(playerBet) <= playerMoney:
            time.sleep(1)
            print('Alright, %s gold it is...' % (playerBet))
            break
        print('Place your bet')
# Player and computer d20 roles
    playerRole = random.randint(1, 20)
    computerRole = random.randint(1, 20)
    if playerRole > computerRole + 4:
        time.sleep(1)
        print('CRITICAL WIN! YOU DOUBLED YOUR BET!')
        playerMoney = (int(playerBet) * 2) + playerMoney
    elif playerRole > computerRole:
        time.sleep(1)
        print('YOU WIN! this time...')
        playerMoney = (int(playerBet) * 1) + playerMoney
    elif computerRole >= playerRole:
        time.sleep(1)
        print('Sorry, you lose.')
        playerMoney = playerMoney - int(playerBet)
