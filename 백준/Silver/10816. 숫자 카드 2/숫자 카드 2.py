import sys
input = sys.stdin.readline
from collections import Counter

n = int(input().strip())
cnt = 0
cards = list(map(int, input().split()))
cards_count = Counter(cards)

m = int(input().strip())
sang_cards = list(map(int, input().split()))
result = [cards_count[sang_card] for sang_card in sang_cards]

print(*result)



