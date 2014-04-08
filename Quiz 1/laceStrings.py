def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # 
    s3 = '' # new interlaced string
    i = 0 
    for letter in s1:
        s3 += letter
        if i < len(s2):
            s3 += s2[i]
            i+= 1
    while i < len(s2):
        s3 += s2[i]
        i+= 1        
    return s3
    # end of code    