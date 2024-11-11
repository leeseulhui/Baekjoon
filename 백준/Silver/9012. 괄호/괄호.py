import sys
input = sys.stdin.readline

#괄호가 제대로 짝을 이루고 있다 => yes, 그렇지 않다 => no

t = int(input().strip())

for _ in range(t):
    line = input()
    stack = []

    for i in line:
        if i == '(':        # 현재 문자가 ( 인 경우 -> 스택에 현재 문자 추가
            stack.append('(')
        elif i ==')':   # 현재 문자가 ) 인 경우 -> 스택에서 마지막에 추가된 )를 pop(제거)
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()


    if len(stack) != 0: # 스ㅐㄱ이 비어있지 않다면?
        print('NO')
    else:   # 스택이 비어있다면?
        print('YES')


