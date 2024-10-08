import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    R, S = input().strip().split()
    R = int(R)

    P = ""  

    for char in S:
        P = P + char * R

    print(P)



    