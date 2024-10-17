import sys

# 입력
H, W, X, Y = map(int, sys.stdin.readline().split())
A = [[0]*W for _ in range (H)]
B = [[] for _ in range (H+X)]

for i in range (H+X):
  element = list(map(int, sys.stdin.readline().split())) # B의 원소
  B[i] = element

if Y>W or X>H: # 겹치는 부분이 생기지 않음
  A = B
elif X == 0 and Y == 0: # 모든 부분이 겹침
  for i in range (H):
    for j in range (W):
      A[i][j] = int(B[i][j]/2)
else: # 겹치는 부분이 있을 때
  for i in range (H):
    for j in range (W):
      if i<X or j<Y: # 겹치지 않는 부분
        A[i][j] = B[i][j]
      else: # 겹치는 부분
        A[i][j] = B[i][j] - A[i-X][j-Y]

for h in range (H):
  print(' '.join(map(str,A[h])))