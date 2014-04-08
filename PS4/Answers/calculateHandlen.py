def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for letter in hand:
        handLen += hand[letter]
    return handLen
# end of code