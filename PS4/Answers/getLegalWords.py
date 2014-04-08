def getLegalWords(hand, wordsList):
    '''
    Constructs a sublist of words that can be formed with the letters in hand.
    hand is a dictionary of letter frequency and wordsList a list of words.
    '''
    legalList = []
    for word in wordsList:             # word evaluation
        wordLegal = True            # word not guilty until proved contrary
        workHand = hand.copy()          # copy hand so it can be reused
        
        for letter in word:            # check if letter in dictionary
            if workHand.get(letter,0) == 0: # if not present or used up
                wordLegal = False     
                break                  # word is not valid
            else:                      
                workHand[letter] -= 1   # update dictionary and check another letter
                
        if wordLegal:
            legalList.append(word)          # all letters checked. Add word to list
    return legalList
# end of code