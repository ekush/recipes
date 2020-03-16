# Created by rashed at 3/4/20
# URL: https://www.codechef.com/problems/LAPIN


for test_case in range(int(input())):
    string = input()
    length = len(string)
    first_half = string[0:int(length//2)]
    second_half = string[int(length//2):length]
    print(first_half)
    print(second_half)
    if first_half == second_half:
        print("YES")