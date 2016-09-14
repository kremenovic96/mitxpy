s = 'azcbobobegghakl'
ans0 = ''
ans1 = ''
counter = 0
for n in range(len(s)):
    
    for i in range(n, len(s)-1):
        if s[i+1] >= s[i]:
            ans0 += s[i]
            counter += 1
        else:
            break
    if len(ans0) > len(ans1):
        ans1 = ans0
        ans0 = ''
    n = counter    
print(ans1)  
print (len(s))