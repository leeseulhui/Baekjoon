import sys
input = sys.stdin.readline

N = int(input().strip())
result = []

for _ in range(N):
    A = int(input().strip())
    result.append(A)

cute = result.count(1)
not_cute = result.count(0)

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

