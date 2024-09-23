import sys
input = sys.stdin.readline

N,M = map(int, input().split())

#행렬을 저장할 리스트
A = []
B = []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)


for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

#두 행렬을 저장할 행렬 C
C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])

    C.append(row)

for row in C:
    print(' '.join(map(str, row)))

        