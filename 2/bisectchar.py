def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if char == aStr:
            return True
    elif char < aStr[round(len(aStr)/2)-1]:
        return isIn(char, aStr[0:round(len(aStr)/2)-1])
    elif char > aStr[round(len(aStr)/2)-1]:
        return isIn(char, aStr[round(len(aStr)/2)-1:round(len(aStr)-1)])
        
        
