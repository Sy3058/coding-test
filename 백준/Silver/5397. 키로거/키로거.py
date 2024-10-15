import sys
from collections import deque

n = int(sys.stdin.readline()) # number of test case

for _ in range (n):
  text = sys.stdin.readline().strip()
  left = deque()
  right = deque()

  for t in text:
    if t == '<':
      if left: # 커서 왼쪽에 무언가 존재한다면
        right.appendleft(left.pop()) # 왼쪽에서 오른쪽으로 이동
    elif t == '>':
      if right: # 커서 오른쪽에 무언가 존재한다면
        left.append(right.popleft()) # 오른쪽에서 왼쪽으로 이동
    elif t == '-':
      if left: # 커서 왼쪽에 무언가 존재한다면
        left.pop() # 왼쪽에서 문자 삭제
    else: # cmd가 아닌 것이 들어오는 경우
      left.append(t) # 왼쪽에 문자 추가 (커서가 문자 오른쪽으로 이동하므로 왼쪽에 추가되는 것과 동일)
  result = ''.join(left) + ''.join(right)
  print(result)