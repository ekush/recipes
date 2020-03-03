# Created by rashed at 3/3/20
# URL: https://www.codechef.com/problems/FLOW017

for i in range(int(input())):
    a,b,c = input().split()
    nums = [int(a), int(b), int(c)]
    nums.sort()
    print(nums[1])