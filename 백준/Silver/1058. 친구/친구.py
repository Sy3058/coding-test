import sys
input = sys.stdin.readline

n = int(input())
f = [list(input().strip()) for _ in range (n)]
con = [[0]*n for _ in range (n)]

for k in range (n):
  for i in range (n):
    for j in range (n):
      if i == j:
        continue
      if f[i][j] == 'Y' or (f[i][k] == 'Y' and f[k][j] == 'Y'): # ij가 친구이거나 ik와 kj가 친구라서 ij가 친구가 되는 경우
        con[i][j] = 1

ans = 0
for row in con:
  ans = max(ans, sum(row))

print(ans)