import sys
input = sys.stdin.readline

A, B = map(int, input().split())

-10000 <= A and B <= 10000

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")

