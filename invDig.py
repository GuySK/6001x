def invDig(x):
    if type(x) != int:
        return None
    if x >= 10:
        y = x
        l = 0
        while y > 0:
            y = y/10
            l +=1
        return (x%10)*(10**(l-1)) + invDig((x/10))
    else:
        return x
# end of code