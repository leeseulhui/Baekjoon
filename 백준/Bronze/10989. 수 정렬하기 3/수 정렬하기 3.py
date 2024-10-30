import sys
input = sys.stdin.readline

n = int(input())

num_box = [0] * (10000 + 1)

for _ in range(n):
    num_box[int(input())] += 1

for i in range(len(num_box)):
    if num_box[i] != 0:
        for _ in range(num_box[i]):
            print(i)