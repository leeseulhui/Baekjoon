import sys
input = sys.stdin.readline

N = int(input().strip())

if N == 1:
    exit()

while N % 2 == 0:   # 소인수 홀수만 찾기 위해 2로 먼저 나눔
    print(2)
    N = N // 2

for i in range(3, int(N**0.5) + 1, 2):
    while N % i == 0:
        print(i)
        N = N // i

if N > 1:
    print(N)