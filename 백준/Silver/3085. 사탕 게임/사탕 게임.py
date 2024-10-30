import sys

n = int(sys.stdin.readline())
c = [list(sys.stdin.readline()) for _ in range(n)]

def checkCurMaxNum():
  max_cnt =1
  for i in range (n):
    # 가로
    cnt = 1
    for j in range (1, n):
      if c[i][j] == c[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      max_cnt = max(cnt, max_cnt)
    
    # 세로
    cnt = 1
    for j in range (1, n):
      if c[j][i] == c[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      max_cnt = max(cnt, max_cnt)
  
  return max_cnt

# 오른쪽 swap, 아래쪽 swap
result = 1
for i in range (n):
  for j in range (n-1):
    # 오른쪽 swap
    if j + 1 < n and c[i][j] != c[i][j+1]:
      c[i][j], c[i][j+1] = c[i][j+1], c[i][j] # swap
      result = max(result, checkCurMaxNum())
      c[i][j], c[i][j+1] = c[i][j+1], c[i][j] # return
    # 왼쪽 swap
    if i+1 < n and c[i][j] != c[i+1][j]:
      c[i][j], c[i+1][j] = c[i+1][j], c[i][j] # swap
      result = max(result, checkCurMaxNum())
      c[i][j], c[i+1][j] = c[i+1][j], c[i][j] # return

print(result)