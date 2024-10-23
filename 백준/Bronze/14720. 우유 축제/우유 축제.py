import sys
input = sys.stdin.readline

n = int(input().strip())
stores = list(map(int, input().split()))

current_milk = 0    # 왜? 처음엔 무조건 딸기우유를 마셔야 하니까 0으로 지정함
count = 0   # 아직 우유를 안 마셨으니까 처음엔 0

for store in stores:
    if store == current_milk:
        count += 1
        current_milk = (current_milk + 1) % 3 # 띨기 -> 초코 -> 바나나 순으로 설정

print(count)
