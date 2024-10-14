import sys
input = sys.stdin.readline

cur_person = 0
max_person = 0

for _ in range(10):
    down, up = map(int, input().split())

    cur_person = cur_person - down + up

    max_person = max(max_person, cur_person)

print(max_person)