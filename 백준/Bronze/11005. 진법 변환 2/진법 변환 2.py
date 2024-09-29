import sys
input = sys.stdin.readline

N, B = map(int, input().split())    #N = 10진법 수, B = 바꿀 진법 수 

result = ""

while N > 0:
    rest = N % B
    N = N // B

    if rest >= 10:
        result = result + chr(rest - 10 + ord('A'))

    else:
        result = result + str(rest)

print(result[::-1])