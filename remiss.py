# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/REMISS

for i in range(int(input())):
    a,b = input().split()
    if int(a) > int(b):
        print("%d %d" % (int(a), int(a)+int(b)))
    else:
        print("%d %d" % (int(b), int(a) + int(b)))