def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # True if a, b, c exist so 6a+9b+20c=n
    # ok in case n divisible by any one

    def check9N6(n):
        i=0
        while i*9 < n:
            if (n-i*9)%6 == 0:
                return True
            else:
                i+=1
        return False
    #end of code    
    
    if n%6 == 0:
        return True
    elif n%9 == 0: 
        return True
    elif n%20 == 0:
        return True
    else:
        # Try combinations of 9 and 6 until greater than n
        if check9N6(n):
            return True
            
        # No luck with 9 and 6. Try with 20    
        i=1
        while i*20 < n:
            if (n-i*20)%9 == 0:
                return True
            elif (n-i*20)%6 == 0:
                return True
            elif check9N6(n-i*20):
                return True
            else:
                i+=1
        # No luck with 20, 9 and 6. Not possible 
        return False
# end of code        