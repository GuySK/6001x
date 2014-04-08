def radiationExposure(start, stop, step):
    '''
    Approximates the integral of function f
    '''
    # testing function
    # following lines must be commented before submitting to grader
    def f(x):
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)
    # end of testing function
    x = start
    area = 0
    while x < stop:
        area += step * f(x)
        x += step
    return area
# end of code