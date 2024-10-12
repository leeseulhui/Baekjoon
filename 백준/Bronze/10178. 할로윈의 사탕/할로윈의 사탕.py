import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    c, v = map(int, input().split())

    piece = c // v
    dad = c % v

    print(f"You get {piece} piece(s) and your dad gets {dad} piece(s).")