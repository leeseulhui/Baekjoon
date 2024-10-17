import sys
input = sys.stdin.readline

n = int(input())
score = [0] * (n + 1)

for i in range(1, n+1):
    score[i] = int(input()) # 계단의 점수

dp = [0] * (n+1)    # dp 테이블을 먼저 만들고 초기화를 시킴

# 계단이 1개 이하
if n == 1:
    print(score[1])

else:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

    print(dp[n])

