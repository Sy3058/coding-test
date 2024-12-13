import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range (n)]
ans = 64

def count(x, y):
  arr = [board[k][y:y+8] for k in range (x, x+8)]

  ow, ob = 0, 0 # 홀수 (홀짝 짝홀인 경우)
  ew, eb = 0, 0 # 짝수 (짝짝 홀홀인 경우)

  for i in range (8):
    for j in range (8):
      if i%2 != j%2: # 홀짝, 짝홀인 경우
        if arr[i][j] == 'W':
          ow += 1
        else:
          ob += 1
      else:
        if arr[i][j] == 'W':
          ew += 1
        else:
          eb += 1
  
  c1 = 32-ew + 32-ob # 홀수 자리에 b만 짝수 자리에 w만
  c2 = 32-ow + 32-eb # 홀수 자리에 w만 짝수 자리에 b만

  return min(c1, c2)

for a in range (n-7):
  for b in range (m-7):
    tmp = count(a, b)
    ans = min(tmp, ans)

print(ans)
