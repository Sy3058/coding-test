from collections import deque

for tc in range (1, int(input()) + 1):
  n = int(input())
  house = tuple(map(int, input().split()))
  shop = [tuple(map(int, input().split())) for _ in range (n+1)]
  dest = shop[-1]
  visited = [False] * (n + 1)

  def bfs(start):
    nv = deque([start])

    while nv:
      x, y = nv.popleft()

      for i in range (n + 1):
        nx, ny = shop[i]
        
        if not visited[i]:
          if abs(nx - x) + abs(ny - y) <= 1000:
            if (nx, ny) == dest:
              return "happy"
            visited[i] = True
            nv.append((nx, ny))
    return "sad"
  
  print(bfs(house))
