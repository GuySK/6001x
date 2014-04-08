varA = 0
varB = 1
if (type(varA) == str or type(varB) == str): # check if strings involved
    print('string involved')
else:
    if varA > varB:
        print('bigger')
    elif varA == varB:
        print('equal')
    else:
        print('smaller')
    