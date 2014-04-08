def recursiveLength(x):
    '''
    Finds the length of an integer greater than 0 recursively
    '''
    if x == 0:
        return 0
    else:
        return 1 + recursiveLength(x/10)
# end of code