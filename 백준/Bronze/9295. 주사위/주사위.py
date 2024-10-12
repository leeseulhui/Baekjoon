import sys
input = sys.stdin.readline

t = int(input().strip())

tot = 0

for i in range(1, t+1):
    s, c = map(int, input().split())
    t += i
    tot = s + c

    print(f"Case {i}: {tot}")