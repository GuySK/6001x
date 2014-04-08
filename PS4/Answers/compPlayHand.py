from ps4a import calculateHandlen, isValidWord, getWordScore, updateHand
from compChooseWord import *
    
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, as follows:

    * The hand is passed as a parameter to a procedure.
    * The computer may return a word or None to indicate she's done playing.
    * Invalid words are rejected, and the hand is terminated.
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the computer 
      procedure is called again to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the 
    * computer procedure returns no words.

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """ 
       
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
        
    outputLine3 = 'Invalid word, hand terminated.'

    def prtLine4(hpts):
        outputLine = 'Run out of letters. Total score: ' + str(hpts) + ' points.'
        print(outputLine)
    # end of code 

    def prtLine5(hpts):
        outputLine = 'Total score: '+ str(hpts) + ' points.'   
        print(outputLine)
    # end of code 
    
    inputLine1 = 'Calling procedure to enter word. If no word is returned hand is finished.'

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
        # currentWord = raw_input(inputLine1)      # get new word
        # print(inputLine1)                         # get new word
        currentWord = compChooseWord(hand, wordList, n)
        
    # If there is no input:
        if currentWord == None:                   # computer has no more words 
            # End the game (break out of the loop)
           break                                # get out of loop

        # Otherwise (the input is not a single period):     
        # If the word is not valid:
        if not isValidWord(currentWord, hand, wordList):       # check if word is valid
            # Reject invalid word (print a message and end hand)
            print(outputLine3)                     # tell the user
            break 
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
