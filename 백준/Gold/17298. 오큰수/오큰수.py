import sys

n = int(sys.stdin.readline()) # size of array
arr = list(map(int, sys.stdin.readline().split())) # array
nge = []

stack = []
for i in range (n-1, -1, -1): # 뒤에서부터 검사
  while stack and stack[-1] <= arr[i]: # stack에 있는 수보다 arr[i]가 더 크면 왼쪽에서 확인할 때 무조건 arr[i]가 먼저 검사됨. 따라서 stack[-1] 보다 arr[i]가 크면 stack에서 stack[-1]을 제거.
    stack.pop()

  if stack:
    nge.append(stack[-1])
  else:
    nge.append(-1) # 오른쪽에 큰 수가 없는 경우

  stack.append(arr[i])

nge.reverse()

print(' '.join(map(str, nge)))