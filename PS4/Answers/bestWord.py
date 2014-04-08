def bestWord(wordsList):
    '''
    Finds the word with most points in the list.
    wordsList is a list of words.
    '''
    
    def wordValue(word):
        '''
        Computes value of word. Word is a string of lowercase letters.
        '''
        SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
        value = 0
        for letter in word:
            value += SCRABBLE_LETTER_VALUES[letter]
        return value
    # end of code
    
    topL = ['', 0]
    for word in wordsList:
        value = wordValue(word)
        if value > topL[1]:
            topL[1] = value
            topL[0] = word
    return topL
# end of code