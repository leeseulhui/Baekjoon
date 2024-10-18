import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mod = pow(10, 9) + 7

# 가장 먼저 dp 배열 초기화 해줘야함
dp = [[0] * (m + 1) for _ in range(n+1)]

# 초기값은 (1,1)
dp[1][1] = 1


for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            continue

        # 1. 아래쪽에서 오는 경우
        if i > 1:
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod

        # 2. 오른쪽에서 오는 경우
        if j > 1:
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod

        # 3. 대각선에서 오는 경우
        if i > 1 and j > 1:
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod

print(dp[n][m])




