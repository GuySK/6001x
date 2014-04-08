def semordnilap(str1, str2):
    '''
    Recursive version of semordnilap.
    '''
    if len(str1) != len(str2): # no way if lengths are different
        return False
    if str1[0] == str2[-1:]: # check chars at both extremes
        if len(str1) == 1:   # if no more chars, we're done
            return True     
        else:                # doing fine so far but still more chars to check    
            return semordnilap(str1[1:], str2[0:-1]) # drop chars and go again
    else:                   # chars do not agree
        return False        # it makes no sense to keep on checking
# end of code