import sys

sen = sys.stdin.readline().rstrip()

while sen != '.':
  stack = []
  balance = True # 괄호의 균형이 맞는 상태인지 확인
  for i in range (len(sen)):
    if sen[i] == '(':
      stack.append(sen[i])
    elif sen[i] == '[':
      stack.append(sen[i])
    elif sen[i] == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        balance = False
        break # )만 나오는 경우 뒤에 뭐가 나와도 balance가 맞지 않음
    elif sen[i] == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        balance = False
        break
  if balance and not stack:
    print('yes')
  else:
    print('no')
  sen = sys.stdin.readline().rstrip()