t = int(input())

for _ in range (t):
  ps = input()
  stack = []
  flag = True

  if ps[0] == ')': # )로 시작하면 절대 성립할 수 없음
    print('NO')
    continue

  for p in ps:
    if p == '(':
      stack.append(0)
    
    else:
      if stack:
        stack.pop()
      else:
        flag = False
        break
  
  if stack or not flag: # stack에 남은 값이 있거나 flag가 false인 경우
    print('NO')
  else:
    print('YES')
