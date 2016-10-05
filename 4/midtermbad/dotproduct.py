# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:27:25 2016

@author: ranko
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    dot = 0
    for i in range(len(listA)):
        dot += listA[i] * listB[i]
    return dot    
        