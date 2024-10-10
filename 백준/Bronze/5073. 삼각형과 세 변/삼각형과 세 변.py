import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().strip().split())

    if a == 0 and b == 0 and c == 0: 
        break

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")

