# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:57:59 2016

@author: ranko
"""
print("Please think of a number between 0 and 100!")
low = 0
high = 100
middle = (low + high) // 2
found = False
while not found:
    print("Is your secret number ? " + str(middle))
    imp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if imp == 'h':
        high = middle
    elif imp == 'l':
        low = middle
    elif imp == 'c':
        print("Game over. Your secret number was: " + str(middle))
        found = True
    else:
        print("Sorry, i did not understand your input.")
    middle = (low + high) // 2    
    