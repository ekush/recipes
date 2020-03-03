# Created by rashed at 3/3/20


for i in range(int(input())):
    l = [int(d) for d in str(input())]
    before = int("".join(map(str, l)))
    l.reverse()
    after = int("".join(map(str, l)))

    print("losses" if before != after else "wins")