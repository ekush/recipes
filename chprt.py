# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/CHOPRT


for i in range(int(input())):
    a, b = input().split()
    print('>' if int(a) > int(b) else '<' if int(a) < int(b) else '=')
