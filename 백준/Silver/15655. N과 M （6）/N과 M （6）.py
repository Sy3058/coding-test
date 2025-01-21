import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
arr = []
visited = [False] * n

def dfs():
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in range (n):
    if visited[i]:
      continue

    if arr and arr[-1] > num[i]:
      continue

    visited[i] = True
    arr.append(num[i])
    dfs()
    arr.pop()
    visited[i] = False

dfs()