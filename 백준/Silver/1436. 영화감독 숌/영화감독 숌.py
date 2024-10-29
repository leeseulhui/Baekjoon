import sys
input = sys.stdin.readline

# idea : n이 늘어날 수록 666 앞의 수도 하나씩 증가

n = int(input())
end = 666
count = 0

while(1):
    if '666' in str(end):
        count += 1

    if count == n:
        print(end)
        break

    end += 1