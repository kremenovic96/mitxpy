# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:36:08 2016

@author: ranko
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    a = []
    b = []
    for i in L[::-1]:
        for j in i[::-1]:
            b.append(j)  
            z = b[:]
        a.append(z)    
        b.clear()
    for j in range(len(a)):
        L[j] = a[j]
    
            