def oddTuples(aTup):
    '''
    Creates a new tuple with every other element
    '''
    newTup = () # new tuple
    count = 0 # index
    for e in aTup:
        if count % 2 == 0: # copy only elements where index is even
            newTup += (aTup[count],) # append element
        count += 1 # and count
    return newTup
# end of code