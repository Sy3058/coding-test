import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friend = {i:[] for i in range (n)}
visited = [False] * n
flag = False
route = []

for _ in range (m):
  a, b = map(int, input().split())
  friend[a].append(b)
  friend[b].append(a)

def dfs(s, depth):
  global flag
  if depth == 5:
    flag = True
    return

  nv = friend[s]

  for x in nv:
    if not visited[x]:
      visited[x] = True
      dfs(x, depth + 1)
      visited[x] = False

for i in range (n):
  if not flag:
    dfs(i, 0)

print(1) if flag else print(0)