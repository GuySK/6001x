def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
    elif len(aStr) == 1:
        return aStr
    else: 
        return aStr[-1] + reverseString(aStr[:-1])

# end of code for reverseString        