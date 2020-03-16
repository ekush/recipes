# Created by rashed at 3/9/20
# URL: https://www.codechef.com/problems/SMPAIR

for test_case in range(int(input())):
    for series in range(int(input())):
        numbers = [int(d) for d in input().split()]
        numbers.sort()
        print(numbers[0] + numbers[1])
        break
