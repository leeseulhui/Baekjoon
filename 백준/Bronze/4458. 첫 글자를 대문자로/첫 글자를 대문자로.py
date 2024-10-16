import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    sen = input().strip()

    print(sen[0].upper() + sen[1:])
        


        