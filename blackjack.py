import random
import os
import time

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def welcome():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)
    print("Welcome to Blackjack game!\nDispending first card...")
    time.sleep(2)

def dealcard():
    return random.choice(cards)

def playerScore (person):
    sum = 0
    for i in person:
        sum += i
    return sum

def blackjack(sum_of_computer,sum_of_player):
    if sum_of_computer == 21:
        return 1
    elif sum_of_player  == 21:
        return 2
    else:
        return 0 

def printBlackjack(result,computer,player):
    if result == 1:
        print("Computer's card: " ,  [computer] , ", Player's cards: " , [player])
        print(f"computer has a blackjack, it wins!")
        option = input("Press 1 to play again, press 2 to exit:")
        again = playagain(option)
        return again

    elif result == 2:
        print("Computer's card: " ,  [computer] , ", Player's cards: " , [player])
        print(f"You have a blackjack, you wins!")
        option = input("Press 1 to play again, press 2 to exit:")
        again = playagain(option)
        return again    

    
def addCard(person,sumofCard):
    newCard = dealcard()
    person.append(newCard)
    sumofCard += newCard
    return sumofCard

def checkAce (person):
     if 11 in person:
        return True

def changeAce(person,sumofCard):
    person.remove(11)
    person.append(1)
    #calculate new sum
    sumofCard = sum(person)
    return sumofCard

def finalwin (sum_of_computer,sum_of_player):
    if sum_of_player == sum_of_computer:
        return 0
    elif sum_of_computer == 21:
        return 1
    elif sum_of_player == 21:
        return 2
    elif sum_of_computer > 21 and sum_of_player < 21:
        return 2
    elif sum_of_computer < 21 and sum_of_player > 21:
        return 1
    elif sum_of_computer < 21 and sum_of_player < 21 and sum_of_computer > sum_of_player:
        return 1
    elif sum_of_computer < 21 and sum_of_player < 21 and sum_of_computer < sum_of_player:
        return 2

def printresult(computer,player,result):
    print("Computer's card: " ,  computer , ", Player's cards: " , player)
    if result == 1:
        print("Computer wins!")
    elif result == 2:
        print("Player wins!")
    else:
        print("it is a draw.")

def playagain (choice):
    while choice != "1" and choice != "2":
        choice = input("Enter 1 to play again and 2 to exit:")

    if choice != "1":
        return False
    else:
        return True
   
def main():
    again = True
    while again:
        os.system('cls')
        player1 = []
        computer = []
        PC = 0
        player = 0
        #welcoming screen
        welcome()

        
        #distribute cards
        i = 0
        for i in range (2):
            computer.append(dealcard())
            player1.append(dealcard())
        # print(player1,computer)

        #add up the sum of players' cards
        PC = playerScore(computer)
        player =playerScore(player1)

        #check if players have blackjack
        first_result = blackjack(PC,player1)
        printBlackjack(first_result,PC,player1)


        #reveal first card of both players
        print("Computer's first card: " ,  {computer[0]} , ", Player's first cards: " , {player1[0]})
        print("Dispending sencond card...")
        time.sleep(3)

        #if no blackjack, check if computer needs to draw cards
        num = 0
        print("Computer is thinking...")
        time.sleep(1)
        if PC > 16:
            print ("Computer's card is enough.") 
        else:
            print ("Computer is drawing cards.")
            time.sleep(1) 
            while PC <= 16:
                PC = addCard(computer,PC)
                num += 1
                if PC > 16:
                    print(f"computer draw {num} card(s).") 
        
        #check if Ace in computer
        AceCheck = checkAce(computer)
        if AceCheck and PC > 21:
            PC = changeAce(computer,PC)
                
        
        #player's turn to draw card
        print("Your cards: " , player1)
        add = input ("Press 1 to add new card, press 2 to discard:")
        while add == "1":
            player = addCard (player1,player)
            print("Now you have" ,player1)
            add = input ("Press 1 to add another new card, press 2 to continue:")
        
        #check if ace in player
        player_ace = checkAce(player1)
        if player_ace:
            change = input("You have an ace. Press 1 to change its value to 1:")
            if change == "1":
                changeAce(player1,player)


        #display final result
        result = finalwin(PC,player)
        printresult(computer,player1,result)

        #ask if play again
        option = input("Press 1 to play again, press 2 to exit:")
        again = playagain(option)

if __name__ == '__main__':
    main()