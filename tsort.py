# URL: https://www.codechef.com/problems/TSORT

number_list = []
for i in range(int(input())):
    number_list.append(int(input()))
number_list.sort()
print(*number_list, sep='\n')