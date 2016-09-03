# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 21:30:39 2016

@author: ranko
"""

x = int(input("Enter a number:" ))
ans = 0
while ans ** 3 < x:
    ans += 1
if ans ** 3 != x:
    print (str(x) + " is not perfect cube.")
else:
    print('cube of ' + str(x) + ' is ' + str(ans))    
    