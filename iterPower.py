def iterPower(base, exp):
    '''
    Iterative version of exponentiation 
    '''
    counter = exp
    result = 1
    while counter > 0:
        result = result * base
        counter -= 1
    return result
# end of code