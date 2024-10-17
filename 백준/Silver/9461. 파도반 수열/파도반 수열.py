import sys
input = sys.stdin.readline

# p(n) = p(n-2) + p(n-1) 

t = int(input())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1   # 1,2,3 변의 길이는 모두 1로 같음

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])
