# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/FLOW018


from functools import reduce

for i in range(int(input())):
    number = int(input())
    if number == 0:
        print(1)
    else:
        print(reduce((lambda x, y: x * y), ([int(d) for d in range(1, number + 1)])))