import sys
input = sys.stdin.readline

x, y, z = map(int, input().split())

prize = 0

if x == y == z: 
    prize = 10000 + x * 1000
elif x == y or y == z or x == z: 
    if x == y:
        prize = 1000 + x * 100
    elif y == z:
        prize = 1000 + y * 100
    elif x == z:
        prize = 1000 + x * 100
else: 
    prize = max(x, y, z) * 100  

print(prize)





