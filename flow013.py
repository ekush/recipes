# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/FLOW013

for i in range(int(input())):
    a,b,c = input().split()
    print('YES' if int(a)+int(b)+int(c) == 180 else 'NO')