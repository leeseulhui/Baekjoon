import sys
input = sys.stdin.readline

N, X = map(int, input().split())

A = list(map(int, input().split()))

#수열 A에서 X보다 작은 값들 출력
for num in A:
    if num < X:
        print(num, end=' ')