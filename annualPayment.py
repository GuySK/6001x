def annualPayment(balance, annualInterestRate, monthlyPayment):
    '''
    Calculates balance after one year of fixed payments
    Takes balance, interes rate and payment as int or floats
    '''
    period = 0
    interest = 0.0
    newBalance = balance 
    payment = monthlyPayment # payment is fixed

# Main Loop
    for period in range(1,13):
        newBalance -= payment # update balance with payment
        interest = newBalance * (annualInterestRate/12.0) # calculate interest 
        newBalance += interest # and add it to next period"s balance
    return newBalance # final balance          
# end of function