s = 'azcbobobegghakl'
ans0 = ''
ans1 = ''
for char in s:
	if ans1 == '':
		ans1 += char
	elif char >= ans1[-1]:
		ans1 += char
	elif char < ans1[-1]:
         ans0 += char
	if len(ans0) > len(ans1):
        	ans1 = ''

if len(ans0) > len(ans1):
	ans1 = ans0
print(ans1)			