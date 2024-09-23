import sys
input = sys.stdin.readline

S = input().strip()

#문자열이 비어있지 않다면?
if S:   
    words = S.split()
    count = len(words)
#문자열이 비어있다면?
else:
    count = 0

print(count)
    
