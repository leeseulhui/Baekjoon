import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    p = int(input().strip())    #고려해야될 선수의 수
    most_palyer = ""
    most_price = 0
    

    for _ in range(p):
        C, name = input().split()
        C = int(C)

        if C > most_price:
            most_price = C
            most_name = name

    print(most_name)

    
        



