import random

paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
      '''

scissors = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
      '''

rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      '''

def PaperScissorsRock():
    name = input("What is your name? \n")
    
    answer = input("Would you like to play a game %s? \n Please enter y for yes or n for no: " % name.capitalize())

    shapes = {1:'paper', 2:'scissors', 3:'rock'}

    print ('')
    print ("LET THE GAMES BEGIN! \n ")
    print ('******************************************************************* \n')
    print ("We shall play a game of Paper Scissors Rock!")
    print ("Best out of 3 games is the winner. \n")
    print ('*******************************************************************')

    winCount = [0,0,0] # player wins, computer wins, and then draws
    
    while answer.lower() == "y":
        
        gameCount = 0

        while gameCount < 3:

            computerNum = random.randint(1,3)
            computerThrow = shapes[computerNum]

            print ('')
            playerThrow = input("Choose your throw: ")

            if playerThrow.lower() not in ['paper', 'scissors', 'rock']:
                print ('')
                print ("That's not a throw silly! Please enter a legal shape! \n")
                continue

            print ('')
            print ("PAPER, SCISSORS, ROCK! \n")
            print ("The computer throws %s" % computerThrow)

            if playerThrow.lower() == "paper":
                
                if computerThrow == "rock":
                    winCount[0] += 1
                    gameCount += 1
                    print (rock)
                    print ("You throw paper.")
                    print (paper)
                    print ("Paper beats Rock! You win!")

                elif computerThrow == "scissors":
                    winCount[1] += 1
                    gameCount += 1
                    print (scissors)
                    print ("You throw paper.")
                    print (paper)
                    print ("Paper loses to Scissors! You lose!")

                elif computerThrow == "paper":
                    winCount[2] += 1
                    print (paper)
                    print ("You throw paper.")
                    print (paper)
                    print ("You both threw Paper! It's a draw!")

            if playerThrow.lower() == "scissors":
                
                if computerThrow == "paper":
                    winCount[0] += 1
                    gameCount += 1
                    print (paper)
                    print ("You throw paper.")
                    print (scissors)
                    print ("Scissors beats Paper! You win!")

                elif computerThrow == "rock":
                    winCount[1] += 1
                    gameCount += 1
                    print (rock)
                    print ("You throw scissors.")
                    print (scissors)
                    print ("Scissors loses to Rock! You lose!")

                elif computerThrow == "scissors":
                    winCount[2] += 1
                    print (scissors)
                    print ("You throw scissors.")
                    print (scissors)
                    print ("You both threw Scissors! It's a draw!")

            if playerThrow.lower() == "rock":
                
                if computerThrow == "scissors":
                    winCount[0] += 1
                    gameCount += 1
                    print (scissors)
                    print ("You throw rock.")
                    print (rock)
                    print ("Rock beats Scissors! You win!")

                elif computerThrow == "paper":
                    winCount[1] += 1
                    gameCount += 1
                    print (paper)
                    print ("You throw rock.")
                    print (rock)
                    print ("Rock loses to Paper! You lose!")

                elif computerThrow == "rock":
                    winCount[2] += 1
                    print (rock)
                    print ("You throw rock.")
                    print (rock)
                    print ("You both threw Rock! It's a draw!")

            print ('\n ******************************************************************* \n')

        if winCount[0] >= 2:
            print("You won best out of 3! \n") #prints if player wins 2 out of 3 games

        elif winCount[1] >= 2:
            print("The computer won best out of 3! \n") #prints if computer wins 2 out of 3 games
            
        answer = input("Would you like to play again? If so, pleast enter y: ")

    print ('')
    print ("You decided not to play anymore. ")
    print ('')
    print ("You won %d times" % winCount[0])
    print ("The computer won %d times" % winCount[1])
    print ("Ended in a draw %d times" % winCount[2])
    print ("GAME OVER")
    print ("Terminating program now.")
    exit
    

    

PaperScissorsRock()
