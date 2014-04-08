def invDigAc(x, a):
#    if type(x) != int: # this should be taken care by the wrapper function
#        return None
    if x >= 10:         # check if last digit to process
        ac = 0          # nop. set up new accumulator
        y = x           # working variable to determine length               
        l = 0           # length of integer
        while y > 0:    # while loop computes length of integer
            y = y/10
            l +=1
        ac = a + (x%10)*(10**(l-1)) # for the sake of clarity, new accum
        return invDigAc(x/10, ac) # recursion
    else:
        return a+x # last digit, just added to the acc
# end of code