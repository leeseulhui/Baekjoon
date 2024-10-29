import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            card_sum = cards[i] + cards[j] + cards[k]

            # 카드 합이 m 넘으면 안됨 + 최대한 m에 가까워야 함
            if card_sum <= m and card_sum > sum:
                sum = card_sum

print(sum)
