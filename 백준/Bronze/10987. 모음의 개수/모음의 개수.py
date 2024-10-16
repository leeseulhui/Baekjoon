import sys
input = sys.stdin.readline

w = input().strip()

mou = 'aeiou'

count = 0

for char in w:
    if char in mou:
        count += 1

print(count)