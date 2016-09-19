# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:03:46 2016

@author: ranko
"""
# solution is partly working
s = 'azcbobobegghakl'
ans0 = ''
ans1 = ''


for n in s:
    if ans0 == '':
        ans0 += n
    elif n >= ans0[-1]:
        ans0 += n
    elif ans0[-1] > n:
        if len(ans0) > len(ans1):
            ans1=ans0
            ans0 = n
if len(ans0) > len(ans1):
    ans1 = ans0          

     
print("Longest substring in alphabetical order is: " + ans1)  
