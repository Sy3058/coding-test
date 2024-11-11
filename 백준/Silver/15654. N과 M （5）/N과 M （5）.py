n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
arr = []
visited = [False] * n

def dfs():
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return

  for i in range (n):
    if visited[i] == True:
      continue

    visited[i] = True
    arr.append(num_list[i])
    dfs()
    arr.pop()
    visited[i] = False

dfs()