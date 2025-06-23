import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range (n)]
price = float('inf')
visited = [False] * n

def circuit(s, tmp, cnt):
  global price
  global i
  if cnt == n and s == i:
    price = min(price, tmp)
    return
  
  if tmp >= price:
    return
  
  for j in range (n):
    if arr[s][j] != 0 and not visited[j]:
      tmp += arr[s][j]
      visited[j] = True
      circuit(j, tmp, cnt + 1)
      tmp -= arr[s][j]
      visited[j] = False

for i in range (n):
  circuit(i, 0, 0)
print(price)