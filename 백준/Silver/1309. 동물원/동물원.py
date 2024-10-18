import sys
input = sys.stdin.readline

n = int(input().strip())

# 디피 초기화
dp = [0] * (n + 1)

dp[0] = 1   # 사자를 한 마리도 배치하지 않는 경우의 수

dp[1] = 3   # 세로가 1칸일 경우(아예 배치 x, 오른쪽, 왼쪽 => 3가지)

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i -2] * 1) % 9901   # n-1 칸에서는 2가지 방법 , n칸에서는 1가지 방법

print(dp[n])


