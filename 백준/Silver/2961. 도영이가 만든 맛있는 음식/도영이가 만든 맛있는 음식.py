import sys
input = sys.stdin.readline

n = int(input())
ing = []
for _ in range (n):
  s, b = map(int, input().split())
  ing.append((s, b))

visited = [False] * n
md = float('inf') # min difference

def cook(cnt):
  global ni, ts, tb, md
  if cnt == ni:
    md = min(abs(ts - tb), md)
    return
  
  for i in range (n):
    if not visited[i]:
      ts *= ing[i][0]
      tb += ing[i][1]
      visited[i] = True
      cook(cnt + 1)
      ts //= ing[i][0]
      tb -= ing[i][1]
      visited[i] = False

for ni in range (1, n+1): # number of ingredients
  ts, tb = 1, 0
  cook(0)

print(md)