def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
    '''
    Divides two integers. It returns 0 if denominator is zero.
    '''
    assert (type(item) == int) and (type (denom) == int), 'Invalid type of parameters'
    try:
        return item / denom
    except ZeroDivisionError:
	return 0
# end of code