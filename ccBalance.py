# ccBalance.py
# This program calculates the unpaid balance of a credit card account
#
# The following lines should be commented before submitting to grader
balance = float(raw_input('Enter initial balance: '))
annualInterestRate = float(raw_input('Enter Annual Rate [decimal]: '))
monthlyPaymentRate = float(raw_input('Enter Monthly Payment Rate [decimal]: '))
#
# Print Monthly Report Function
def prtMonRep(period, payment, balance):
    ''' Prints Monthly Report ''' 
    print('Month: ' + str(period))
    print('Minimum monthly payment: ' + str(round(payment,2)))
    print('Remaining balance: ' + str(round(balance,2)))
# end of function
#
# Internal variables
period = 0
payment = 0.0
totalPayment = 0.0
interest = 0.0
newBalance = balance 
#
# Main Loop
for period in range(1,13):
    payment = newBalance * monthlyPaymentRate # payment this period
    totalPayment += payment # keep count of my total payments
    newBalance -= payment # update balance with payment
    interest = newBalance * (annualInterestRate/12.0) # calculate interest 
    newBalance += interest # and add it to next period"s balance
    prtMonRep(period, payment, newBalance) # Print it out 

# Final printout        
print('Total paid: ' + str(round(totalPayment,2)))
print('Remaining balance: ' + str(round(newBalance,2)))
# end of code