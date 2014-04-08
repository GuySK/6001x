def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand2 = hand.copy() # working copy of hand

    if word not in wordList: # word must be valid
        return False
    
    for letter in word:
        if hand2.get(letter,0) == 0: # letter not in hand
            return False
        else:
            hand2[letter] -= 1 # update hand with letter use

    return True            
# end of code