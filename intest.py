# Created by rashed at 3/2/20

x, y = input().split()
n = int(x)
k = int(y)

count = 0

for i in range(n):
    t = int(input())
    if t % k == 0:
        count = count +1

print(count)