import sys
input = sys.stdin.readline

store = []

for _ in range(9):
    a = int(input().strip())
    store.append(a)

max_value = max(store)      # 최댓값

max_index = store.index(max_value)  # 해당 최댓값의 인덱스

print(max_value)
print(max_index + 1)

