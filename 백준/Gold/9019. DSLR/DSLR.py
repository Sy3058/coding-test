import sys
from collections import deque
input = sys.stdin.readline

for tc in range (1, int(input()) + 1):
  a, b = map(int, input().split()) # a는 초기값 b는 최종 값
  nv = deque([(a, "")])
  visited = [False] * 10000
  visited[a] = True

  while nv:
    num, command = nv.popleft()

    if num == b:
      print(command)
      break

    d1 = num//1000
    d2 = (num % 1000) // 100
    d3 = (num % 100) // 10
    d4 = (num % 10)
    
    dnum = (num * 2) % 10000
    snum = num - 1 if num != 0 else 9999 # num = 0이면 num-1은 9999
    lnum = ((d2 * 10 + d3) * 10 + d4) * 10 + d1 # 1234 -> 2341
    rnum = ((d4 * 10 + d1) * 10 + d2) * 10 + d3 # 1234 -> 4123

    if not visited[dnum]:
      visited[dnum] = True
      nv.append((dnum, command + "D"))
    
    if not visited[snum]:
      visited[snum] = True
      nv.append((snum, command + "S"))
    
    if not visited[lnum]:
      visited[lnum] = True
      nv.append((lnum, command + "L"))
    
    if not visited[rnum]:
      visited[rnum] = True
      nv.append((rnum, command + "R"))