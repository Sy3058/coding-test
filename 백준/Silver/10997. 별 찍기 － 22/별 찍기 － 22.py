s = int(input())
w = 4*s - 3
h = 4*s - 1
arr = [[' ']*w for _ in range (h)]

def star(n, x, y):
  global arr

  w = 4*n - 3
  h = 4*n - 1
  if n == 1:
    arr[x][y] = '*'
    return
  
  if n == 2:
    arr[x-1][y] = '*'
    for i in range (y-2, y-2+w):
      arr[x-4][i] = '*' # 윗변
      arr[x+2][i] = '*' # 아랫변
      if i != y-1:
        arr[x-2][i] = '*'
    
    for j in range (x-4, x-4+h):
      arr[j][y-2] = '*' # 왼쪽변
      if j != x-3:
        arr[j][y+2] = '*'
  
  else:
    arr[x-2*(n-1)][y+2*n-3] = '*'
    for i in range (y-2*(n-1), y-2*(n-1)+w):
      arr[x-2*n][i] = '*' # 윗변
      arr[x+2*(n-1)][i] = '*' # 아랫변
    
    for j in range (x-2*n, x-2*n+h):
      arr[j][y-2*(n-1)] = '*'
      if j != x-2*n+1:
        arr[j][y+2*(n-1)] = '*'
  
  star(n-1, x, y)
  return


if s == 1:
  print ('*')

else:
  star(s, 2*s, 2*s-2)

  for i in range (h):
    print(''.join(map(str, arr[i])).rstrip())