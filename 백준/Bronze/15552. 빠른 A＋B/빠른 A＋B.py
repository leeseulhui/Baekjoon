import sys
input = sys.stdin.readline


T = int(input())

T >= 1000000
sum = 0

for _ in range(T):
    A, B = map(int, input().split())
    1<=A <= 1000 and 1<= B <= 1000
    sum = A + B
    print(sum)