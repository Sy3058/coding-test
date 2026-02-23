import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(input()) for _ in range (n
)]

prefix = [[0] * (m+1) for _ in range (n+1)]

# 패턴 하나에서 다시 칠해야 하는 칸이 X개라면 나머지 패턴은 K**2 - X이므로 패턴 하나(B로 시작)만 확인
# i,j가 홀홀 짝짝이면 B 반대는 W
for i in range (n):
  for j in range (m):
    if  (i+j) % 2 == 0: # 짝짝이거나 홀홀
      if board[i][j] == 'W':
        prefix[i+1][j+1] = 1 + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
      else:
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
    else:
      if board[i][j] == 'B':
        prefix[i+1][j+1] = 1 + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
      else:
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

ansA = float('inf') # 패턴1이 최소일 때 정답
ansB = 0 # 패턴2가 최소이려면 패턴1에서 최대여야 뺐을 때 최소
for i in range (n-k+1):
  for j in range (m-k+1):
    repaint = prefix[i+k][j+k] - prefix[i][j+k] - prefix[i+k][j] + prefix[i][j]
    ansA = min(ansA, repaint)
    ansB = max(ansB, repaint)

if ansA < k**2 - ansB:
  print(ansA)
else:
  print(k**2 - ansB)