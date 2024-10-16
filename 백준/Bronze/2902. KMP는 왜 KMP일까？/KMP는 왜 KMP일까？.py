import sys
input = sys.stdin.readline

def short(n):
    parts = n.split('-')

    short_n = ''.join([part[0] for part in parts])

    return short_n

n = input()
print(short(n))