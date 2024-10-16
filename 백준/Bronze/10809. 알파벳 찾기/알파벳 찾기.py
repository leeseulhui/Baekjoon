import sys
input = sys.stdin.readline

s = input().strip()

for char in range(ord('a'), ord('z') + 1):
    print(s.find(chr(char)), end=' ')
