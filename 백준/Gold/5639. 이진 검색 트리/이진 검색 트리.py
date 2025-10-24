import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
  try:
    num = int(input())
    arr.append(num)
  except:
    break

def sol(arr):
  if len(arr) == 0:
    return
  
  tmp_l, tmp_r = [], []
  mid = arr[0]
  for i in range (1, len(arr)):
    if arr[i] > mid: # 루트노드보다 작은 수까지가 왼쪽 배열, 그 이후는 오른쪽 배열
      tmp_l = arr[1:i]
      tmp_r = arr[i:]
      break
  # 모두 mid보다 작은 경우
  else:
    tmp_l = arr[1:]
  
  sol(tmp_l)
  sol(tmp_r)
  print(mid)

sol(arr)