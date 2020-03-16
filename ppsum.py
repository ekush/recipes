# Created by rashed at 3/9/20
# URL: https://www.codechef.com/problems/PPSUM

for test_case in range(int(input())):
    d, n = input().split()
    total = int(n)
    for r in range(int(d)):
        total = total * (total + 1) // 2
    print(total)
