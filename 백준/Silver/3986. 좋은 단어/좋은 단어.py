import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range (N):
  word = sys.stdin.readline().strip()
  stack = []
  flag = True

  for w in word:
    if not stack:
      stack.append(w)
    
    else:
      if stack[-1] == w:
        stack.pop()
      
      elif stack[-1] != w:
        stack.append(w)
  
  if not stack: # 스택이 비어있다면 좋은 문자
    cnt += 1

print(cnt)