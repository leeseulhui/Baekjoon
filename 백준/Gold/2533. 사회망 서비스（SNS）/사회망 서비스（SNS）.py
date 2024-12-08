import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    visited[v]=True #방문처리
    for next in adj[v]: #인접한 노드 방문
        if(visited[next]): continue #방문했다면 넘어가기
        dfs(next) #인접한 다음 노드 dfs
        dp[v][0]+=dp[next][1] #내가 얼리얼답터가 아니면 자식노드가 얼리어답터여야해
        dp[v][1]+=min(dp[next]) #내가 얼리얼답터면 자식노드가 뭐든 상관 없어


N = int(input())
adj = [[] for _ in range(N+1)]
visited=[False]*(N+1)

dp= [[0,1] for _ in range(N+1)]

for i in range(N-1):
    f,t=map(int,input().split())
    adj[f].append(t)
    adj[t].append(f)

dfs(1) #아무 노드에서 시작해도 무방
print(min(dp[1]))