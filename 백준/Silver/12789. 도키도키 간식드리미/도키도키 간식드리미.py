import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque((map(int, sys.stdin.readline().split())))
side = deque([])
flag = True

for i in range (1, N+1):
  if i in arr:
    while arr[0] != i:
      tmp = arr.popleft()
      side.append(tmp)
    arr.popleft() # i 제거
  
  elif side[-1] == i:
    side.pop()
  
  else: # 공간에 있는 사람은 대기열로 돌아갈 수 없으므로 i가 arr에 없고 side[-1]도 아닌 경우 처리 불가
    flag = False
    break

print("Nice" if flag else "Sad")