import sys
input = sys.stdin.readline
 
submitted = []

for _ in range(28):
    submitted.append(int(input().strip()))

all_stu = set(range(1,31))  #중복되지 않은 값이어야 하므로 집합 사용

submitted_set = set(submitted)

not_submitted = sorted(all_stu - submitted_set)

print(not_submitted[0])
print(not_submitted[1])