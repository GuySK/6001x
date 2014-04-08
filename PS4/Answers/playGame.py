def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """

    handsPlayed = False
    outputLine1 = 'Enter n to deal a new hand, r to replay the last hand, or e to end game: '
    outputLine2 = 'You have not played a hand yet. Please play a new hand first!'
    outputLine3 = 'Invalid command.'
    
    while True:
        cmd = raw_input(outputLine1)
        
        if cmd == 'n':
            # deal a new hand
            handsPlayed = True
            hand = dealHand(HAND_SIZE)
            lastHand = hand
            playHand(hand, wordList, HAND_SIZE)
              
        elif cmd == 'r':
            # replay hand
            if not handsPlayed:
                print(outputLine2)
            else:
                playHand(lastHand, wordList, HAND_SIZE)
            
        elif cmd == 'e':
            # end game
            break
        else:         
            print(outputLine3)
    return None
    # end of main loop
#
