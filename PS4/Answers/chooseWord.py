def chooseWord(hand, wordList, n):
    '''
    Chooses the word on the list with maximum value according to hand.
    hand a dict of letters and their occurrence. wordList a list of words.
    Returns word.
    '''

    def getLegalWords(hand, wordsList, n):
        '''
        Constructs a sublist of words that can be formed with the letters in hand.
        hand is a dictionary of letter frequency and wordsList a list of words.
        n is the maximum word length allowed.
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
                if len(word) <= n:          # check if word not longer than allowed
                    legalList.append(word)  # and add word to list
        return legalList
    # end of code

    def bestWord(wordsList, n):
        '''
        Finds the word with most points in the list.
        wordsList is a list of words. n is the max allowed word length 
        Returns a list of two elements containing the word and its value.
        '''
        
        def wordValue(word, n):
            '''
            Computes value of word according to game rules. n is max word length 
            Value = len(word) * sum(Letter values) * d; 
            where: if len(word) >= n then d = 2, else d =1. 
            Word is a string of lowercase letters.
            '''
            SCRABBLE_LETTER_VALUES = {
            'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
        }
            value = 0
            letterCount = 0
            for letter in word:
                value += SCRABBLE_LETTER_VALUES[letter]
                letterCount += 1
            value *=  letterCount
            if letterCount >= n:
                value += 50
            return value
        # end of code
        
        topL = ['', 0]
        for word in wordsList:
            value = wordValue(word, n)
            if value > topL[1]:
                topL[1] = value
                topL[0] = word
        return topL
    # end of code
    
    # Main section
    
    legalWords = getLegalWords(hand, wordList, n)  # get all possible legal words
    if len(legalWords) == 0:                       # No legal words 
        return None
    print('Legal words are: '),
    for word in legalWords:
       print(word + ', '),
    print('')
    topValueWord = bestWord(legalWords, n)         # find the best one
    print('Best word is ' + topValueWord[0] + ' with value ' + str(topValueWord[1]))
    return topValueWord[0]
    
# end of code
    