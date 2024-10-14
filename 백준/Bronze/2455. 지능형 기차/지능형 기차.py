import sys
input = sys.stdin.readline

cur_person = 0  
max_person = 0

for _ in range(4):
    down_person, up_person = map(int, input().split())

    cur_person -= down_person
    cur_person += up_person

    if cur_person > max_person:
        max_person = cur_person

print(max_person)
    


