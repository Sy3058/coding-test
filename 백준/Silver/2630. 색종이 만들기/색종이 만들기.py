import sys

n = int(sys.stdin.readline())
arr = [[] for _ in range (n)]
result = []

for i in range (n):
  li = list(map(int, sys.stdin.readline().split()))
  arr[i] = li

def cut(x, y, n):
  color = arr[x][y]
  for i in range(x, x+n): # x 끝까지 확인
    for j in range (y, y+n): # y 끝까지 확인
      if color != arr[i][j]: # 색이 다른 부분이 있다면
        half = n//2
        cut(x, y, half) # 2사분면
        cut(x+half, y, half) # 1사분면
        cut(x, y+half, half) # 3사분면
        cut(x+half, y+half, half) # 4사분면
        return
  if color == 0: # 색이 모두 같다면 result에 추가
    result.append(0)
  else:
    result.append(1)

cut(0,0,n)
print(result.count(0)) # 0의 갯수가 하얀색의 갯수
print(result.count(1)) # 1의 갯수가 파란색의 갯수