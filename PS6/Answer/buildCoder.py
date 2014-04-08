def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string
    lowcase = string.ascii_lowercase
    upcase =  string.ascii_uppercase
    codeDict = {}
    
    i = 0
    for letter in lowcase:
        codeDict[lowcase[i]] = lowcase[(i+shift)%26]
        i += 1
    
    i = 0
    for letter in upcase:
        codeDict[upcase[i]] = upcase[(i+shift)%26]
        i += 1        
    
    return codeDict    
# end of code for buildCoder    