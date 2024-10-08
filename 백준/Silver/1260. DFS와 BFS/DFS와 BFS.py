import sys
input = sys.stdin.readline

def dfs(c):
    ans_dfs.append(c)   #방문 노드 추가
    visited[c] = 1  #방문 표시

    for n in adj[c]:
        if not visited[n]:    #방문하지 않은 노드인 경우
            dfs(n)

def bfs(start):
    q = []      # 필요한 q, visted[] 변수 생성
    q.append(start)
    ans_bfs.append(start)
    visited[start] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not visited[n]:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1  # 0은 미방문, 1은 방문 따라서 적용됐으니, 1인 방문으로 표시


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())

    #이렇게 양쪽 다 append 해주는 이유는 간선 = 양방향 이라는 조건 때문
    adj[a].append(b)
    adj[b].append(a)

# 1. 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)


