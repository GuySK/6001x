def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # (b ** myLog(x,b)) <= x
    i = 0
    while b ** i <= x:
        i += 1
    return i-1
    #end of code    