import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (n)] # 입력 배열
visited = [[False]*m for _ in range (n)] # 방문했는지 확인하는 배열

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = 0

# ㅏ를 제외한 나머지 모양 탐색
def dfs(x, y, tmp, cnt):
  global ans

  if cnt == 4: # 테트로미노가 된 경우
    ans = max(ans, tmp)
    return

  for dx, dy in directions: # 방향 탐색
    nx, ny = x+dx, y+dy

    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True # 방문 처리
      dfs(nx, ny, tmp+board[nx][ny], cnt+1)
      visited[nx][ny] = False

# ㅏ 모양
def ex(x, y):
  global ans
  arr = []
  for dx, dy in directions:
    nx, ny = x+dx, y+dy

    if 0 <= nx < n and 0 <= ny < m:
      arr.append(board[nx][ny])
  
  l = len(arr)
  if l == 4: # 네 방향이 모두 포함되었다면 가장 작은 한 방향을 삭제하면 ㅏ 모양이 됨
    arr.sort(reverse = True)
    arr.pop()
    ans = max(ans, sum(arr) + board[x][y])
  elif l == 3: # ㅏ 모양
    ans = max(ans, sum(arr) + board[x][y])
  return # l == 2이면 ㅏ 모양 불가

for i in range (n):
  for j in range (m):
    visited[i][j] = True
    dfs(i, j, board[i][j], 1)
    ex(i, j)
    visited[i][j] = False

print(ans)