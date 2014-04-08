def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    allLetters = string.ascii_lowercase
    availableLetters = ''
    for letter in allLetters:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
# end of code