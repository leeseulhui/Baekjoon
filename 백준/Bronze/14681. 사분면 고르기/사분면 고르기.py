import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

-1000 <= x <= 1000 and x != 0
-1000 <= y <= 1000 and x != 0

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)  
elif x < 0 and y < 0:
    print(3)  
else:
    print(4)