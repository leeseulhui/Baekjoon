import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)
0 < A and B < 10
