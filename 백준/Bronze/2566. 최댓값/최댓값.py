import sys
input = sys.stdin.readline

matrix = [] #배열 저장할 리스트

max_value = -1  #어차피 자연수기 때문에 일단 음수로 하나 처리해둠
max_position = (0,0)

for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)



#위에서 만든 9*9 행렬에서 max_value 값 찾기
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_position = (i+1, j+1)   # 인덱스 0번째가 아니라 1번째를 나타내기 위해 +1을 해줌

print(max_value)
print(max_position[0], max_position[1])