import sys

n = int(sys.stdin.readline()) # number of tower
towers = list(map(int, sys.stdin.readline().split()))
stack = []
result = []

for i in range (n):
  # i번째 탑보다 왼쪽에 있는 탑 중에서 자신보다 높은 탑을 찾음
  while stack and stack[-1][1] < towers[i]: # stack이 존재하고 마지막 stack의 높이가 tower보다 낮을 경우
    stack.pop()

  if stack:
    result.append(stack[-1][0] + 1) # 신호를 받은 타워의 인덱스
  else:
    result.append(0) # 신호를 받는 탑이 없는 경우

  stack.append((i, towers[i])) # 현재 탑의 인덱스와 높이를 스택에 추가

print(" ".join(map(str, result)))