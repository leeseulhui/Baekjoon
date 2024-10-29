import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def count_change(start_color, x, y):
    change = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                next_color = start_color    # 짝수 합 = 시작 색상
            else:
                next_color = 'B' if start_color == 'W' else 'W' # 홀수 합 = 반대 색상

            if board[x + i][y + j] != next_color:
                change += 1 
    return change
            

min_change = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        change_w = count_change('W', i, j)
        change_b = count_change('B', i, j)

        # 최소 변경 수 업데이트
        min_change = min(min_change, change_w, change_b)

print(min_change)