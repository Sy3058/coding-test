import sys

n = int(sys.stdin.readline())
arr = [(list(map(int, sys.stdin.readline().split()))) for _ in range (n)]
minus = 0 # -1로 채워진 종이
zero = 0 # 0으로 채워진 종이
plus = 0 # 1로 채워진 종이

def cut(x, y, n):
  global minus, zero, plus
  
  if n == 1:
    if arr[x][y] == -1:
      minus += 1
    elif arr[x][y] == 0:
      zero += 1
    else:
      plus += 1
  
  else:
    tmp_arr = []
    for i in range (x, x+n):
      tmp_arr.extend(arr[i][y:y+n])

    if len(set(tmp_arr)) != 1:
      cut(x, y, n//3)
      cut(x, y+n//3, n//3)
      cut(x, y+2*n//3, n//3)
      cut(x+n//3, y, n//3)
      cut(x+n//3, y+n//3, n//3)
      cut(x+n//3, y+2*n//3, n//3)
      cut(x+2*n//3, y, n//3)
      cut(x+2*n//3, y+n//3, n//3)
      cut(x+2*n//3, y+2*n//3, n//3)
    
    else:
      if arr[x][y] == -1:
        minus += 1
      elif arr[x][y] == 0:
        zero += 1
      else:
        plus += 1

cut(0, 0, n)

print(minus)
print(zero)
print(plus)