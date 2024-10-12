import sys
input = sys.stdin.readline

M = int(input().strip())
N = int(input())

# 소수 저장 리스트
prime = []

for num in range(M, N + 1):
    if num < 2:
        continue

    # 소수 찾기 시작
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        prime.append(num)


if not prime:
    print(-1)

else:
    print(sum(prime))
    print(min(prime))