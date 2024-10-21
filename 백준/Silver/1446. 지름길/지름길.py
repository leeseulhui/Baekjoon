import sys
input = sys.stdin.readline

# 1. 지름길 정보 저장
# 2. dp 배열 만들어서 각 거리 위치에서 최단 거리 저장
# 3. dp 계산

n, d = map(int, input().split())

dp = [i for i in range(d + 1)]
shortcut = []

for _ in range(n):
    start, end, short = map(int, input().split())
    if end - start > short:
        shortcut.append((start, end, short))

shortcut.sort()

for start, end, short in shortcut:
    for i in range(d + 1):
        if end == i:
            dp[i] = min(dp[i], dp[start] + short)

        else:
            dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[d])



