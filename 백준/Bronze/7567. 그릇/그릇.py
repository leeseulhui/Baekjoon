import sys
input = sys.stdin.readline

def bowl_height(N):
    height = 10  

    for i in range(1, len(N)):
        if N[i] == N[i - 1]:
            height += 5  
        else:
            height += 10  
    return height

N = input().strip()

result = bowl_height(N)
print(result)

