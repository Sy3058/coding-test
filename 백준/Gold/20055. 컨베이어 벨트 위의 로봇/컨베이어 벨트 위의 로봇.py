import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = [False]*n
cnt = 0
level = 0

def rt():
  global cnt
  global level
  # belt: deque, robot: list

  belt.rotate() # 벨트 회전
  robot[-1] = False
  for i in range (n-2, -1, -1): # 벨트 따라 로봇 이동
    if robot[i]:
      if i+1 != n-1: robot[i+1] = True
      robot[i] = False
  
  for i in range (n-2, -1, -1): # 로봇 이동
    if robot[i] and not robot[i+1] and belt[i+1] != 0: # 현재 칸에 로봇이 있고 다음 칸에 로봇이 없고 내구도가 0이 아닌 경우
      robot[i] = False
      if i+1 != n-1: robot[i+1] = True
      belt[i+1] -= 1
      if belt[i+1] == 0: cnt += 1
  
  if belt[0] != 0: # 로봇 올리기
    robot[0] = True
    belt[0] -= 1
    if belt[0] == 0:
      cnt += 1

while cnt < k:
  rt()
  level += 1

print(level)