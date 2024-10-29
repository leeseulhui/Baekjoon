import sys
input = sys.stdin.readline

def equations(a,b,c,d,e,f):
    D = a * e - b * d
    D_x = c * e - b * f
    D_y = a * f - c * d

    # x와 y 계산
    x = D_x // D
    y = D_y // D

    return x, y

a, b, c, d, e, f = map(int, input().split())

x, y = equations(a, b, c, d, e, f)
print(x, y)


    