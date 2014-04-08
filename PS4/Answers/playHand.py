def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    
       
    strHand = ''
    handPoints = 0    
    wordPoints = 0
    handLen = 0
    currentWord = ''

    def prtLine1(cH):
        outputLine = 'Current Hand: ' + cH 
        print(outputLine)
    # end of code 
    
    def prtLine2(cw, wpts, hpts):
        outputLine = '"'+ cw + '"' + ' earned ' + str(wpts) + ' points. Total: ' + str(hpts) + ' points'
        print(outputLine)
    # end of code 
        
    outputLine3 = 'Invalid word, please try again.'

    def prtLine4(hpts):
        outputLine = 'Run out of letters. Total score: ' + str(hpts) + ' points.'
        print(outputLine)
    # end of code 

    def prtLine5(hpts):
        outputLine = 'Goodbye! Total score: '+ str(hpts) + ' points.'   
        print(outputLine)
    # end of code 
    
    inputLine1 = 'Enter word, or a "." to indicate that you are finished: '

    # Main loop
    while True:

    # Keep track of the total score
        
    # As long as there are still letters left in the hand    
        handLen = calculateHandlen(hand)             # see if hand still valid
        if handLen == 0:
            prtLine4(handPoints)                     # no more words 
            return                                  # end of game

    # Display the hand
        strHand = ''        
        for letter in hand.keys():      # get hand in display format
            for i in range(hand[letter]):
                strHand += letter + ' '      
        prtLine1(strHand)              # display current hand
           
    # Ask user for input            
        currentWord = raw_input(inputLine1)      # get new word

    # If the input is a single period:
        if currentWord == '.':                   # user wants to end hand 
            # End the game (break out of the loop)
           break                                # get out of loop

        # Otherwise (the input is not a single period):     
        # If the word is not valid:
        if not isValidWord(currentWord, hand, wordList):       # check if word is valid
            # Reject invalid word (print a message followed by a blank line)
            print(outputLine3)                     # tell the user 
        else:

            # Otherwise (the word is valid):
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            wordPoints = getWordScore(currentWord, n)    # get points earned
            handPoints += wordPoints                     # accumulate hand points
            prtLine2(currentWord, wordPoints, handPoints) # tell user points earned
            print('')                                   # additional line             
 
            # Update the hand 
            hand = updateHand(hand, currentWord)         # update hand
   
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    prtLine5(handPoints)
    return None
              
    # end of code
#