# Created by rashed at 3/3/20

for i in range(int(input())):
    l = [int(d) for d in str(input())]
    l.reverse()
    print(int("".join(map(str, l))))
