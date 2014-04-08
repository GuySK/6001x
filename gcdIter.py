def gcdIter(a, b):
    '''
    Iterative version of the Greatest Common Divisor algorithm
    '''
    if a >= b: 
        x = a; y = b # numbers already in order
    else:
        x = b; y = a # put them in order
# iterative part
    z = y # set counter to the smaller one
    while z > 0: 
        if ((x%z == 0) and (y%z == 0)): # check if they divide
            return z # good luck
        z -= 1 # no luck, try again
# end of code