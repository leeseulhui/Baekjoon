import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def check(a1, a0, c, n0):
    if a1 > c:
        return 0
    
    if a1 * n0 + a0 <= c * n0:
        return 1
    else:
        return 0
    
print(check(a1, a0, c, n0))


    