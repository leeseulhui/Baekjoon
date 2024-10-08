import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n = int(input())
relation = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

#입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(start):
    stack = [(start, 0)]

    while stack:
        node, prv = stack.pop()
        parent[node] = prv

        for nxt in relation[node]:
            if nxt != prv:
                stack.append((nxt, node))

#dfs 실행
dfs(1)

for answer in parent[2:]:
    print(answer)