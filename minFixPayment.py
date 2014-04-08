# This program calculates the minimum fixed payment in multiples of ten
# for cancelling a debt in a year with the interest rate provided.
# minFixPayment.py
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
# Main Loop
    for period in range(1,13):
        newBalance -= monthlyPayment # update balance with payment
        interest = newBalance * (annualInterestRate/12.0) # calculate interest 
        newBalance += interest # and add it to next period"s balance
    return newBalance # final balance          
# end of function
#
# Main 
# The following lines must be commented before submitting to grader
balance = float(raw_input('Enter capital: '))
annualInterestRate = float(raw_input('Enter rate: '))
#
payment = balance / 12 # lower limit is for no interest
payment -= payment%10 # truncate to a multiple of 10
# 
while annualBalance(balance,annualInterestRate,payment) > 0:
    payment += 10
print('Lowest payment: ' + str(int(payment)))
# end of code