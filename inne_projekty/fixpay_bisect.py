# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:57:26 2017

@author: Leszek
"""
from time import time
start = time()
balance, annualInterestRate = 2209697, 0.15
presentBalance = balance
monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = round((balance * (1 + monthlyInterestRate
                                             ) ** 12)/12.0, 4)
monthlyPayment = 0


while presentBalance > 0.01:
    monthlyPayment = (monthlyPaymentLowerBound +
                            monthlyPaymentUpperBound)/2
    month = 1

    while presentBalance > 0 and month <= 12:
        presentBalance -= monthlyPayment
        presentBalance += monthlyInterestRate * presentBalance
        month += 1

    if presentBalance < 0:
        monthlyPaymentUpperBound = monthlyPayment
        presentBalance = balance
    elif presentBalance > 0.01:
        monthlyPaymentLowerBound = monthlyPayment
        presentBalance = balance
    else:
        monthlyPayment += 0.01
        z = round(monthlyPayment, 2)
            

print('Lowest payment: ' + str(z))
print(time() - start)