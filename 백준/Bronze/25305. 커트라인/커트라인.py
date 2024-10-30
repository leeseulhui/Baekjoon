import sys
input = sys.stdin.readline

n, k = map(int, input().split())

x_box = list(map(int, input().split()))

x_box.sort(reverse=True)

best_score = x_box[k-1]

print(best_score)



