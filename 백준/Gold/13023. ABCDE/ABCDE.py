import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, depth):
    global flag
    if flag:  # 이미 찾았으면 중단
        return
    if depth == 5:  # 친구 관계 5명 연속 발견
        flag = True
        return

    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, depth + 1) # 백트래킹
            visited[nxt] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    if flag:
        break
    visited[i] = True
    dfs(i, 1)  # 시작 노드도 depth=1부터 카운트
    visited[i] = False

print(1 if flag else 0)
