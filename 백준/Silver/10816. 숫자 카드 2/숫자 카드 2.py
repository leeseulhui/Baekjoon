import sys
from collections import Counter

n = int(input().strip())

cards = list(map(int, input().strip().split()))
card_count = Counter(cards) 

m = int(input().strip())

targets = list(map(int, input().strip().split()))
result = [card_count[target] for target in targets]

print(*result)  # 공백으로 구분해서 출력
