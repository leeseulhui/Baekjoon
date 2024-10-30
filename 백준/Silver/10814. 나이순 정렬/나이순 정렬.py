import sys
input = sys.stdin.readline

n = int(input().strip())
member = []

for _ in range(n):
    age, name = input().strip().split()
    age = int(age)
    member.append((age, name))

sorted_member = sorted(member, key= lambda x: x[0])

for age, name in sorted_member:
    print(age, name)

