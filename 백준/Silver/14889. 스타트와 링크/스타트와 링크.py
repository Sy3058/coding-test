import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range (n)]
visited = [False] * n
ans = float('inf')

def dfs(depth, idx):
  global ans
  if depth == n // 2: # 절반은 다른 팀에 배정되므로 절반만 확인
    a, b = 0, 0 # a팀과 b팀
    
    for i in range (n):
      for j in range (n):
        if visited[i] and visited[j]: # 방문했으면 a팀에 배정
          a += board[i][j]
        
        elif not visited[i] and not visited[j]: # 방문하지 않았으면 b팀에 배정
          b += board[i][j]
    
    ans = min(ans, abs(a - b)) # 둘의 차이를 확인
    return
  
  for i in range (idx, n): # 백트래킹
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, i + 1)
      visited[i] = False

dfs(0, 0)
print(ans)