#pset 2: problem  2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:16:05 2016

@author: ranko
"""
balance = 4773
unpaid = [None] * 12
testBalance = balance
annualInterestRate = 0.2
lowest = 0
month = 12
monthlyInterestRate = annualInterestRate / 12.0
while testBalance > 0:
    lowest += 10
    testBalance = balance
    for n in range(12):
        unpaid[n] = testBalance - lowest
        testBalance = unpaid[n] + monthlyInterestRate * unpaid[n]
    
    

print("Lowest payment: " + str(lowest))
