import sys
input = sys.stdin.readline

# 입력부분
N, K = map(int, input().split())

# N의 약수를 구하는 식
division = []

for i in range(1,N+1):
    if N % i == 0:
        division.append(i)
    
# 구한 약수들 중에서 K번째로 작은 수 구하기
if len(division) >= K:
    print(division[K-1])
else:
    print(0)
