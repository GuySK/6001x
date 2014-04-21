def isMyNumber(x):
    sn = 1
    if x > sn:
        return 1
    elif x < sn:
        return -1
    else:
        return 0
    
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
    # print('guessing...' + str(guess))
        sign = isMyNumber(guess)
        if sign == 0:
            break
        if sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess