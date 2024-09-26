import sys

sen = sys.stdin.readline().strip()
arrow = False
stack = []
answer = []

for s in sen:
  if s == '<':
    if stack:
      stack.reverse()
      answer.extend(stack)
      stack = []
    arrow = True # 괄호 열림
    answer.append(s)
  elif s == '>':
    arrow = False # 괄호 닫힘
    answer.append(s)
  elif s == ' ':
    if arrow == False:
      stack.reverse()
      answer.extend(stack)
      stack = []
    answer.append(s)
  elif arrow == True:
    answer.append(s)
  else:
    stack.append(s)

stack.reverse()
answer.extend(stack) # 마지막 부분 처리

print(''.join(answer))