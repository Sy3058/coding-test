import sys
input = sys.stdin.readline

n = int(input())
post = input().strip()
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = {alpha[i]:int(input()) for i in range (n)}
op = {'*', '+', '/', '-'}
stack = []

for i in range (len(post)):
  if post[i] in op:
    right = stack.pop()
    left = stack.pop()
    tmp = eval(str(left)+post[i]+str(right)) # str문을 바로 계산
    stack.append(tmp)
  else:
    stack.append(num[post[i]]) # 알파벳에 해당하는 값

print('%0.2f'%stack[0])