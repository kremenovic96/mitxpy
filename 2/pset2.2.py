# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:49:17 2016

@author: ranko
"""
unpaid = [None] * 12
balance = 320000
testBalance = balance
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lower = balance / 12
upper = (balance * (1 + monthlyInterestRate) ** 12.0) / 12.0
lowest = 1
while  (testBalance >= -0.01) and not(testBalance <= 0.01):
    lowest = (lower + upper) / 2
    #testBalance = balance
    for n in range(12):
        unpaid[n] = testBalance - lowest
        testBalance = unpaid[n] + monthlyInterestRate * unpaid[n]
    if testBalance < -0.01:
        upper = lowest
    elif testBalance > 0.01:
        lower = lowest
    else:
        break
    testBalance = balance    
print("Lowest Payment: " + str(round(lowest,2)))
print(testBalance)
