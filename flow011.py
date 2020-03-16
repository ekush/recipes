# Created by rashed at 3/9/20
# url: https://www.codechef.com/problems/FLOW011

for test_case in range(int(input())):
    basic = int(input())

    if basic < 1500:
        print(basic+basic*.1+basic*.9)
    else:
        print(basic+500+basic*.98)