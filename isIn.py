def isIn(char, aStr):
    '''
    Finds a character in a string recursively
    '''
    if len(aStr) == 0:     # check if string empty on first call
        return False      # yep.      
    if len(aStr) == 1:      #check if we're running out of chars in string 
        if char == aStr[0]: # yes. is it this one?
             return True   # Found it!
        else: 
            return False   # Nop. Go home.
    else:                   # length is greater than 1
        if (char < aStr[0] or char > aStr[-1:]): # check if within limits
            return False    # Nop. Char is not present.
        else:
            target = len(aStr)/2 # Target the middle of the string
            if char == aStr[target]: # is this it?
                return True # found it!
            elif char < aStr[target]: # check if char in the lower side
                return isIn(char, aStr[0:target]) # it could be. try again.
            else:
                return isIn(char, aStr[target+1:]) # try on the upper side
# end of code         
    
        
     