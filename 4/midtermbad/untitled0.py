# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:39:55 2016

@author: ranko
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    if num == 1:
        return 0
    exp = 1
    base1= base
    while (base ** exp < num):
        base1 *= base
        exp += 1
    print(exp)  
    if base ** exp - num >= abs(base ** (exp - 1) - num):
    #if (base ** exp -  > base ** (exp-1)
                    
        return exp -1
    else:
        return exp