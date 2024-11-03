n, m = map(int, input().split())

arr = []
visited = [[False] * (n+1) for _ in range (m)]

def dfs():
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range (1, n+1):
    for j in range (m):
      if visited[len(arr)][i] == True:
        continue
      
      visited[(len(arr))][i] = True
      arr.append(i)
      dfs()
      arr.pop()
    visited[len(arr)][i] = False

dfs()
