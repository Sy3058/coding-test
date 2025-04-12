import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
board = [list(map(int, input().split())) for _ in range (n)]
plan = list(map(int, input().split()))
for i in range (m):
  plan[i] -= 1 # 인덱스를 맞추기 위해

def bfs(s, e):
  if s == e:
    return True
  nv = deque([s])
  visited = [False] * (n)
  flag = False

  while nv:
    x = nv.popleft()
    visited[x] = True

    for i in range (n):
      if not visited[i] and board[x][i] == 1: # x와 연결된 i를 찾음
        if i == e:
          flag = True
          break
        else:
          nv.append(i)
    
    if flag: break
  return flag

ans = 'YES'
for i in range (1, m):
  if bfs(plan[i-1], plan[i]):
    continue
  else:
    ans = 'NO'
    break

print(ans)