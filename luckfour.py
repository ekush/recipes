# URL: https://www.codechef.com/problems/LUCKFOUR


for i in range(int(input())):
    occurance = 0
    number = [int(d) for d in str(input())]

    for n in number:
        if n == 4:
            occurance = occurance +1
    print(occurance)