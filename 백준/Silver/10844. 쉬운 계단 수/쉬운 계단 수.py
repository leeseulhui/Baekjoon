import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

# 길이가 1일 때 계단 수는 각 1개
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]

        if j < 9:
            dp[i][j] += dp[i-1][j+1]

        dp[i][j] %= 1000000000

ans = sum(dp[n]) % pow(10,9)
print(ans)

