# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/AMR15A

input()
even = 0
odd = 0
numbers = [int(n) for n in input().split()]

for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("READY FOR BATTLE" if even > odd else "NOT READY")
