# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:59:42 2016

@author: ranko
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (low + high) /2
while abs(ans **2 -x) >= epsilon:
    print("low: "+str(low) +"high: " + str(high) + "ans: " + str(ans))
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2
print("num of guesses: " + str(numGuesses))
print(str(ans) + " is close to sqr of: " + str(x))    
        


