# Created by rashed at 3/4/20
# https://www.codechef.com/problems/PRB01


for i in range(int(input())):
    number = int(input())
    prime = True
    if number == 1:
        prime = False
    else:
        for r in range(2, number - 1):
            if number % r == 0:
                prime = False
                break
    print("yes" if prime is True else "no")
