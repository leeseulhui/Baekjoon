import sys
input = sys.stdin.readline

def process(cmd):
    stack = []
    result = []

    for command in cmd:
        if command.startswith('1'):
            _, x = command.split()
            stack.append(int(x))
        elif command == '2':
            result.append(stack.pop() if stack else -1)
        elif command == '3':
            result.append(len(stack))
        elif command == '4':
            result.append(1 if not stack else 0)
        elif command == '5':
            result.append(stack[-1] if stack else -1)

    return result

n = int(input().strip())
cmd = [input().strip() for _ in range(n)]

output = process(cmd)
print("\n".join(map(str, output)))
