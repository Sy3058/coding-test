import sys
from collections import deque

text = input()
N = len(text)
M = int(input())

# 초기 커서 위치 기준 왼쪽에 모든 text가 존재
left = deque(text)
right = deque()

for _ in range (M):
  command = sys.stdin.readline().strip()

  if command == "L":
    if left: # 커서가 문장의 맨 앞일 때 제외
      right.appendleft(left.pop()) # 왼쪽 스택의 오른쪽 끝 엘리먼트를 가져와 오른쪽 스택의 왼쪽 끝에 삽입
  elif command == "D":
    if right: # 커서가 문장의 맨 뒤일 때 제외
      left.append(right.popleft()) # 오른쪽 스택의 왼쪽 끝 엘리먼트를 가져와 왼쪽 스택의 오른쪽 끝에 삽입
  elif command == "B":
    if left: # 커서가 문장의 맨 앞일 때 제외
      left.pop() # 왼쪽 스택의 오른쪽 끝 엘리먼트 삭제
  else:
    left.append(command[2]) # 왼쪽 스택의 오른쪽 끝에 삽입

print(''.join(left) + ''.join(right))