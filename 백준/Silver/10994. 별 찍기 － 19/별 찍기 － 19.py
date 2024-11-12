import sys

s = int(sys.stdin.readline()) # 별의 개수
length = (4*s) - 3 # 위/아래 변의 길이
arr = [[' ']*(length) for _ in range(length)] # length * length 크기의 arr 안에 별이 찍힘

def star(n, x, y):
  global arr

  length = (4*n) -3
  if n == 1:
    arr[x][y] = '*'
    return
  
  for i in range (length):
    # 바깥 테두리의 별은 항상 length만큼 찍힘
    arr[x][y+i] = '*' # 윗변
    arr[y+i][x] = '*' # 좌측변
    arr[x+length-1][y+i] = '*' # 아랫변
    arr[x+i][y+length-1] = '*' # 우측변
  
  star(n-1, x+2, y+2) # n이 하나 줄어들 때 x와 y는 2씩 증가
  return

star(s, 0, 0)

for i in range(length):
  print(''.join(map(str, arr[i])))
