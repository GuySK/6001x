def gcdRecur(a,b):
    '''
    Implments Euclid's algorithm for GCD in a recursive way
    '''
# order variables (only necessary during original call)
    if a < b: 
        c = a; # save 'a'
        a = b; b = c; # and swap them
#         
    if b == 0: # check if we're there
        return a # base case
    else:
        return gcdRecur(b, a % b) # nop, follow Euclides
# end of code