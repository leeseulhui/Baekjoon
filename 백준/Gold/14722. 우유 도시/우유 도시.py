import sys
input = sys.stdin.readline

STRAWBERRY, CHOCOLATE, BANANA = 0, 1, 2

def max_milk():

    dp = [[0] * n for _ in range(n)]

    if milks[0][0] == STRAWBERRY:
        dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            # 현재까지 마신 우유 개수
            curr_milk_count = dp[i][j]
            next_milk = curr_milk_count % 3

            # 남쪽으로 이동
            if i + 1 < n:
                if milks[i + 1][j] == next_milk:  # 다음 가게에서 마실 수 있으면
                    dp[i + 1][j] = max(dp[i + 1][j], curr_milk_count + 1)   # 다음으로 넘어감
                else:  # 마실 수 없으면 그대로 유지
                    dp[i + 1][j] = max(dp[i + 1][j], curr_milk_count)

            # 동쪽으로 이동
            if j + 1 < n:
                if milks[i][j + 1] == next_milk:  # 다음 가게에서 마실 수 있으면
                    dp[i][j + 1] = max(dp[i][j + 1], curr_milk_count + 1)
                else:  # 마실 수 없으면 그대로 유지
                    dp[i][j + 1] = max(dp[i][j + 1], curr_milk_count)

    return dp[n - 1][n - 1]

n = int(input())
milks = [list(map(int, input().split())) for _ in range(n)]

print(max_milk())
