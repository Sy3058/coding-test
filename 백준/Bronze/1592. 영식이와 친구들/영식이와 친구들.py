import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = [0] * (n + 1) # 1부터 N까지 자리에 앉아있음
x = 1
arr[x] = 1 # 1번이 공을 받음
while max(arr) < m: # 한 사람이 공을 M번 받기 전까지
  if arr[x] % 2 == 1: # 받은 횟수가 홀수인 경우
    nx = (x + l) % n
    if nx == 0:
      nx = n
  
  else: # 받은 횟수가 짝수인 경우
    nx = (x - l) % n
    if nx == 0:
      nx = n
  
  arr[nx] += 1
  x = nx

print(sum(arr) - 1)