import sys
input = sys.stdin.readline

n = int(input())
b = [] # building
for _ in range (n):
  x, y = map(int, input().split())
  b.append(y)

stack = []
cnt = 0

for i in range (n):
  if stack:
    if b[i] == 0:
      cnt += len(stack)
      stack = []
    
    elif b[i] > stack[-1]:
      stack.append(b[i])
    
    else:
      while stack and b[i] < stack[-1]:
        stack.pop()
        cnt += 1
      
      while stack and b[i] == stack[-1]:
        stack.pop()
      
      stack.append(b[i])

  else:
    if b[i] != 0:
      stack.append(b[i])

cnt += len(stack)

print(cnt)