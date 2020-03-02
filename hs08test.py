"""
URL : https://www.codechef.com/problems/HS08TEST
"""
x, y = input().split()
wamount = int(x)
balance = float(y)

if wamount + 0.5 < balance and wamount % 5 == 0:
    print("%.2f" % (balance - wamount - float(0.5)))

else:
    print("%.2f" % balance)

