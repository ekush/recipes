# Created by rashed at 3/2/20
# URL : https://www.codechef.com/status/FCTRL2
from functools import reduce

for i in range(int(input())):
    print(reduce((lambda x, y: x * y), ([int(d) for d in range(1, int(input()) + 1)])))
