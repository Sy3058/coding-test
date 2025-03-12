import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))

board = [[False]*n for _ in range (n)]
ans = 0

for i in range (n-1):
  b = height[i] # 지금 빌딩의 높이
  stack = []
  s = height[i+1] - height[i] # 기울기
  board[i][i+1], board[i+1][i] = True, True # 바로 옆의 빌딩은 무조건 볼 수 있음

  for j in range (i+2, n):
    h = height[j] # 다음 빌딩의 높이
    eh = b + s*(j-i) # 다음 빌딩의 기대되는 높이

    if h > eh: # 그 다음 빌딩을 볼 수 있는 경우
      s = (h - b) / (j-i) # 기울기 변경
      board[i][j], board[j][i] = True, True
    
for i in range (n):
  ans = max(ans, board[i].count(True))

print(ans)