import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().strip().split())

    #종료 조건
    if A == 0 and B == 0:
        break

    if A > B:
        print("Yes")
    else:
        print("No")

    
