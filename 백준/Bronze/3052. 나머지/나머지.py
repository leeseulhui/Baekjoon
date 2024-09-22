import sys
input = sys.stdin.readline

rests = set()    #서로 다른 나머지를 저장할 집합임

for i in range(10):
    number = int(input().strip())
    rest = number % 42
    rests.add(rest)

print(len(rests))
    
        