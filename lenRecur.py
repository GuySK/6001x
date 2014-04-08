def lenRecur(aStr):
    '''
    Computes the length of a string recursively
    '''
    count = 0
    if aStr == '': # empty. base case
        return count
    else:
        count +=1 # string has at least one character
        return count + lenRecur(aStr[1:]) # shift it to the right and do it again
# end of code    