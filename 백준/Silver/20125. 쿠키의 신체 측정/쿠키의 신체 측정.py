import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range (n)]
cookie = [[] for _ in range (n)] # 몸의 위치
cc = [0 for _ in range (n)] # *의 개수
head = []

for i in range (n):
  for j in range (n):
    if arr[i][j] == '*':
      if len(head) == 0:
        head = [i, j]
      cookie[i].append((i, j))
      cc[i] += 1

heart = (head[0]+1, head[1])
larm = heart[1] - cookie[head[0]+1][0][1] # 왼쪽 팔 길이
rarm = cookie[head[0]+1][-1][1] - heart[1] # 오른쪽 팔 길이

for i in range (head[0]+1, n):
  if cc[i] == 2:
    lleg = cookie[i][0] # 왼쪽 다리 위치
    rleg = cookie[i][1] # 오른쪽 다리 위치
    break

waist = lleg[0] - heart[0] - 1 # 허리 길이이
llleg = 0 # 왼쪽 다리 길이
lrleg = 0 # 오른쪽 다리 길이이

for i in range (lleg[0], n):
  if cc[i] == 2:
    llleg += 1
    lrleg += 1
  elif cc[i] == 1:
    if cookie[i][0][1] == lleg[1]:
      llleg += 1
    else:
      lrleg += 1
  else:
    break

print(heart[0]+1, heart[1]+1)
print(larm, rarm, waist, llleg, lrleg)