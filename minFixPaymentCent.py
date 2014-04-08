# This program calculates the minimum fixed payment to the cent
# for cancelling a debt in a year with the interest rate provided.
# minFixPaymentCent.py
#
def annualBalance(capital, annualInterestRate, monthlyPayment):
    '''
    Calculates balance of sum after one year of fixed payments.
    Takes capital, interst rate and payment as int or floats.
    '''
    period = 0
    interest = 0.0
    newBalance = capital
#    
    for period in range(1,13):
        newBalance -= monthlyPayment # update balance with payment
        interest = newBalance * (annualInterestRate/12.0) # calculate interest 
        newBalance += interest # and add it to next period"s balance
    return newBalance # final balance          
# end of function
#
# Main 
while True:
# The following lines must be commented before submitting to grader
#
    balance = float(raw_input('Enter capital: '))
    annualInterestRate = float(raw_input('Enter rate: '))
#
# validate input
    if balance < 0 or annualInterestRate < 0:
        print('Error. Balance, interest rate cannot be negative.')
        break
    monthlyInterestRate = annualInterestRate/12.0 # monthly rate
    lowerPayment = balance / 12.0 # lower limit is for no interest
    upperPayment = (balance * (1 + monthlyInterestRate)**12)/12 # upper limit
    loopCounter = 0 # just to know how many iterations takes
    payment = lowerPayment + (upperPayment - lowerPayment) / 2.0 # starting point
#
    while abs(annualBalance(balance,annualInterestRate,payment)) > 0.01:
        loopCounter +=1 # count how many iterations
        if (annualBalance(balance,annualInterestRate,payment) > 0.0): # not enough
            lowerPayment = payment # set new lower limit
        else:
            upperPayment = payment # set new upper limit
        payment = lowerPayment + (upperPayment - lowerPayment)/2 # recalculate 
#        print('Iter no: ' + str(loopCounter))
#        print('Lower limit: ' + str(lowerPayment))
#        print('Upper limit: ' + str(upperPayment))
#        print('New Payment: ' + str(payment))       
#    print('Number of iterations: ' + str(loopCounter))    
    print('Lowest payment: ' + str(round(payment,2)))
    break # finish main loop
# end of code