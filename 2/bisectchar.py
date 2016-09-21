def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
   
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
   # if char == aStr[len(aStr) // 2]:
    #    return True
    if char < aStr[len(aStr) // 2]:
        return isIn(char,aStr[:len(aStr) // 2])
    if char > aStr[len(aStr) // 2]:
        return isIn(char,aStr[len(aStr) // 2 + 1:])
            
    if char == aStr[len(aStr) // 2]:
        return True       

print(isIn('w', 'dgkntw'))
print(isIn('f', 'dhjksuwxy'))       
