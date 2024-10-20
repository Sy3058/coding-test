N = int(input()) # 명령어 개수
stack = []

for _ in range (N):
  c = input().split() # 명령어
  if c[0] == 'push': # 정수 X를 스택에 넣음
    stack.append(int(c[1]))
  elif c[0] == 'pop': # 가장 위에 있는 정수를 빼고 출력, 없으면 -1
    if stack: # stack에 숫자가 있다면
      popnum = stack.pop()
      print(popnum)
    else:
      print(-1)
  elif c[0] == 'size': # satck에 들어있는 정수의 개수 출력
    print(len(stack))
  elif c[0] == 'empty': # stack이 비어있으면 1, 아니면 0 출력
    if stack:
      print(0)
    else:
      print(1)
  else: # 스택 가장 위에 있는 정수를 출력, 없으면 -1
    if stack:
      print(stack[-1])
    else:
      print(-1)