import sys
input = sys.stdin.readline

while True:
    T = input()
    if not T:
        break
    A, B = map(int, T.split())
    print(A + B)