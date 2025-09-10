import sys
input = sys.stdin.readline

for tc in range (1, int(input()) + 1):
  n = int(input())
  house = tuple(map(int, input().split()))
  shop = [tuple(map(int, input().split())) for _ in range (n)]
  dest = tuple(map(int, input().split()))
  visited = [False] * (n + 1)

  def dfs(start):
    x, y = start

    if abs(x - dest[0]) + abs(y - dest[1]) <= 1000:
      return True

    for i in range (n):
      if not visited[i]:
        nx, ny = shop[i]
        if abs(nx - x) + abs(ny - y) <= 1000:
          visited[i] = True
          if dfs((nx, ny)):
            return True
    return False
  
  print('happy' if dfs(house) else 'sad')
