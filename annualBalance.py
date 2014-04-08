def annualBalance(capital, annualInterestRate, monthlyPayment):
    '''
    Calculates balance of sum after one year of fixed payments.
    Takes capital, interst rate and payment as int or floats.
    '''
    period = 0
    interest = 0.0
    newBalance = capital
#    
# Main Loop
    for period in range(1,13):
        newBalance -= monthlyPayment # update balance with payment
        interest = newBalance * (annualInterestRate/12.0) # calculate interest 
        newBalance += interest # and add it to next period"s balance
    return newBalance # final balance          
# end of function