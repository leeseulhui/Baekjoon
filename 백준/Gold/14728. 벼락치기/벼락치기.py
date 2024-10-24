import sys
input = sys.stdin.readline

def max_score():
    dp = [0] * (t + 1)

    for k,s in score:
        for time in range(t, k - 1, -1):
            dp[time] = max(dp[time], dp[time - k] + s)

    return dp[t]

n, t = map(int, input().split())
score = [tuple(map(int, input().split())) for _ in range(n)]

print(max_score())

