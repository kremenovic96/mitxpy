#pset 2: payinng off debt
unpaid = [None] * 12
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balance = 42
p = 0
#unpaid[0] = balance
for n in range(12):
    unpaid[n] = balance - (balance * monthlyPaymentRate)
    balance = unpaid[n] + (annualInterestRate / 12.0) * unpaid[n]
    
print("Remaining balance: " + str(round(balance,2)))
 
    