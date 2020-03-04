# URL: https://www.codechef.com/problems/TLG

diff = 0
winner = 0
for i in range(int(input())):
    p1, p2 = input().split()
    if (int(p1) - int(p2) != diff and int(p1) - int(p2) < 0):
        diff = abs(int(p1) - int(p2))
        winner = 2
    else:
        diff = abs(int(p1) - int(p2))
        winner = 1
print("%d %d" % (diff, winner))
