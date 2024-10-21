import sys
input = sys.stdin.readline

# 3의 배수와 5의 배수 = 15의 배수
MOD = 1_000_000_007
n = int(input().strip())

dp = [[[0 for _ in range(5)] for _ in range(3)] for _ in range(n + 1)]

dp[0][0][0] = 1


for now in range(n):
    for mod3 in range(3):
        for mod5 in range(5):

            # 숫자 1을 추가
            new_mod3 = (mod3 + 1) % 3
            new_mod5 = (mod5 * 10 + 1) % 5
            dp[now + 1][new_mod3][new_mod5] += dp[now][mod3][mod5]
            dp[now + 1][new_mod3][new_mod5] %= MOD

            # 숫자 5를 추가
            new_mod3 = (mod3 + 5) % 3
            new_mod5 = (mod5 * 10 + 5) % 5
            dp[now + 1][new_mod3][new_mod5] += dp[now][mod3][mod5]
            dp[now + 1][new_mod3][new_mod5] %= MOD

print(dp[n][0][0])




