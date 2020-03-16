# Created by rashed at 3/4/20
# URL: https://www.codechef.com/problems/TRISQ
import math

for test_case in range(int(input())):
    t_side = int(input())
    t_area = (t_side // 2) - 1
    print((t_area * (t_area + 1)) // 2)
