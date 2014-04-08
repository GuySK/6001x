from ps4a import *
from compPlayHand import *

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    handsPlayed = False
    outputLine1 = 'Enter n to deal a new hand, r to replay the last hand, or e to end game: '
    outputLine2 = 'You have not played a hand yet. Please play a new hand first!'
    outputLine3 = 'Invalid command.'
    outputLine4 = 'Enter u to have yourself play, c to have the computer play: '
    
    while True:
        cmd = raw_input(outputLine1)
        
        if cmd == 'n':
            while True:
                player = raw_input(outputLine4)
                if player == 'u' or player == 'c':
                    break
                else:
                    print(outputLine3)
            # end of input2 loop
                    
            # deal a new hand
            handsPlayed = True
            hand = dealHand(HAND_SIZE)
            lastHand = hand
            if player == 'u':
                playHand(hand, wordList, HAND_SIZE)
            else:
                compPlayHand(hand, wordList, HAND_SIZE)
              
        elif cmd == 'r':
            # replay hand
            if not handsPlayed:
                print(outputLine2)
            else:
                while True:
                    player = raw_input(outputLine4)
                    if player == 'u' or player == 'c':
                        break
                    else:
                        print(outputLine3)
                # end of input2 loop

                if player == 'u':
                    playHand(lastHand, wordList, HAND_SIZE)
                else:
                    compPlayHand(lastHand, wordList, HAND_SIZE)
                    
        elif cmd == 'e':
            # end game
            break
        else:         
            print(outputLine3)
    return None
    # end of main loop