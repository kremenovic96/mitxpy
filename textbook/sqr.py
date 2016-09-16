# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:54:49 2016

@author: ranko
"""

x = 25
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0
ans = 0.0
while abs(ans ** 2-x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print("Numguesses: "+ str(numGuesses))
if abs(ans ** 2 -x) >= epsilon:
    print("failed to finds squuare root ")
else:
    print(str(ans) + " is close to: " + str(x))    