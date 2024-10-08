import sys
input = sys.stdin.readline

def opt(A, operator, B):
    if operator == '+':
        return A + B
    elif operator == '*':
        return A * B

    
A = int(input().strip())
operator = input().strip()
B = int(input().strip())

result = opt(A, operator, B)
print(result)

