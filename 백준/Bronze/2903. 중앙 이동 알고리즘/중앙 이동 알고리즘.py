import sys
input = sys.stdin.readline

N = int(input().strip())

result = (2 ** N + 1) ** 2          # ((2 ** N) ** 2) * 4    
print(result)