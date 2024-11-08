import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = {input().strip() for _ in range(n)}

no_look = {input().strip() for _ in range(m)}

result = sorted(no_hear & no_look)

print(len(result))
print("\n".join(result))