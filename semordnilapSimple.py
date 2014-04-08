def semordnilapSimple(str1, str2):
    '''
    Simple version of semordnilap. Assumes both strs not null with length > 1
    No need of recursion here.
    '''
    if str1[0:].upper() == str2[-1::-1].upper():
        return True
    else:
        return False
# end of code