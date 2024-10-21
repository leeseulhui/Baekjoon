import sys
input = sys.stdin.readline

def DP():
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] > -1:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

                # 오른쪽 카드 버리면 버린만큼의 점수 획득
                if j < n and a[i] > b[j]:
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b[j])

    return dp

def solution():
    if max(a) > max(b):
        print(sum(b))
        return
    dp = DP()
    ans = max(max(dp[n]), max([_dp[n] for _dp in dp]))  # dp[n]으로 접근
    print(ans)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

solution()
