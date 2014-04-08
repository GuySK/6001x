def biggest(aDict):
    longest = -1 # just in case there are zero length entries
    bigkey = '' # function must return null if dictionary void
    for k in aDict.keys():
        if len(aDict[k]) > longest: # check for new candidate
            longest = len(aDict[k]) # yep, longer
            bigkey = k # remember key
    if bigkey == '': # check if dictionary empty
        return None 
    else:
        return bigkey 
# end of code